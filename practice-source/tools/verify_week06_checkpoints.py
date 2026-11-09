from pathlib import Path
import os,json,tempfile,zipfile,subprocess,time,urllib.request,urllib.parse,http.cookiejar,re,html
root=Path(__file__).resolve().parents[1]
dotnet=os.environ.get('DOTNET','dotnet')
env=dict(os.environ,ASPNETCORE_ENVIRONMENT='Development',DOTNET_CLI_TELEMETRY_OPTOUT='1')
results=[]
with tempfile.TemporaryDirectory(prefix='week06-steps-',dir=root) as td:
 for step in range(8):
  with zipfile.ZipFile(root/f'downloads/Week06-step{step:02d}.zip') as z:z.extractall(td)
  p=Path(td)/f'Week06-Step{step:02d}'
  r=subprocess.run([dotnet,'build',str(p),'--disable-build-servers','-p:UseSharedCompilation=false'],env=env,capture_output=True,text=True)
  assert r.returncode==0,r.stdout+r.stderr
  url=f'http://127.0.0.1:{5310+step}/';log=tempfile.TemporaryFile()
  server=subprocess.Popen([dotnet,'run','--project',str(p),'--no-build','--no-launch-profile','--urls',url],cwd=p,env=env,stdout=log,stderr=log)
  try:
   client=urllib.request.build_opener(urllib.request.ProxyHandler({}),urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
   for _ in range(100):
    try:client.open(url,timeout=1);break
    except Exception:time.sleep(.1)
   valid={'Input.DisplayName':'小安','Input.Email':'student-a@example.com','Input.Session':'週三晚上','Input.Note':''}
   for name,data,ok in [('valid',valid,True),('bad-email',{**valid,'Input.Email':'abc'},step<3),('blank',dict.fromkeys(valid,''),step<3),('boundary-pass',{**valid,'Input.DisplayName':'A'*(15 if step==7 else 20)},True),('boundary-fail',{**valid,'Input.DisplayName':'A'*(16 if step==7 else 21)},step<3)]:
    page=client.open(url).read().decode();token=html.unescape(re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"',page)[1])
    body=html.unescape(client.open(url,urllib.parse.urlencode({**data,'__RequestVerificationToken':token}).encode()).read().decode())
    success='報名資料已收到' if step<4 else '報名資料驗證通過'
    assert (success in body)==ok,(step,name,'summary')
    if step>=4 and name=='bad-email':assert 'Email 格式不正確' in body
    if step==3 and name=='bad-email':assert 'data-valmsg-for="Input.Email"' not in body
   results.append(f'Step {step:02d}: build + valid/bad-email/blank/boundary-pass/boundary-fail POST PASS');print(results[-1],flush=True)
  finally:
   server.terminate();server.wait(timeout=10);log.close()
(root/'week06-checkpoints-verification.txt').write_text('\n'.join(results)+'\nTested on macOS arm64 / .NET 10; Windows Visual Studio UI not executed.\n')
