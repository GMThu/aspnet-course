using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Week05TeacherDemo.Pages;

public class IndexModel : PageModel
{
    [BindProperty]
    public RegistrationInput Input { get; set; } = new();
    public bool Submitted { get; set; }
    public void OnGet() { }
    public void OnPost() { Submitted = true; }
    public class RegistrationInput
    {
        public string DisplayName { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
        public string Session { get; set; } = string.Empty;
        public string? Note { get; set; }
    }
}
