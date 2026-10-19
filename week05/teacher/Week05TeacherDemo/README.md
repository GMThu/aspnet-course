# Week 05 教師完整專案｜讓表單真的收到資料

本專案只示範第五週接收路線：

```text
Browser → POST → Model Binding → OnPost → Razor
```

## 開啟方式

1. 以 Visual Studio 2026 開啟 `Week05TeacherDemo.csproj`。
2. 按 `Ctrl + F5`。
3. 用兩組不同假資料送出，確認成功摘要跟著改變。

也可在專案資料夾執行：

```bash
dotnet restore
dotnet run
```

## 教學檔案

- `Pages/Index.cshtml`：form、`asp-for` 與成功摘要。
- `Pages/Index.cshtml.cs`：`RegistrationInput`、`[BindProperty]`、`OnPost()`。
- `wwwroot/css/site.css`：桌機與手機版面。

## 本週驗收

1. localhost 可以停止後再次啟動。
2. 輸入「小安」時，摘要顯示小安。
3. 換另一名稱後，摘要同步改變。
4. 能沿著 form → `asp-for` → `[BindProperty]` → `OnPost()` → Razor 說明資料。

## 教學界線

- 尚未加入 DataAnnotations 與 `ModelState` 驗證。
- 尚未寫入資料庫。
- 第六週才處理空白、錯誤 Email 與邊界測試。
- 課堂只使用假資料。
