-- 課後複習／選用；有時間才教。只查既有資料，不新增假資料。
-- 整份可重跑，三個 SELECT 會各顯示一個結果表。
USE CampusActivityLab08;
GO
SELECT Id, DisplayName, Session
FROM dbo.Registrations;

SELECT Id, DisplayName, Session
FROM dbo.Registrations
WHERE Session = N'上午場';

SELECT Id, DisplayName, Session
FROM dbo.Registrations
WHERE Session = N'上午場'
ORDER BY Id DESC;
