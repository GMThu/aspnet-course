"""Recreate each taught checkpoint from dotnet new; test real POSTs and rebuild ZIPs.
Usage: DOTNET=/path/to/dotnet python3 tools/verify_walkthrough.py
Requires Python 3 and .NET 10 SDK. Run from any directory.
"""
from pathlib import Path
import platform,os,json,subprocess,tempfile,shutil,zipfile,time,urllib.request,urllib.parse,http.cookiejar,re,html
ROOT=Path(__file__).resolve().parents[1]
DOTNET=os.environ.get('DOTNET','dotnet')
ENV=dict(os.environ,DOTNET_CLI_TELEMETRY_OPTOUT='1',ASPNETCORE_ENVIRONMENT='Development')
C5=json.loads((ROOT/'src/code.json').read_text());C6=json.loads((ROOT/'src/week06/code.json').read_text())
records=[]
def build(project,label):
 r=subprocess.run([DOTNET,'build',str(project),'--disable-build-servers','-p:UseSharedCompilation=false'],env=ENV,capture_output=True,text=True)
 if r.returncode:raise RuntimeError(label+'\n'+r.stdout+r.stderr)
 records.append(label+': build PASS');print(records[-1],flush=True)
def post_tests(project,week,port):
 log=tempfile.TemporaryFile(mode='w+t')
 server=subprocess.Popen([DOTNET,'run','--project',str(project),'--no-build','--no-launch-profile','--urls',f'http://127.0.0.1:{port}'],cwd=project,env=ENV,stdout=log,stderr=log)
 url=f'http://127.0.0.1:{port}/'
 client=urllib.request.build_opener(urllib.request.ProxyHandler({}),urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
 try:
  for _ in range(100):
   try:client.open(url,timeout=1);break
   except Exception:
    if server.poll() is not None:raise RuntimeError('server stopped')
    time.sleep(.1)
  else:
   log.seek(0);raise RuntimeError('server did not start: '+log.read())
  success='報名資料已收到' if week==5 else '報名資料驗證通過'
  valid={'Input.DisplayName':'小安','Input.Email':'student-a@example.com','Input.Session':'週三晚上','Input.Note':''}
  cases=[('A',valid,True,['小安','student-a@example.com','無']),('B',{**valid,'Input.DisplayName':'小美','Input.Email':'student-b@example.com','Input.Session':'週六下午'},True,['小美','student-b@example.com','週六下午'])]
  if week==6:
   cases += [('blank',dict.fromkeys(valid,''),False,['請輸入顯示名稱','請輸入 Email','請選擇參加場次']),('bad-email',{**valid,'Input.Email':'abc'},False,['Email 格式不正確']),('missing-session',{**valid,'Input.Session':''},False,['請選擇參加場次']),('name-20',{**valid,'Input.DisplayName':'ABCDEFGHIJKLMNOPQRST'},True,[]),('name-21',{**valid,'Input.DisplayName':'ABCDEFGHIJKLMNOPQRSTU'},False,['顯示名稱最多 20 字']),('note-100',{**valid,'Input.Note':'A'*100},True,[]),('note-101',{**valid,'Input.Note':'A'*101},False,['備註最多 100 字']),('corrected',valid,True,[])]
  for name,data,ok,messages in cases:
   page=client.open(url).read().decode()
   assert success not in html.unescape(page),'fresh GET must not show summary'
   token=html.unescape(re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"',page).group(1))
   response=client.open(url,urllib.parse.urlencode({**data,'__RequestVerificationToken':token}).encode())
   content=html.unescape(response.read().decode())
   assert (success in content)==ok,(week,name,'success gate')
   for msg in messages:assert msg in content,(week,name,msg)
   if not ok and data['Input.Email']:assert f'value="{data["Input.Email"]}"' in content,'input not retained'
   records.append(f'Week{week} {name}: POST PASS');print(records[-1],flush=True)
 finally:
  server.terminate();server.wait(timeout=10)
def archive(project,name,step):
 info=f'''本包：{name}\n下一步：{step}\n\n1. ZIP 右鍵 → 全部解壓縮，到新的資料夾。不要在 ZIP 裡編輯。\n2. 找到同時有 Pages、wwwroot 與 Week05Registration.csproj 的那層。\n3. Visual Studio → 開啟專案或方案 → 選 Week05Registration.csproj。\n4. 需要 .NET 10 SDK 與 ASP.NET 與網頁程式開發工作負載；Ctrl+F5 執行。\n\n備份請放在專案資料夾外，避免備份 .cs 一起被編譯。\n本練習沒有資料庫，只使用假資料。\n第六週保留 Week05Registration 專案名稱，以延續第五週 namespace。\n'''
 if name.startswith('Week06'): info=info.replace('Week05Registration','Week06Validation').replace('第六週保留 Week06Validation 專案名稱，以延續第五週 namespace。','第六週使用獨立 Week06Validation 專案與 namespace。')
 folder='Week06Validation' if name.startswith('Week06') else 'Week05Registration'
 with zipfile.ZipFile(ROOT/'downloads'/name,'w',zipfile.ZIP_DEFLATED) as z:
  for f in sorted(project.rglob('*')):
   if f.is_file() and not any(x in ['bin','obj','.vs','.vscode'] for x in f.relative_to(project).parts):z.write(f,folder+'/'+f.relative_to(project).as_posix())
  z.writestr(folder+'/README.txt',info)
with tempfile.TemporaryDirectory(prefix='walkthrough-',dir=ROOT) as td:
 p=Path(td)/'Week05Registration'
 subprocess.run([DOTNET,'new','webapp','-n','Week05Registration','-f','net10.0','-o',str(p),'--no-restore'],env=ENV,check=True,stdout=subprocess.DEVNULL)
 build(p,'01 clean template');archive(p,'Week05-01-starter.zip','第五週第 02 步：先啟動首頁，再到第 03、04 步。尚未加入表單與自訂 CSS。')
 (p/'Pages/Index.cshtml').write_text(C5['form'])
 with (p/'wwwroot/css/site.css').open('a') as f:f.write('\n'+C5['css'])
 build(p,'04 form and CSS');archive(p,'Week05-02-form.zip','第五週第 05 步：接後端。表單與 CSS 已備妥，不必重貼樣式。')
 (p/'Pages/Index.cshtml.cs').write_text(C5['handler']);build(p,'05 backend with plain HTML form')
 (p/'Pages/Index.cshtml').write_text(C5['final']);build(p,'06 bound form and summary');post_tests(p,5,5215)
 archive(p,'Week05-03-complete.zip','第五週第 07 步驗收。也可複製本資料夾，開始第六週第 00 步。')
 for source in list(p.rglob('*')):
  if source.is_file() and not any(x in ['bin','obj'] for x in source.relative_to(p).parts):
   try: source.write_text(source.read_text().replace('Week05Registration','Week06Validation'))
   except UnicodeDecodeError: pass
 (p/'Week05Registration.csproj').rename(p/'Week06Validation.csproj')
 (p/'Pages/Index.cshtml.cs').write_text(C6['handler']);build(p,'Week06 step03 validation backend before error UI')
 (p/'Pages/Index.cshtml').write_text(C6['form']);build(p,'Week06 step04 error UI');post_tests(p,6,5216)
 archive(p,'Week06-complete.zip','第六週第 05 步三路測試，再做第 06 步長度邊界。本包已包含驗證與錯誤訊息。')
for name,content in [('Index-form.cshtml.txt',C5['form']),('Index-complete.cshtml.txt',C5['final']),('Index.cshtml.cs.txt',C5['handler']),('site-week05.css.txt',C5['css'])]:(ROOT/'downloads'/name).write_text(content)
(ROOT/'walkthrough-verification.txt').write_text('\n'.join(records)+f'\n\nPlatform: {platform.system()} {platform.machine()} / .NET 10. Windows Visual Studio UI not executed.\n')
print('All walkthrough checkpoints and POST cases passed. Downloads rebuilt from tested checkpoints.')
