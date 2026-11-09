from pathlib import Path
import os,json,tempfile,zipfile,subprocess,time,urllib.request,urllib.parse,http.cookiejar,re,html
root=Path(__file__).resolve().parents[1]
dotnet=os.environ.get('DOTNET','dotnet')
env=dict(os.environ,DOTNET_CLI_TELEMETRY_OPTOUT='1')
env.pop('ASPNETCORE_ENVIRONMENT',None)
results=[]
with tempfile.TemporaryDirectory(prefix='week06-steps-',dir=root) as td:
 with zipfile.ZipFile(root/'downloads/Week06-starter.zip') as z:z.extractall(td)
 p=Path(td)/'Week06Validation'
 checkpoints=json.loads((root/'src/week06/checkpoints.json').read_text())
 for step in range(8):
  if step in [2,3,7]:(p/'Pages/Index.cshtml.cs').write_text(checkpoints[step]['handler'])
  if step==4:(p/'Pages/Index.cshtml').write_text(checkpoints[step]['form'])
  assert (p/'Pages/Index.cshtml.cs').read_text()==checkpoints[step]['handler']
  assert (p/'Pages/Index.cshtml').read_text()==checkpoints[step]['form']
  r=subprocess.run([dotnet,'build',str(p),'--disable-build-servers','-p:UseSharedCompilation=false'],env=env,capture_output=True,text=True)
  assert r.returncode==0,r.stdout+r.stderr
  url=f'http://127.0.0.1:{5310+step}/';log=tempfile.TemporaryFile()
  server=subprocess.Popen([dotnet,'run','--project',str(p),'--no-build','--launch-profile','http','--urls',url],cwd=p,env=env,stdout=log,stderr=log)
  try:
   client=urllib.request.build_opener(urllib.request.ProxyHandler({}),urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
   for _ in range(100):
    try:client.open(url,timeout=1);break
    except Exception:time.sleep(.1)
   else:raise RuntimeError('Server failed to start')
   page=client.open(url).read().decode()
   assert 'novalidate' in page
   assert '_ValidationScriptsPartial' not in page
   for asset in ['/css/site.css','/lib/bootstrap/dist/css/bootstrap.min.css']:
    response=client.open(url.rstrip('/')+asset);assert response.status==200 and 'css' in response.headers.get('Content-Type','')
   valid={'Input.DisplayName':'小安','Input.Email':'student-a@example.com','Input.Session':'週三晚上','Input.Note':''}
   for name,data,ok in [('valid',valid,True),('bad-email',{**valid,'Input.Email':'abc'},step<3),('blank',dict.fromkeys(valid,''),step<3),('boundary-pass',{**valid,'Input.DisplayName':'A'*(15 if step==7 else 20)},True),('boundary-fail',{**valid,'Input.DisplayName':'A'*(16 if step==7 else 21)},step<3),('note-100',{**valid,'Input.Note':'A'*100},True),('note-101',{**valid,'Input.Note':'A'*101},step<3),('corrected',valid,True),('invalid-after-success',{**valid,'Input.Email':'abc'},step<3)]:
    token=html.unescape(re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"',page)[1])
    body=html.unescape(client.open(url,urllib.parse.urlencode({**data,'__RequestVerificationToken':token}).encode()).read().decode())
    success='報名資料已收到' if step<4 else '報名資料驗證通過'
    assert (success in body)==ok,(step,name,'summary')
    if step>=4 and name in ['bad-email','invalid-after-success']:
     assert re.search(r'<span[^>]*data-valmsg-for="Input.Email"[^>]*>Email 格式不正確</span>',body)
     assert 'value="小安"' in body
    if step>=4 and name=='blank':
     for field,msg in [('DisplayName','請輸入顯示名稱'),('Email','請輸入 Email'),('Session','請選擇參加場次')]:assert re.search(fr'<span[^>]*data-valmsg-for="Input.{field}"[^>]*>{msg}</span>',body)
    if step>=4 and name=='note-101':assert re.search(r'<span[^>]*data-valmsg-for="Input.Note"[^>]*>備註最多 100 字</span>',body)
    page=body
    if step==3 and name=='bad-email':assert 'data-valmsg-for="Input.Email"' not in body
   results.append(f'Step {step:02d}: sequential edits + build + CSS + 9 chained POST cases PASS');print(results[-1],flush=True)
  finally:
   server.terminate();server.wait(timeout=10);log.close()
# Restore the exact course rule after the step07 experiment.
 (p/'Pages/Index.cshtml.cs').write_text(checkpoints[6]['handler'])
 assert 'StringLength(20' in (p/'Pages/Index.cshtml.cs').read_text()
(root/'week06-checkpoints-verification.txt').write_text('\n'.join(results)+'\nTested on macOS arm64 / .NET 10; Windows Visual Studio UI not executed.\n')
