-- 對應指南步驟 7；已貼上同一段 INSERT 成功，就不要再執行本檔。
USE CampusActivityLab08;
GO
-- 整份只執行一次；看 Messages 的影響 1 列，再開 03-select.sql 查詢。
INSERT INTO dbo.Registrations (DisplayName, Session)
VALUES (N'小安', N'上午場');
