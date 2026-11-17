第九週獨立完成版，程式與三段 Checkpoints 的最終程式相同，但內附固定的 InitialCreate Migration。
僅供尚未建立 CampusActivityLab09 的環境，或已使用這份 Complete 建立的資料庫。
若已在自己的工作副本產生 Migration，請留在原專案，依序套用後續 02-Save、03-Query；不要用本版的 Migration 覆蓋原檔。
自行產生與本版的 MigrationId（含時間戳）不同；表名一樣不代表可直接套用另一套歷史。請勿刪資料表、刪歷史或直接修改 MigrationId 解錯。
確認適用後：核對 appsettings.json 伺服器與 CampusActivityLab09，再依序 dotnet restore、dotnet tool restore、dotnet ef database update、dotnet run --launch-profile http；不再 migrations add InitialCreate。首次還原需要網路。
