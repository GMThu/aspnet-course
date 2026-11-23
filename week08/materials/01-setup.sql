-- 教師備援：主課先用 SSMS 介面建庫、再用 01-create-table.sql 建表，不必額外執行本檔。
-- 第八週：老師先示範，再分段執行。可重跑；不刪除既有資料。
USE master;
GO
IF DB_ID(N'CampusActivityLab08') IS NULL
    EXEC(N'CREATE DATABASE CampusActivityLab08');
GO
USE CampusActivityLab08;
GO
IF OBJECT_ID(N'dbo.Registrations', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.Registrations
    (
        Id int IDENTITY(1,1) NOT NULL PRIMARY KEY,
        DisplayName nvarchar(20) NOT NULL,
        Session nvarchar(20) NOT NULL
    );
END;
GO
SELECT DB_NAME() AS CurrentDatabase;
SELECT Id, DisplayName, Session FROM dbo.Registrations ORDER BY Id;
