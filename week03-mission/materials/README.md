# 第三週任務闖關版｜學生練習包

## 任務
在活動開始前，修好小安的活動網站。完成五關，再接受老師指定的一項臨時修改。

## ASP.NET 主線
1. 先把 `Pages/Index.cshtml` 複製到專案外備份。
2. 保留頂端的 `@page`、`@model` 與 `@{ ... }`，不要修改 `Index.cshtml.cs`。
3. 只用 `Index-body-mission-starter.txt` 替換原本顯示 Welcome 的內容區。
4. 將 `images/campus-walk.svg` 複製到專案的 `wwwroot/images/`。
5. 圖片路徑使用 `/images/campus-walk.svg`。
6. 每完成一關就儲存、重新整理、實際操作。

## 純 HTML 備用路線
1. 完整解壓縮，不要直接在 ZIP 內編輯。
2. 編輯 `mission-starter.html`，使用瀏覽器查看結果。
3. 圖片路徑使用 `images/campus-walk.svg`，前面沒有 `/`。
4. 純 HTML 路線不會執行 ASP.NET；之後仍需補做 ASP.NET 啟動驗收。

## 五關
- 第一關：自己的活動名稱，一個 `h1`。
- 第二關：至少一個 `h2`、兩段自己的 `p`。
- 第三關：`ul` 中至少三個 `li`，其中一項由自己新增。
- 第四關：修正 `herf`，讓 `href` 連結真的能開啟。
- 第五關：修正圖片檔名 `campus_walk.svg` → `campus-walk.svg`，並補上有意義的 `alt`。

## 最終 Boss
老師會臨時指定一項小修改。學生須當場完成，並說明改了哪個標籤或屬性。完成五關與最終任務，驗收後即可下課。

## 不要做
- 不要覆蓋 `@page`、`@model`。
- 不要把另一份完整的 `<html><head><body>` 貼進 Razor 首頁。
- 不要提交 `bin/`、`obj/`、帳密、連線字串或真實個資。
- AI 可以提示單一錯誤，但不要要求它重寫整頁。
