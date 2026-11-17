# 第八週｜SQL Server 入門學生包（60–90 分鐘）

先讀含課程介面圖解與九個小步驟的 start-here.html，使用已安裝 SQL Server Express 與 SSMS 的 Windows 電腦。
本週練習資料庫 CampusActivityLab08；不要在 master 建表。

1. 00-create-database.sql：第一次建庫；01-create-table.sql：第一次建表。物件已存在就跳過。
   01-setup.sql：可重跑的建庫／建表備援，不刪既有資料。
2. 02-insert.sql：新增一筆小安。每次執行都會新增一筆，請只執行一次。
3. 03-select.sql：查詢，可重複執行。
4. 04-optional-filter.sql：90 分鐘選做。新增段各執行一次，之後只選查詢段執行。
5. acceptance.txt：完成證據。
6. demo-complete.html：瀏覽器結果示意，不連線 SQL Server，不能當作實機驗收。

60 分鐘只要求連線、認識表格、INSERT、SELECT 與關閉查詢分頁後再查。
90 分鐘再加 WHERE、ORDER BY 與個人練習。不要求 EF Core/Migration。

原 EF Core 完整教材移到 ../ef-core/，另需約 150 分鐘；使用另一個 CampusActivityDb 由 Migration 建表。
SQL 檔為 UTF-8；只用課堂假資料。官方參考：https://learn.microsoft.com/en-us/ssms/quickstarts/ssms-connect-query-sql-server

圖片在 images/，來源與版本差異見 screenshot-sources.html。解壓縮時保留資料夾結構，離線開啟 start-here.html 仍可看圖。圖片名稱與 SQL 一致：CampusActivityLab08／dbo.Registrations。六張圖片已調整為課程示意圖，並非實機重拍。
