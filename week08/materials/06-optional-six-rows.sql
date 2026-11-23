-- 課後複習／選用：整份只執行一次，預期影響 6 列。已跑過就不再執行。
USE CampusActivityLab08;
GO
INSERT INTO dbo.Registrations (DisplayName, Session)
VALUES (N'練習小美', N'上午場'),
       (N'練習小明', N'下午場'),
       (N'練習小華', N'上午場'),
       (N'練習小宇', N'下午場'),
       (N'練習小晴', N'上午場'),
       (N'練習小傑', N'下午場');
