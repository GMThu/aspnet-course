# Week 07 教師示範專案｜EF Core × SQL Server

## 用途
課前示範「驗證通過 → Entity → DbContext → SQL Server → Query → Razor」，以及五項統一驗收。此專案不是學生任務包。

## 環境
- .NET 10
- EF Core SQL Server／Design／Tools 10.0.14
- System.Security.Cryptography.Pkcs 10.0.14（明確覆寫有已知弱點的舊版相依）
- SQL Server Express（範例執行個體 `.\\SQLEXPRESS`）
- SSMS

## 課前執行
1. 以 Visual Studio 開啟 `Week07TeacherDemo.csproj`。
2. 確認 `appsettings.json` 的執行個體名稱與教師機一致。
3. 還原 NuGet 套件。
4. 在套件管理主控台執行：
   ```powershell
   Update-Database
   ```
5. 執行網站，用假資料完成驗收。

若要從頭示範 Migration，請複製一份專案再移除 `Migrations` 目錄；不要在唯一教師備份上刪除既有資料庫。

## 統一驗收
1. 空白與 `Email=abc`：顯示錯誤，資料列數不增加。
2. 合法假資料：只增加一筆。
3. Razor 列表與 SSMS 查詢內容一致。
4. 停止網站再啟動，該筆仍可查到。
5. 成功頁重新整理，不會重送同一筆 POST。

## SQL 查核
```sql
USE CampusActivityDb;
GO
SELECT TOP (10)
    Id, DisplayName, Email, Session, Note, CreatedAt
FROM dbo.Registrations
ORDER BY Id DESC;
```

## 安全界線
- 只用課堂假資料。
- 畫面列表刻意不顯示 Email 與 Note，避免投影暴露內容。
- 範例使用 Windows 驗證；真實部署的秘密應放環境設定或 Secret Manager，不進 Git。
- 本週只教 Create＋Read，不延伸完整 CRUD、權限或正式部署。

## 驗證限制
教材製作機沒有 .NET SDK 與 SQL Server，因此製作端只能做靜態結構／JSON／HTML／套件版本驗證；正式上課前必須在 Windows 教師機完成 `dotnet restore/build`、`Update-Database` 與上述五項 browser＋DB smoke test。
