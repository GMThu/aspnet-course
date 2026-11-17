using System.ComponentModel.DataAnnotations;

namespace Week09Lab.Models;

public class Registration
{
    public int Id { get; set; }

    [Required, StringLength(20)]
    public string DisplayName { get; set; } = string.Empty;

    [Required, StringLength(254)]
    public string Email { get; set; } = string.Empty;

    [Required, StringLength(20)]
    public string Session { get; set; } = string.Empty;

    [StringLength(100)]
    public string? Note { get; set; }
}
