namespace Week07Registration.Models;

public class Registration
{
    public int Id { get; set; }
    public string DisplayName { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public string Session { get; set; } = string.Empty;
    public string? Note { get; set; }
    public DateTime CreatedAt { get; set; }
}

// 若你的專案名稱不是 Week07Registration，請調整 namespace。
// Id 由資料庫產生；CreatedAt 由後端在保存時設定。
