USE CampusActivityLab08;
GO
-- 90 分鐘選做：每個 INSERT 各執行一次；只用假資料。
INSERT INTO dbo.Registrations (DisplayName, Session)
VALUES (N'小晴', N'下午場');
INSERT INTO dbo.Registrations (DisplayName, Session)
VALUES (N'小宇', N'上午場');

-- 只選取下面 SELECT 執行，避免重送上方 INSERT。
SELECT Id, DisplayName, Session
FROM dbo.Registrations
WHERE Session = N'上午場'
ORDER BY Id DESC;
