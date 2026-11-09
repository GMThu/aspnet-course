# 第七週｜AI 排錯提示詞

AI 只能協助縮小問題；Migration 成功、資料表存在與資料列增減，都要由你在自己的環境實際驗證。

```text
我正在 ASP.NET Core Razor Pages 專案中，使用 EF Core 10 與 SQL Server Express。

目標：讓通過 ModelState 的 RegistrationInput 保存成 Registration，並在 GET 查回最近 10 筆。

目前卡在這一站（只選一項）：
[套件 / DbContext / 連線字串 / Migration / SaveChanges / Query / Razor]

我剛執行的命令或操作：
【貼最小相關操作】

第一個完整錯誤訊息：
【先遮蔽帳號、路徑個資、密碼與連線秘密】

已確認的證據：
【例如：資料表存在，但資料列仍是 0】

限制：
1. 不刪除資料庫、不重建整個專案。
2. 不更換框架版本，不加入本週以外的架構。
3. 一次只提供一個檢查步驟，說明它要排除哪個原因。
4. 不宣稱已修好；最後列出我應實際重跑的驗收步驟。
```

收到建議後，依序：讀懂 → 比對差異 → 執行 → 用同一組資料重測 → 記錄證據。
