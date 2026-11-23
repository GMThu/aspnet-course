-- 只有一筆資料時，排序前後看起來會一樣，這是正常的。
-- 沒有下午場資料時，查詢下午場出現 0 列也是正常的，不代表操作錯誤。
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
