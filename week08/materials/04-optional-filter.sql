-- 90 分鐘選做。不要整份重複執行；選取時包括該段的 USE 與 GO。
-- A 段開始：兩筆假資料只新增一次；已新增就跳過 A 段。
USE CampusActivityLab08;
GO
INSERT INTO dbo.Registrations (DisplayName, Session)
VALUES (N'小晴', N'下午場');
INSERT INTO dbo.Registrations (DisplayName, Session)
VALUES (N'小宇', N'上午場');
-- A 段結束

-- B 段開始：之後只選取本段執行，可重跑；不會新增資料。
USE CampusActivityLab08;
GO
SELECT Id, DisplayName, Session
FROM dbo.Registrations
WHERE Session = N'上午場'
ORDER BY Id DESC;
-- B 段結束
