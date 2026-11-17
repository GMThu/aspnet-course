第九週｜EF Core 接上第六週表單（120 分鐘）
先開 start-here.html 或 Week09-EFCore-Student-Guide.pdf。
Starter：起始表單，複製到自己的 Week09Lab 後才修改。
Checkpoints：01-Database → 02-Save → 03-Query，逐段將內容複製至工作專案根目錄，保留資料夾層級；每次先停止網站，複製後 dotnet clean，再 build／run；clean 不會刪除資料庫或 Migrations。
Complete：獨立完成版，固定 Migration；僅供全新 Lab09 或已由同一份 Complete 建立的資料庫。途中落後要保留原工作專案與 Migrations，套用後續 Checkpoints，勿直接換 Complete。
verify-in-ssms.sql：只讀驗收。find-by-id.sql：以自己記下的 Id 查詢。acceptance.txt：學生紀錄。
固定 .NET 10／EF Core 10.0.15／dotnet-ef 10.0.15。首次套件還原需網路。
資料庫 CampusActivityLab09，表 dbo.Registrations；五欄 Id／DisplayName／Email／Session／Note；本週場次週三晚上／週六下午。
不改 CampusActivityLab08，也不使用舊 EF Core 延伸的 CampusActivityDb。
學生包不含 bin、obj 或已安裝 NuGet 套件；外部文件與回網站需連網。
完成版會顯示所有人最近十筆，僅供本機課堂假資料，不是已完成登入與權限保護的公開報名服務。
