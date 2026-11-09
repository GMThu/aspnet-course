# 第五、六週圖文實作手冊來源

這是 GitHub Pages 靜態版，沿用已完成的 React 教材；不依賴 Sites 登入或伺服器。

```sh
cd practice-source
npm ci
npm run build
```

將來源與產生的 `../practice/` 一起提交。第五週網址為 `/aspnet-course/practice/`，第六週為 `/aspnet-course/practice/week06/`。下載包在 `downloads/`；替換教材碼時同步更新 `src/code.json` 與 `src/week06/code.json`。

所有圖示均為教學示意，非 Windows 實機截圖。專案以 .NET 10 在 macOS 通過編譯與表單流程測試；學校 Windows 操作介面尚待實機核對。進度只儲存在目前瀏覽器，沒有帳號、資料庫或學生資料上傳。

## 初學者逐步驗收

在已安裝 .NET 10 SDK 的環境執行 `python3 tools/verify_walkthrough.py`。也可用 DOTNET 環境變數指定 dotnet 執行檔。腳本從乾淨的 `dotnet new webapp` 建立六個實作檢查點，每一步建置，測試兩週的真實 POST，再由這些檢查點重建 ZIP（包含學生 README.txt）。最後執行 `npm run build` 更新公開產物。

`walkthrough-verification.txt` 記錄最近一次程式流程驗收。這不能代替學校 Windows Visual Studio 實機操作驗收。

## 第六週逐步完整程式碼

`python3 tools/build_week06_checkpoints.py` 產生第 00–07 步 JSON 與完整專案 ZIP，接著執行 `npm run build`。每步提供完整後端、完整 Razor 畫面與預期結果。第 02 步刻意沒有閘門，第 07 步為 15 字實驗版。

驗證：`DOTNET=/path/to/dotnet python3 tools/verify_week06_checkpoints.py`。測試每個 ZIP 建置及合法、空白、錯誤 Email、長度邊界 POST。

第六週獨立起跑包：`Week06-starter.zip`，專案檔與 namespace 統一為 `Week06Validation`。第 00–07 步與完成包使用同一名稱；第五週原始下載包維持原名。已有舊版第六週資料者，請下載新包到獨立資料夾再依本版完整程式碼練習。

## 學生流程複查

從公開 Week06-starter.zip 起跑，核對第 00–07 步。修正：起跑畫面使用第六週標題；起跑 form 預先加入 novalidate，避免第 02 步 Email 標註觸發瀏覽器攔截；HTTP 指令改用 --launch-profile http，以保留開發環境與靜態資源設定。

verify_week06_checkpoints.py 現在在同一份起跑專案依序只修改講義指定檔案，檢查八步建置、CSS HTTP 回應與 72 次連續 POST，涵蓋空白、Email、名稱邊界、備註 100/101 字，以及成功後再次失敗。另以瀏覽器核對起跑、第 02/03 步、欄位錯誤、修正成功與邊界畫面。驗證環境為 macOS/.NET 10，未執行 Windows Visual Studio 介面。

## 逐行說明

`npm run build` 會先執行 `tools/build_week06_explanations.py`，從目前 checkpoints.json 產生 explanations.json。每一行（含空行、括號、結束標籤）都有對應解說；遇到未涵蓋的新程式行會停止建置，避免解說與程式版本脫節。學生第 01 步直接顯示 Input Model 與 BindProperty 解說；各步完整程式碼區另有後端與 HTML/Razor 全檔逐行說明。複製按鈕仍只複製原本可執行程式。

第五週也有逐行解說：`tools/build_week05_explanations.py` 從 code.json 產生純 HTML（42 行）、C# 後端（28 行）、完成 Razor（60 行）的說明。兩週共用 code_line_explanations.py 與 LineNotes 顯示元件；第五週保留接收資料、不驗證與不存入資料庫的教學階段。另補 [BindProperty]／SupportsGet／get-set 對照及 Input、Submitted、OnPost 如何配合畫面。建置時檢查每行說明是否齊全。
