# -*- coding: utf-8 -*-
"""Verify the guide's missing-rule/gate/message demonstrations with actual POSTs."""
from pathlib import Path
import os, tempfile, zipfile, subprocess, time, urllib.request, urllib.parse, http.cookiejar, re, html
root = Path(__file__).resolve().parents[1]
dotnet = os.environ.get('DOTNET', 'dotnet')
env = dict(os.environ, DOTNET_CLI_TELEMETRY_OPTOUT='1')
env.pop('ASPNETCORE_ENVIRONMENT', None)
results = []
with tempfile.TemporaryDirectory(prefix='week06-experiment-', dir=root) as td:
    with zipfile.ZipFile(root/'downloads/Week06-complete.zip') as z:
        z.extractall(td)
    p = Path(td)/'Week06Validation'
    backend = (p/'Pages/Index.cshtml.cs').read_text()
    form = (p/'Pages/Index.cshtml').read_text()
    cases = [
        ('baseline-blank', backend, form, '', 'student-a@example.com', False, '請輸入顯示名稱'),
        ('baseline-email', backend, form, '小安', 'abc', False, 'Email 格式不正確'),
        ('corrected', backend, form, '小安', 'student-a@example.com', True, None),
        ('no-required', backend.replace('[Required(ErrorMessage = "請輸入顯示名稱")]', ''), form, '', 'student-a@example.com', False, 'The DisplayName field is required.'),
        ('no-gate', re.sub(r'if \(!ModelState.IsValid\)\s*\{\s*return;\s*\}', '', backend), form, '小安', 'abc', True, 'Email 格式不正確'),
        ('no-span', backend, re.sub(r'<span asp-validation-for="Input.Email"[^>]*></span>', '', form), '小安', 'abc', False, None),
    ]
    for name, handler, markup, display, email, success, message in cases:
        (p/'Pages/Index.cshtml.cs').write_text(handler)
        (p/'Pages/Index.cshtml').write_text(markup)
        build = subprocess.run([dotnet, 'build', str(p), '--disable-build-servers', '-p:UseSharedCompilation=false'], env=env, capture_output=True, text=True)
        assert build.returncode == 0, build.stdout + build.stderr
        url = 'http://127.0.0.1:5328/'
        with tempfile.TemporaryFile() as log:
            server = subprocess.Popen([dotnet, 'run', '--project', str(p), '--no-build', '--launch-profile', 'http', '--urls', url], cwd=p, env=env, stdout=log, stderr=log)
            try:
                client = urllib.request.build_opener(urllib.request.ProxyHandler({}), urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
                for _ in range(100):
                    try:
                        page = client.open(url, timeout=1).read().decode()
                        break
                    except Exception:
                        time.sleep(.1)
                else:
                    raise RuntimeError('Server failed to start')
                token = html.unescape(re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"', page)[1])
                data = {'Input.DisplayName': display, 'Input.Email': email, 'Input.Session': '週三晚上', 'Input.Note': '', '__RequestVerificationToken': token}
                body = html.unescape(client.open(url, urllib.parse.urlencode(data).encode()).read().decode())
                assert ('報名資料驗證通過' in body) == success, name
                errors = re.findall(r'<span[^>]*class="[^"]*field-validation-error[^>]*>(.*?)</span>', body)
                assert errors == ([message] if message else []), (name, errors)
                assert f'value="{email}"' in body, name
                if name == 'no-span':
                    assert 'data-valmsg-for="Input.Email"' not in body
                results.append(f'{name}: build + POST + visible errors + summary + retained Email PASS')
                print(results[-1], flush=True)
            finally:
                server.terminate()
                server.wait(timeout=10)
(root/'week06-experiments-verification.txt').write_text('\n'.join(results) + '\nmacOS arm64 / .NET 10; Windows Visual Studio UI not executed.\n')
