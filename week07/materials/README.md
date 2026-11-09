# 第七週學生任務包｜EF Core × SQL Server

這個任務包延續第六週專案，不是可直接取代專案的完整答案。請依課堂順序，把片段加入自己的 Razor Pages 專案。

## 先看完成條件 Demo
開啟 `demo-complete.html`。它只模擬完成後應看見的行為與驗收條件，**不是資料庫，也不能取代 localhost 與 SSMS 證據**。

## 檔案用途
- `START-HERE.md`：本週主線與完成條件。
- `Registration-week07.cs`：Entity 參考片段。
- `CampusActivityContext-week07.cs`：DbContext 參考片段。
- `Program-and-appsettings-week07.txt`：套件、服務註冊與連線設定。
- `Index-save-and-query-week07.txt`：PageModel 保存與查詢片段。
- `Index-list-week07.txt`：Razor 成功訊息與最近報名列表。
- `AI-debug-prompt.md`：卡關時的最小提問模板。
- `demo-complete.html`：視覺與驗收參考。

## 重要安全界線
- 範例連線使用 Windows 驗證，不要把 SQL 密碼寫進檔案或提交到 Git。
- `Server=.\\SQLEXPRESS` 必須依自己的 SQL Server 執行個體調整。
- 不要刪除資料庫、修改他人資料或貼出真實個資。
- Migration 要先閱讀再套用；不要為了解錯直接刪除整個專案或資料庫。

## 套件版本
教材製作時（2026-11-09）以 .NET 10、EF Core `10.0.14` 與 `System.Security.Cryptography.Pkcs 10.0.14` 驗證版本一致性；後者明確覆寫有已知弱點的舊版相依。若老師指定不同修補版本，以老師課堂版本為準，套件請維持相容的修補版本。
