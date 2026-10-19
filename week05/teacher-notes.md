# 第五週教師授課小抄

## 課程定位

延續第四週的活動宣傳頁，第一次讓學生修改 `Index.cshtml.cs`，完成：

```text
瀏覽器填寫 → POST → Model Binding → Validation → Razor 顯示結果
```

本週不接資料庫、不做完整 CRUD。學生必須能明確說明「後端收到」不等於「資料已保存」。

## 完成後學生應能

1. 指出 `Index.cshtml` 與 `Index.cshtml.cs` 的分工。
2. 說明 `form method="post"`、`asp-for`、`[BindProperty]` 與 `OnPost()` 的關係。
3. 用 DataAnnotations 定義必填、格式與長度規則。
4. 以 `ModelState.IsValid` 阻止錯誤資料進入成功區。
5. 親自完成空白、錯誤 Email、合法資料三條測試。
6. 沿五站資料路線說明發生問題的位置。
7. 在需要時指出 Razor Pages 專案中畫面、C# 處理與 CSS 的位置。

## 上課前（約 5 分鐘）

### 教師完整 ASP.NET 專案

教師包另附 `teacher/Week05-Teacher-Project.zip`，解壓後以 Visual Studio 2026 開啟 `Week05TeacherDemo.csproj`，即可直接執行完整 Razor Pages 範例。專案內含：

- `Pages/Index.cshtml`：真正的 ASP.NET 表單畫面。
- `Pages/Index.cshtml.cs`：POST、Model Binding、DataAnnotations 與 ModelState。
- `wwwroot/css/site.css`：桌機與手機版面。
- `preview.html`：沒有 .NET SDK 時可先看的靜態畫面；它不能取代 localhost 驗證。
- `README.html`：Windows 解壓後可直接雙擊閱讀的網頁說明。
- `README.md`：同一份說明的 Markdown 原始檔。

上課建議先用完整專案示範一次，再讓學生從起始片段逐步完成，避免學生只複製完整答案。

1. 開啟第 2 頁的預期成品 Demo。
2. 依序按「測試空白」「測試錯誤 Email」「填入正確假資料」。
3. 切到 390px，確認沒有水平捲動。
4. 明確說明 Demo 是行為參考，不是 ASP.NET，也不能覆蓋學生專案。
5. 提醒只使用課堂假資料。

## 三節課建議節奏

### 第一節｜表單外觀與對應（約 50 分鐘）

- 第 1–4 頁，約 8 分鐘：故事、終點、任務地圖與五站資料旅程。
- 第 5 頁，3–5 分鐘：專案導航，只認「畫面、C#、CSS」，不背完整目錄。
- 第 6–9 頁，約 15 分鐘：GET／POST、form 範圍、label、asp-for。
- 第 10 頁，15 分鐘：練習一。
- 第 11 頁，5 分鐘：依三層檢查收束。

### 第二節｜PageModel 接收資料（約 50 分鐘）

- 第 12–14 頁，約 12 分鐘：PageModel、輸入模型、BindProperty。
- 第 15–17 頁，約 13 分鐘：OnPost、逐站追蹤、成功摘要與限制。
- 第 18 頁，20 分鐘：練習二。
- 第 19 頁，5 分鐘：沿資料路線除錯。

### 第三節｜驗證、測試與 Boss（約 50 分鐘）

- 第 20–23 頁，約 13 分鐘：收到不等於接受、DataAnnotations、ModelState、欄位錯誤。
- 第 24–25 頁，約 7 分鐘：三條測試與 AI 最小除錯提問。
- 第 26 頁，20 分鐘：練習三。
- 第 27 頁，5 分鐘：同儕測試。
- 第 28–29 頁，5 分鐘：依學生狀態指定 Boss 等級或記錄下次驗收；完成者收束。

Boss 無法在當節全部驗完時，優先驗收三條測試，不壓縮學生實作時間。Boss 可作為下次課程開場的個別檢核。

## 一頁一觀點頁面地圖

