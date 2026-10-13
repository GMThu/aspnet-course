# 第五週｜讓表單真的收到資料

## 今天的任務

延續第四週的活動宣傳頁，加入一個真正會 POST 到 Razor Page 的報名表。完成後，錯誤資料會停在表單並顯示原因，合法資料會顯示報名摘要。

> 本週只完成「接收與驗證」。資料尚未寫入資料庫，請勿宣稱已保存報名紀錄。

## 使用前

1. 啟動第四週的 ASP.NET Razor Pages 專案。
2. 確認首頁仍能在 localhost 顯示。
3. 備份 `Pages/Index.cshtml`、`Pages/Index.cshtml.cs`、`wwwroot/css/site.css`。
4. 解壓縮整個學生包，不要直接在 ZIP 內編輯。
5. 使用課堂假資料，不輸入真實 Email、電話、密碼、連線字串或 API key。

## 檔案用途

- `Index-body-week05-starter.txt`：放進 `Pages/Index.cshtml` 的內容區；保留原本 `@page`、`@model`。
- `RegistrationInput-and-handler.txt`：參考後貼入既有的 `IndexModel` 類別內；不要覆蓋自己的 namespace。
- `site-week05-starter.css`：加到既有 `wwwroot/css/site.css` 最後方。
- `AI-debug-prompt.md`：表單除錯時的最小提問模板。
- `demo-complete.html`：預期行為 Demo，可切換成功／失敗情境；它不是 ASP.NET，也不能取代學生專案。

## 三輪實作

### 練習一｜建立表單畫面

- 加入 form、名稱、Email、場次、備註與送出按鈕。
- 每個欄位都有 label 與 `asp-for`。
- Tab 可依序操作；390px 不出現水平捲動。

### 練習二｜讓後端收到

- 建立 `RegistrationInput`。
- 加入 `[BindProperty]`、`OnPost()` 與 `Submitted`。
- 用兩組不同假資料確認成功摘要會跟著改變。

### 練習三｜加入驗證

- 名稱：必填，最多 20 字。
- Email：必填，格式正確。
- 場次：必選。
- 先檢查 `ModelState.IsValid`，通過後才顯示成功摘要。

## 必測三條路

1. 所有必填欄空白：顯示錯誤，不顯示成功摘要。
2. Email 輸入 `abc`：顯示格式錯誤。
3. 使用合法假資料：顯示內容一致的成功摘要。

## 卡住時依序檢查

1. `form` 是否真的使用 `method="post"`。
2. 欄位與按鈕是否都在 form 裡。
3. `asp-for` 是否對到正確的 `Input` 屬性。
4. `Input` 是否有 `[BindProperty]`。
5. `OnPost()` 是否存在。
6. 是否先檢查 `ModelState.IsValid`。
7. Razor 成功區是否讀取正確屬性。

完成不是「AI 說可以」，而是自己的 localhost 實際通過三條測試，並能說明資料經過：瀏覽器 → POST → Binding → Validation → Razor Page。
