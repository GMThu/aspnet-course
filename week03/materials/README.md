# 第三週學生練習包

## 主線：沿用 CampusActivity 的 Razor Pages 專案
1. 在改動前複製備份 Pages/Index.cshtml 到專案以外的位置。
2. 打開 Pages/Index.cshtml。保留頂端 @page、@model 與 @{ ... } 設定區塊。
3. 只把原本顯示 Welcome／介紹文字的 `<div class="text-center">...</div>` 替換成 Index-body-starter.txt 的內容。不改 PageModel、不改 _Layout.cshtml。
4. 按每頁講義逐步擴充，不一次貼完整參考答案。
5. 複製 images/campus-walk.svg 到專案 wwwroot/images/；若 images 不存在可建立。HTML 使用 /images/campus-walk.svg。
6. 儲存後啟動／重新啟動專案，查看自己的 localhost 網址。

## 備用：環境尚未完成的同學
1. 完整解壓縮練習包，不要只從 ZIP 中直接開啟檔案。
2. 用 Visual Studio「開啟 > 檔案」或 Windows 記事本開啟 activity-starter.html；瀏覽器則用來看結果。
3. 不要改成 .html.txt。使用 UTF-8 儲存；檔案總管可開啟副檔名顯示。
4. 把圖片路徑寫成 images/campus-walk.svg（前面沒有 /）。保持 HTML 與 images 資料夾相鄰。
5. 修改、存檔、瀏覽器重新整理。純 HTML 不會執行 ASP.NET 或 Razor。

## 必做任務
- 一個活動主標題、活動介紹與集合資訊。
- 一份至少三項的攜帶物品清單。
- 一張可顯示、具適當 alt 的示意圖。
- 一個能點到正確目的地的連結。
- 用兩個以上有主題的 section 組織內容，搭配 h2。
- 現場獨立新增一個清單項目，並說明對應標籤。

## 交付
依老師指定平台提交原始檔與必要圖片、瀏覽器截圖、三項修改說明、一個排錯紀錄、AI 使用說明（未使用也可註明）。不要交 bin/obj、帳密、真實個資或整個開發環境。
ASP.NET 路線交 Index.cshtml、wwwroot/images/ 中使用的圖片；純 HTML 路線交 HTML 與 images/，註明尚待補 ASP.NET 啟動驗收。
檢核表只是自評，下載紀錄不等於繳交作業。

## 圖片
campus-walk.svg 是本教材製作的課堂路線示意圖，不是真實東海校園地圖，可用於本課練習。
