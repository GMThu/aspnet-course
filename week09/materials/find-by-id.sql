-- 在 SSMS 執行；將 1 改成自己記下的 Id。
USE CampusActivityLab09;
GO
SELECT Id, DisplayName, Email, Session, Note
FROM dbo.Registrations
WHERE Id = 1;
