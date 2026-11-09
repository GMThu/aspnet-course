# Week 07 教師 Final Boss｜保存路線排錯卡

## 使用方式
學生先重現，再指出卡在哪一站；只做最小修改，最後重跑同一組資料。不要把本卡放入學生 ZIP。

## A｜錯誤資料也新增
- 現象：`Email = abc` 後資料列數增加。
- 必查：`ModelState.IsValid` 是否在 Entity 建立與 `SaveChangesAsync` 之前。
- 必測：錯誤 Email 不增加；合法資料只增加一筆。
- 口試：為什麼資料庫有 NOT NULL 仍不能取代表單驗證？

## B｜畫面說成功，SSMS 沒資料
- 現象：成功提示出現，但查詢仍是 0 筆。
- 必查：`SaveChangesAsync` 是否真的執行，以及網站與 SSMS 是否連到同一個資料庫。
- 必測：新增前後資料列數差 1。
- 口試：`Add` 與 `SaveChangesAsync` 的工作有何不同？

## C｜SSMS 有資料，畫面沒有列表
- 現象：SQL 查得到，但 Razor 顯示空清單。
- 必查：`OnGetAsync`、`LoadRegistrationsAsync`、`Registrations` 屬性與 `foreach`。
- 必測：同一筆 Id／顯示名稱／場次在 SSMS 與畫面一致。
- 口試：Query 與 Razor 各負責哪一段？

## D｜重新整理又多一筆
- 現象：成功後按重新整理，資料列數再增加。
- 必查：成功後是否 `RedirectToPage()`，而不是 `return Page()`。
- 必測：合法送出增加一筆；重整後筆數不變。
- 口試：POST → Redirect → GET 為何能避免重送？

## 統一過關
1. 重現現象。
2. 說出目前卡住的站。
3. 只改必要範圍。
4. 用失敗、成功與重啟證據驗收。
