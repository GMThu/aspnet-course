# 第7週教師授課小抄｜讓通過驗證的資料留下來

## 課程定位
延續第五週 POST/PageModel 與第六週 Input Model/DataAnnotations/ModelState，第一次加入 EF Core 與 SQL Server。主線只有一條：**合法資料 → Entity → DbContext → SaveChanges → Query → 重啟後仍可查到**。

## 課前準備
- 教師機先確認 SQL Server Express、SSMS、.NET 10 與 EF Core 10.0.14 套件可用。
- 用教師專案先跑完 Migration、合法保存與重啟查詢；不要在課堂第一次嘗試。
- 投影只使用課堂假資料。列表刻意不顯示 Email 與 Note。
- 開啟 `materials/demo-complete.html`，切換桌機／390px，先說明六項完成條件；提醒這只是視覺模擬，不能取代 localhost＋SSMS。

## 三節課建議節奏
### 第一節｜資料形狀（50 分）
- 第 1–6 頁：從「成功訊息會消失」建立持久化問題，12 分。
- 第 7–8 頁：Entity、DbContext 逐段示範，10 分。
- 第 9 頁：實作 15 分。
- 第 10 頁：兩人互指類別、主鍵、DbSet，8 分；保留 5 分換場。

### 第二節｜建立資料表（50 分）
- 第 11–15 頁：服務註冊、連線字串、Migration、SSMS，18 分。
- 第 16 頁：實作 20 分。
- 第 17 頁：四站排錯與收束，7 分；保留 5 分換場。

### 第三節｜保存與讀回（50 分）
- 第 18–21 頁：驗證閘門、Mapping、Save、Query，18 分。
- 第 22 頁：實作 20 分。
- 第 23 頁：Final Boss 四情境，8 分。
- 第 24 頁：口頭收束，4 分。

## 一頁一觀點地圖
| 頁 | 觀點／教師動作 |
|---|---|
| 1 | 本週任務：通過驗證才保存 |
| 2 | 成功摘要不是持久化 |
| 3 | 三節課只完成 Create＋Read |
| 4 | 八站資料旅程；逐站點按 |
| 5 | 變數、PageModel、資料庫的壽命 |
| 6 | Input Model 與 Entity 各有工作 |
| 7 | Registration 對應一列；Id 與 CreatedAt |
| 8 | DbContext 是程式窗口，不是資料庫本身 |
| 9 | 實作 00：Entity＋Context，15 分 |
| 10 | 指出一列、主鍵、操作入口 |
| 11 | Program 註冊 DbContext |
| 12 | 連線字串只描述目的地；不放秘密 |
| 13 | Migration 是結構計畫，不是資料 |
| 14 | Add-Migration 與 Update-Database 分開 |
| 15 | SSMS 查資料表結構 |
| 16 | 實作 01：連線＋Migration＋SSMS，20 分 |
| 17 | 套件／Context／連線／Migration 四站排錯 |
| 18 | ModelState 失敗不可寫入，且要重新載入列表 |
| 19 | 明確把 Input 對映到 Entity |
| 20 | Add 追蹤、SaveChanges 寫入、Redirect 防重送 |
| 21 | GET 查最近 10 筆，列表不顯示敏感欄位 |
| 22 | 實作 02：失敗不增、成功一筆、重啟仍在，20 分 |
| 23 | Final Boss 用資料列數與畫面證據定位 |
| 24 | 完成與邊界；下一週再操作指定 Id |

## 三次實作巡視
### 第 9 頁
- 第 5 分鐘：確認學生不是拿 `RegistrationInput` 直接當 Entity。
- 第 8 分鐘：仍卡住者先只完成 `Registration`。
- 快學生：畫出 Entity → DbSet → Table，而不是加入更多欄位。

### 第 16 頁
- 先問「目前錯在哪一站」，不要讓學生同時重裝套件、改連線、刪 Migration。
- 若 `Update-Database` 成功，仍要到 SSMS 看到 DB、Table、欄位。
- 若執行個體不是 `SQLEXPRESS`，使用學生自己的 SSMS 連線名稱；不要全班盲貼同一字串。

### 第 22 頁
- 先測錯誤 Email，記錄資料列數不增加。
- 再測一筆合法假資料，確認只增加一筆。
- 最後停止網站再啟動，不能省略重啟證據。
- 快學生只測重新整理不重送；不要提早進入完整 CRUD。

## 統一驗收
1. **失敗路線**：空白、Email=abc 不新增。
2. **成功路線**：合法假資料只新增一筆。
3. **一致性**：Razor 列表與 SSMS 同一筆資料一致。
4. **持久性**：網站停止再啟動後仍查到。
5. **防重送**：成功後重新整理不重複新增。
6. **說明**：學生能指出 Entity、DbContext、ModelState、SaveChanges、Query。

## 本週邊界
- 只做 Create＋Read。
- 不教完整 CRUD、關聯、Repository Pattern、登入權限、正式部署與 Production secrets。
- Connection String 範例只供本機 Windows 驗證；真實帳密不得進 Git。
- 完成以學生 localhost、SQL Server、SSMS 三處實證為準；Demo、source code 或口頭說「成功」都不算。
