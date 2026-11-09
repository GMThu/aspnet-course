"""Generate every Week06 step from the tested Week05 complete project and canonical code."""
from pathlib import Path
import json, zipfile
ROOT=Path(__file__).resolve().parents[1]
c5=json.loads((ROOT/'src/code.json').read_text());c6=json.loads((ROOT/'src/week06/code.json').read_text())
c5={k:v.replace('Week05Registration','Week06Validation') for k,v in c5.items()}
c5['final']=c5['final'].replace('第五週｜校園活動報名','第六週起跑｜校園活動報名').replace('<form method="post">','<form method="post" novalidate>').replace('資料尚未驗證，也尚未寫入資料庫。','本起跑畫面尚未完成驗證教學，也尚未寫入資料庫。')
rules=c6['handler'].replace('        if (!ModelState.IsValid)\n        {\n            return;\n        }\n','')
changes=['不修改：確認第五週起跑專案。','不修改：指出 Input 與四個屬性。','只改 Index.cshtml.cs：加入 DataAnnotations 規則；暫時沒有閘門。','只改 Index.cshtml.cs：在 Submitted = true 之前加 ModelState 閘門。','只改 Index.cshtml：加入錯誤位置與 novalidate。','不修改：沿用第 04 步，執行三路測試。','不修改：沿用第 04 步，測 20／21 與 100／101 字。','只改 Index.cshtml.cs：名稱上限與訊息暫改 15 字；測完恢復 20。']
expected=['合法資料可送出，摘要顯示「報名資料已收到」。尚未加入本週驗證。','Build 成功，行為與第 00 步相同；兩個類別位於同一檔案。','Build 成功，但 OnPost 仍直接設定成功旗標；即使後端已有驗證錯誤，也還可能顯示成功。這是刻意保留的中間步驟，不可當成完成版。','Build 成功。合法資料仍顯示第五週摘要；不合法資料不顯示摘要，但尚未加入欄位錯誤訊息。','空白送出顯示三個必填錯誤；Email=abc 顯示格式錯誤；合法資料顯示「報名資料驗證通過」。','按本頁測試表逐列測試；合法後再送 abc，成功摘要必須消失。','其他欄位合法：名稱 20 字通過、21 字拒絕；備註空白可通過，100 字通過、101 字拒絕。','15 字母通過、16 字母拒絕，訊息是「顯示名稱最多 15 字」。此版本供實驗；測完恢復第 06 步。']
with zipfile.ZipFile(ROOT/'downloads/Week05-03-complete.zip') as z:
 baseline={'/'.join(n.split('/')[1:]):z.read(n) for n in z.namelist() if not n.endswith('/')}
baseline={n.replace('Week05Registration','Week06Validation'):data.replace(b'Week05Registration',b'Week06Validation') for n,data in baseline.items()}
rows=[]
for i in range(8):
 handler=c5['handler'] if i<2 else rules if i==2 else c6['handler']
 if i==7:handler=handler.replace('StringLength(20, ErrorMessage = "顯示名稱最多 20 字")','StringLength(15, ErrorMessage = "顯示名稱最多 15 字")')
 form=c5['final'] if i<4 else c6['form']
 handler='\n'.join(line.rstrip() for line in handler.splitlines())+'\n'
 name=f'Week06-step{i:02d}.zip';folder=f'Week06-Step{i:02d}'
 files={**baseline,'Pages/Index.cshtml.cs':handler.encode(),'Pages/Index.cshtml':form.encode(),'README.txt':f'第六週第 {i:02d} 步\n修改：{changes[i]}\n預期：{expected[i]}\n全部解壓縮到獨立資料夾，開啟 Week06Validation.csproj。\n需要 .NET 10 SDK。先停止其他練習網站，再 Build、Ctrl+F5。\n未使用資料庫。請勿合併不同步驟，備份放在專案外。\n'.encode()}
 with zipfile.ZipFile(ROOT/'downloads'/name,'w',zipfile.ZIP_DEFLATED) as z:
  for n,data in sorted(files.items()):z.writestr(folder+'/'+n,data)
 rows.append(dict(change=changes[i],expected=expected[i],handler=handler,form=form,zip=name))
(ROOT/'src/week06/checkpoints.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Generated 8 complete checkpoints')

# Public entry and finished packages use the same Week06 identity as all checkpoints.
for step,name in [(0,'Week06-starter.zip'),(4,'Week06-complete.zip')]:
 with zipfile.ZipFile(ROOT/'downloads'/f'Week06-step{step:02d}.zip') as source, zipfile.ZipFile(ROOT/'downloads'/name,'w',zipfile.ZIP_DEFLATED) as target:
  for item in source.namelist():
   target.writestr('Week06Validation/'+item.split('/',1)[1],source.read(item))
