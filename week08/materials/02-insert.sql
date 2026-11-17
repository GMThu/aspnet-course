USE CampusActivityLab08;
GO
-- 每執行一次 INSERT 就新增一筆；先查筆數，只執行一次。
INSERT INTO dbo.Registrations (DisplayName, Session)
VALUES (N'小安', N'上午場');

SELECT Id, DisplayName, Session
FROM dbo.Registrations
ORDER BY Id;
