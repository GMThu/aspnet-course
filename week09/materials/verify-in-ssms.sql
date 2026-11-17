-- 本檔只查詢；請在 SSMS 執行，先確認資料庫名稱。
USE CampusActivityLab09;
GO
SELECT DB_NAME() AS CurrentDatabase;
SELECT COUNT(*) AS TotalCount FROM dbo.Registrations;
SELECT TOP (10) Id, DisplayName, Email, Session, Note
FROM dbo.Registrations
ORDER BY Id DESC;
