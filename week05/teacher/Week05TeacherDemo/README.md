# Week 05 教師完整專案｜Razor Pages 表單資料流

這是第五週教師示範與備課用的完整 ASP.NET Core Razor Pages 專案，目標框架為 **.NET 10 LTS**。內容對應課堂的同一條資料路線：

```text
Browser → POST → Model Binding → Validation → Razor Page
```

## 開啟方式

### Visual Studio 2026

1. 解壓縮 ZIP。
2. 在 Visual Studio 選「開啟專案或方案」。
3. 開啟 `Week05TeacherDemo.csproj`。
4. 按 `Ctrl + F5`。
5. 瀏覽器應開啟 `http://localhost:5085`；若 Visual Studio 使用不同 port，以實際網址為準。

### 終端機

```bash
dotnet restore
dotnet run
```

## 教學檔案地圖

- `Pages/Index.cshtml`：form、`asp-for`、欄位錯誤與成功摘要。
- `Pages/Index.cshtml.cs`：`[BindProperty]`、`OnPost()`、DataAnnotations、`ModelState.IsValid`。
- `wwwroot/css/site.css`：桌機與手機版面。
- `README.html`：可直接雙擊閱讀的網頁版操作說明。
- `preview.html`：不需啟動 ASP.NET 就能先看的靜態畫面預覽；真正功能仍以 localhost 為準。
- `Program.cs`：註冊並啟用 Razor Pages。

## 建議示範順序

1. 先跑 GET：指出 `OnGet()` 與空白表單。
2. 空白送出：停在 `OnPost()`，觀察 `ModelState.IsValid == false`。
3. Email 輸入 `abc`：指出 `[EmailAddress]` 產生錯誤。
4. 合法假資料：觀察 `Input` 已由 Model Binding 填入，然後顯示摘要。
5. 重新啟動網站：說明上一筆資料無法查回，因為本週尚未接資料庫。

## 必測三條路

| 輸入 | 預期結果 |
|---|---|
| 必填欄全空 | 三個欄位錯誤；不顯示成功摘要 |
| 名稱「小安」、Email `abc`、場次「週三晚上」 | 顯示「Email 格式不正確」 |
| 名稱「小安」、Email `student@example.com`、場次「週三晚上」 | 顯示內容一致的成功摘要 |

## 教學提醒

- form 加上 `novalidate` 是為了示範**後端**驗證，不讓瀏覽器原生提示先攔截。
- Razor Form Tag Helper 會自動產生防偽 token。
- 這份專案只接收、驗證並回應資料，**不會保存資料**。
- 課堂只使用假資料，不輸入真實個資或任何秘密。