| 頁 | 觀點／教師動作 |
|---|---|
| 1 | 同一故事：活動頁要接上後端 |
| 2 | 終點是「錯的擋住、對的收到」 |
| 3 | 三節課只完成一條資料路線 |
| 4 | 五站資料旅程；逐步點擊 |
| 5 | 先認路：畫面、C#、CSS 在哪裡 |
| 6 | GET 是拿頁面；POST 是交資料 |
| 7 | form 是資料信封；先讓學生預測 |
| 8 | label 連起問題與操作位置 |
| 9 | asp-for 連起 Razor 欄位與 C# 屬性 |
| 10 | 練習一，15 分鐘 |
| 11 | 第一輪三層檢查 |
| 12 | cshtml 呈現；cshtml.cs 處理 |
| 13 | 同用途欄位收成 Input 模型 |
| 14 | BindProperty 接住 POST |
| 15 | POST 對應 OnPost |
| 16 | 逐站追蹤「小安」；逐步點擊 |
| 17 | 成功摘要能證明與不能證明的事 |
| 18 | 練習二，20 分鐘 |
| 19 | 依五站路線除錯 |
| 20 | 收到不等於應該接受 |
| 21 | 每個 Annotation 回答一個規則問題 |
| 22 | ModelState 是成功前的閘門 |
| 23 | 錯誤訊息要靠近欄位 |
| 24 | 空白、錯誤、成功三條都要測 |
| 25 | AI 只協助縮小問題 |
| 26 | 練習三，20 分鐘 |
| 27 | 同儕只回報現象，不替對方改 |
| 28 | 分級情境式 Boss |
| 29 | 收束並橋接清單與資料庫 |

## 開場專案導航（第 5 頁）

這頁放在主線前段，只用 3–5 分鐘。老師可以直接說：「先認路，不用背。今天只在三個地方移動。」

- `Pages/*.cshtml`：畫面、表單與顯示結果。
- `Pages/*.cshtml.cs`：PageModel、Input、OnPost 與驗證。
- `wwwroot/css/`：瀏覽器可取得的樣式。
- 其他檔案先知道存在；等未來真正使用 `Program.cs`、設定檔或 `.csproj` 時再介紹。

本頁完成條件：學生能指出「畫面、C# 處理、CSS」三處位置，並知道 `Index.cshtml` 與 `Index.cshtml.cs` 共同完成同一個 Razor Page。

## 常見問題與處理順序

### Razor 編譯失敗

1. 確認沒有加入第二組 `@page`、`@model`。
2. 確認 `RegistrationInput` 放在 `IndexModel` 類別內。
3. 確認有 `using System.ComponentModel.DataAnnotations;` 與 `using Microsoft.AspNetCore.Mvc;`。
4. 讀第一個編譯錯誤，不先處理後面連鎖錯誤。

### 按送出沒有進 OnPost

1. form 是否為 `method="post"`。
2. submit 是否位於 form 內。
3. Handler 是否命名為 `OnPost()`。
4. 先用中斷點或暫時可見狀態確認有無執行，不整頁重寫。

### Input 全是空值

1. `asp-for` 是否使用 `Input.DisplayName` 等完整路徑。
2. Input 是否標示 `[BindProperty]`。
3. Razor 與 C# 屬性拼字是否一致。

### 「請選擇場次」也能通過

預設 option 必須是 `value=""`。不要在 OnPost 硬寫顯示文字比對。

### 錯誤資料仍顯示成功

確認 `Submitted = true` 位於 `ModelState.IsValid` 通過之後。

### 學生說資料已經存好了

請他關閉並重新啟動專案，再問「從哪裡查回上一筆？」本週沒有資料庫，應描述為收到、驗證、回應，不是持久保存。

## 快慢分流

- **補強**：只保留名稱、Email、場次；完成 POST、兩項驗證與成功摘要。
- **一般主線**：四欄、三條測試、同儕回報與標準 Boss。
- **提早完成**：由老師指定進階 Boss，只做一題；不自行接資料庫或登入。

## Boss 使用方式

1. 先確認共同三條測試已通過。
2. 老師依狀態指定「基礎救援／標準任務／進階委託」。
3. 同級內才按抽題，避免難度由運氣決定。
4. 四項都要看到：重現、修改、測試、說明。
5. 詳細任務與備用口試見 `materials/teacher-final-boss.md`。

## 驗收用語

- `ad-hoc green`：只代表某次輸入與操作成功。
- 本週課堂驗收：三條測試、390px 可操作、localhost 實際執行、學生能沿五站解釋。
- 靜態 Demo 成功不等於 ASP.NET 成功。
- POST 成功不等於資料庫保存成功。
