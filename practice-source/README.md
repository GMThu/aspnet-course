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
