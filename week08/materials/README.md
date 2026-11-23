# 第八週｜SQL Server 入門學生包（60–90 分鐘）

先開 start-here.html 或 Week08-SSMS-Student-Guide.pdf，按九步操作；需要已安裝 SQL Server Express 與 SSMS 的 Windows 電腦。

1. 連線到自己的 SQL Server。在左側右鍵 Databases → New Database，Database name 填 CampusActivityLab08；其餘預設，按 OK，Refresh 後看到資料庫。
2. 資料庫已存在就沿用，不刪除重建。之後右鍵伺服器 → New Query，選 CampusActivityLab08，執行指南中的 DB_NAME() 核對目的地。
3. 步驟 5／簡報第 10 頁：01-create-table.sql，第一次建立 dbo.Registrations；已有表則核對欄位，不重建。
4. 步驟 7／第 12 頁：02-insert.sql，新增小安／上午場，只執行一次。
5. 步驟 8、9／第 13、15 頁：03-select.sql，查詢可重跑；不再跑 INSERT。
6. 90 分鐘選做：04-optional-filter.sql 的 A 段（含 USE／GO）只跑一次，再只選 B 段做篩選排序。

開 SQL 檔：完整解壓後，在 SSMS 用 File → Open → File 開啟 .sql；確認同一伺服器和資料庫。未反白時 F5 執行整頁，有反白時只執行選取部分。網頁 SQL 與檔案擇一執行，尤其 INSERT 不要重複跑。

00-create-database.sql：教師指示下的 SQL 建庫備援，主課已用介面建好就不執行。
01-setup.sql：教師指示下的建庫／建表備援；可重跑且不清資料，但不會修復舊表欄位。主課不必額外執行。
兩份備援都不能解決缺少建立權限的問題，遇到權限錯誤先請教師協助。

資料庫 CampusActivityLab08；表 dbo.Registrations；三欄 Id／DisplayName／Session。不要在 master 建表。不要求 EF Core 或 Migration。
圖片在 images/，保留解壓後結構可離線看圖。建庫圖為 AI 製作的介面示意，其餘五張課程示意依官方截圖調整，均非實機重拍；來源見 screenshot-sources.html。圖片上的資料庫名稱與教材一致。
課堂只用假資料，使用 acceptance.txt 記錄驗收。回網站、重新下載及官方參考需要網路。
