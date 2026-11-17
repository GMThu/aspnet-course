-- 第一次建表；已存在就跳過，改檢查 Columns。
USE CampusActivityLab08;
GO
CREATE TABLE dbo.Registrations
(
    Id int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    DisplayName nvarchar(20) NOT NULL,
    Session nvarchar(20) NOT NULL
);
