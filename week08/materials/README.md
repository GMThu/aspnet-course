# 第八週｜SQL Server 入門學生包（60–90 分鐘）

先讀 start-here.html，使用已安裝 SQL Server Express 與 SSMS 的 Windows 電腦。
本週練習資料庫 CampusActivityLab08；不要在 master 建表。

1. 01-setup.sql：建庫、建表。可重跑，不刪既有資料。
2. 02-insert.sql：新增一筆小安。每次執行都會新增一筆，請只執行一次。
3. 03-select.sql：查詢，可重複執行。
4. 04-optional-filter.sql：90 分鐘選做。新增段各執行一次，之後只選查詢段執行。
5. acceptance.txt：完成證據。
6. demo-complete.html：瀏覽器結果示意，不連線 SQL Server，不能當作實機驗收。

60 分鐘只要求連線、認識表格、INSERT、SELECT 與關閉查詢分頁後再查。
90 分鐘再加 WHERE、ORDER BY 與個人練習。不要求 EF Core/Migration。

原 EF Core 完整教材移到 ../ef-core/，另需約 150 分鐘；使用另一個 CampusActivityDb 由 Migration 建表。
SQL 檔為 UTF-8；只用課堂假資料。官方參考：https://learn.microsoft.com/en-us/ssms/quickstarts/ssms-connect-query-sql-server
