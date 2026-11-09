using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using Week07TeacherDemo.Data;
using Week07TeacherDemo.Models;

namespace Week07TeacherDemo.Pages;

public class IndexModel : PageModel
{
    private readonly CampusActivityContext _db;

    public IndexModel(CampusActivityContext db)
    {
        _db = db;
    }

    [BindProperty]
    public RegistrationInput Input { get; set; } = new();

    public List<Registration> Registrations { get; set; } = [];

    [TempData]
    public string? SavedMessage { get; set; }

    public async Task OnGetAsync()
    {
        await LoadRegistrationsAsync();
    }

    public async Task<IActionResult> OnPostAsync()
    {
        if (!ModelState.IsValid)
        {
            await LoadRegistrationsAsync();
            return Page();
        }

        var registration = new Registration
        {
            DisplayName = Input.DisplayName,
            Email = Input.Email,
            Session = Input.Session,
            Note = Input.Note,
            CreatedAt = DateTime.UtcNow
        };

        _db.Registrations.Add(registration);
        await _db.SaveChangesAsync();

        SavedMessage = "報名已保存";
        return RedirectToPage();
    }

    private async Task LoadRegistrationsAsync()
    {
        Registrations = await _db.Registrations
            .AsNoTracking()
            .OrderByDescending(registration => registration.Id)
            .Take(10)
            .ToListAsync();
    }

    public class RegistrationInput
    {
        [Required(ErrorMessage = "請輸入顯示名稱")]
        [StringLength(20, ErrorMessage = "顯示名稱最多 20 字")]
        public string DisplayName { get; set; } = string.Empty;

        [Required(ErrorMessage = "請輸入 Email")]
        [EmailAddress(ErrorMessage = "Email 格式不正確")]
        public string Email { get; set; } = string.Empty;

        [Required(ErrorMessage = "請選擇參加場次")]
        public string Session { get; set; } = string.Empty;

        [StringLength(100, ErrorMessage = "備註最多 100 字")]
        public string? Note { get; set; }
    }
}
