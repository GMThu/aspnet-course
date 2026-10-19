# 第五週｜讓表單真的收到資料

## 本週只完成一件事

從零建立或沿用 Razor Pages 專案，讓瀏覽器表單經過 POST、Model Binding、OnPost，最後在 Razor 顯示成功摘要。

> 本週不加入驗證、不接資料庫。空白或格式錯誤仍可能被收到；第六週才處理「收到不等於接受」。

## 從哪裡開始

1. 沒有專案：先讀 `START-HERE.md`。
2. 已有專案：確認 localhost 能停止後再次啟動。
3. 備份目前的 `Pages/Index.cshtml`、`Pages/Index.cshtml.cs`、`wwwroot/css/site.css`。
4. 解壓縮整個學生包，不要直接在 ZIP 內編輯。
5. 全程只使用課堂假資料。

## 練習一｜建立可編譯表單

1. 使用 `Index-form-week05-starter.txt` 替換首頁內容區。
2. 把 `site-week05-starter.css` 追加到 `wwwroot/css/site.css`。
3. 確認專案仍可編譯、Tab 可操作、label 可對焦、390px 無整頁水平捲動。

此階段使用純 HTML 的 `name="Input.*"` 預留後端地址，不引用尚未建立的 C# 屬性。

## 練習二｜讓後端收到

1. 把 `RegistrationInput-and-handler.txt` 的成員放進既有 `IndexModel`。
2. 把純 HTML 欄位改成 `asp-for="Input.*"`。
3. 加入 `Index-result-week05.txt` 的成功摘要。
4. 用兩組不同假資料確認摘要跟著改變。

## 最終驗收

- [ ] 專案停止後能再次啟動。
- [ ] 表單階段與接後端後都沒有 Build error。
- [ ] 兩組不同假資料都能出現在成功摘要。
- [ ] 能說出：瀏覽器 → POST → Binding → OnPost → Razor。
- [ ] 能說明「後端收到」不等於「資料已驗證或保存」。
