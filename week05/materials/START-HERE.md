# 第五週 START HERE｜從零建立 Razor Pages 專案

本週完成：建立專案 → localhost → 可編譯表單 → POST → Binding → OnPost → 成功摘要。

## 0. 環境確認

- Visual Studio 2026 已安裝「ASP.NET 與網頁程式開發」。
- .NET 10 SDK 可用；`dotnet --version` 應以 `10.` 開頭。
- 任務包已完整解壓縮。
- 全程只使用課堂假資料。

## 1. Visual Studio 主要路線

1. 建立新的專案，搜尋 Razor。
2. 選 **ASP.NET Core Web App (Razor Pages)**。
3. 名稱輸入 `Week05Registration`。
4. Framework 選 **.NET 10.0 (LTS)**，Authentication 選 None。
5. 按 `Ctrl + F5`，看到 localhost。

## 2. 終端機備援

```bash
dotnet new webapp -n Week05Registration -f net10.0
cd Week05Registration
dotnet watch
```

## 3. 只認三個位置

```text
Pages/Index.cshtml       ← 畫面與表單
Pages/Index.cshtml.cs    ← PageModel、Input、OnPost
wwwroot/css/site.css     ← 樣式
```

## 4. 練習一：建立可編譯表單

1. 把 `Index-form-week05-starter.txt` 放進首頁內容區。
2. 把 `site-week05-starter.css` 追加到 `site.css`。
3. 保留原本 `@page`、`@model` 與 namespace。
4. 重新執行，確認沒有 Build error。

這一輪只用純 HTML 的 `for`／`id`／`name`；不先引用還不存在的 Input 屬性。

## 5. 練習二：讓後端收到

1. 把 `RegistrationInput-and-handler.txt` 的成員放進既有 `IndexModel`。
2. 把欄位換成 `asp-for="Input.DisplayName"` 等對應。
3. 加入 `Index-result-week05.txt` 的成功摘要。
4. 使用兩組不同假資料送出。

## 6. 完成條件

- [ ] localhost 可以停止後重啟。
- [ ] 表單階段與接後端後都能編譯。
- [ ] 兩組不同輸入會產生不同摘要。
- [ ] 能解釋瀏覽器 → POST → Binding → OnPost → Razor。
- [ ] 知道本週沒有驗證，也沒有資料庫。
