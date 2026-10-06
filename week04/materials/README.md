# 第四週｜CSS × Bootstrap 網站改造大作戰

## 今天的任務

延續第三週的小安活動網站：先看懂最少量 CSS，再使用 ASP.NET 範本已載入的 Bootstrap，並學會用 AI 提出小步修改、解釋原因與驗證結果，把內容改造成好看、好讀、可操作的活動宣傳頁。

## 先看預期成品 Demo

開啟 `demo-complete.html`，先看桌機版，再按上方的「390px 手機版」。這是**預期完成樣式**，不是起始檔：配色可以不同，也不必做得一模一樣，但最後要符合六項條件：

1. 有自己的主色，標題與內文仍清楚可讀。
2. 活動內容放進卡片，段落有適當間距。
3. 圖片不超出卡片，並有具體 `alt`。
4. 按鈕看得出可以點，而且連結真的可操作。
5. 至少有兩項自己能說明的 CSS 個人化修改。
6. 切到 390px 時不出現橫向捲動。

請從起始檔逐步完成，**不要用 Demo 覆蓋 `Index.cshtml`、`site.css` 或備用練習檔**。

## ASP.NET 主線

1. 啟動第三週的 ASP.NET 專案，先確認首頁仍能正常顯示。
2. 打開 `Pages/Shared/_Layout.cshtml`，尋找 `bootstrap.min.css`。
3. 確認 `wwwroot/lib/bootstrap/` 資料夾存在；找不到時先請老師確認，不要自行貼陌生 CDN。
4. 備份原本的 `Pages/Index.cshtml` 與 `wwwroot/css/site.css`。
5. 保留 `Index.cshtml` 頂端的 `@page`、`@model` 與 `@{ ... }`。
6. 將 `Index-body-week04-starter.txt` 的內容貼到首頁內容區，不要修改 `Index.cshtml.cs`。
7. 將 `images/campus-night.svg` 複製到專案的 `wwwroot/images/`。
8. 把 `site-week04-starter.css` 的內容加到既有 `wwwroot/css/site.css` 最後方。
9. 每完成一關都要儲存、重新整理、實際操作。

## 純 HTML 備用路線

如果 ASP.NET 專案暫時無法啟動：

1. 完整解壓縮學生包，不要直接在 ZIP 裡編輯。
2. 開啟 `week04-fallback.html`。
3. 它會載入學生包內的 `bootstrap-practice.css`，只模擬本週用到的少量 class。
4. 圖片路徑使用 `images/campus-night.svg`，前面沒有 `/`。
5. 備用版只用於練習 HTML／CSS，不代表 ASP.NET 已啟動；之後仍要補做 localhost 驗收。

## 五關

1. **看懂 CSS**：指出一條規則的選擇器、屬性和值。
2. **網站換氣氛**：自訂背景與文字顏色，文字仍清楚。
3. **找到 Bootstrap**：在 `_Layout.cshtml` 確認載入位置。
4. **完成活動卡**：使用 `card`、`card-body`、`img-fluid`、`btn` 等 class。
5. **AI 輔助個人化**：用完整提示詞取得建議，只採用自己能解釋且已實測的一項修改。

## AI 提示詞與驗證

打開 `AI-prompt-cheatsheet.md`。每次提供：背景、目標、最小相關程式碼、限制、輸出格式、驗收條件。

AI 的回覆只是候選方案。必須逐行閱讀、比較差異、在 localhost 執行、測試 390px 與連結操作；失敗時描述實際現象再追問。不得貼上帳密、連線字串、API key、真實個資或整個專案。

## 最終 Boss

老師會臨時指定一項小修改。你需要：

1. 找到修改位置。
2. 完成修改並儲存。
3. 回瀏覽器重新整理與操作。
4. 說明改了哪個 class 或 CSS 屬性。

## 不要做

- 不要覆蓋 `@page`、`@model`。
- 不要修改 `Index.cshtml.cs`。
- 不要把完整 `<html><head><body>` 貼進 Razor 首頁。
- 不要直接修改 `bootstrap.min.css`；自己的樣式寫在 `site.css`。
- 不要上傳 `bin/`、`obj/`、帳密、連線字串或真實個資。
- 不要只對 AI 說「幫我變漂亮」，也不要要求它重寫整頁。
- 不要因為 AI 說「完成」就停止；執行結果才是證據。
