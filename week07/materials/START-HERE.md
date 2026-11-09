# 第七週 START HERE｜讓通過驗證的資料留下來

## 今天的唯一主線
延續第六週的小安活動報名專案，使用 EF Core 與 SQL Server 完成：

`合法表單 → Entity → DbContext → SQL Server → Query → Razor 列表`

## 開始前
1. 先執行第六週專案。
2. 用空白、`Email = abc`、合法假資料重跑驗證。
3. 確認合法資料只顯示摘要，停止網站後不會保存。
4. 全程只用課堂假資料，不輸入真實姓名、Email 或帳密。

## 三輪任務
1. 建立 `Registration` Entity 與 `CampusActivityContext`。
2. 設定 SQL Server、建立 Migration、用 SSMS 看到資料表。
3. 合法資料才 `SaveChangesAsync`，再從資料庫查回列表。

## 完成條件
- 空白與錯誤 Email 不增加資料列。
- 合法假資料只增加一筆。
- 頁面列表與 SSMS 查詢內容一致。
- 停止網站再啟動，該筆仍能查到。
- 重新整理成功頁不會重送同一筆 POST。

本週只做 Create＋Read；編輯、刪除、登入權限與正式部署不在本週範圍。
