-- 課後複習／選用：只查詢，可重跑。六筆練習會使下午場比原本多 3 筆。
USE CampusActivityLab08;
GO
SELECT Id, DisplayName, Session
FROM dbo.Registrations
WHERE Session = N'下午場'
ORDER BY Id DESC;
