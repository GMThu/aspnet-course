using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Week09Lab.Pages;

public class IndexModel : PageModel
{
    [BindProperty]
    public RegistrationInput Input { get; set; } = new();

    public bool Submitted { get; set; }

    public void OnGet()
    {
    }

    public void OnPost()
    {
        if (!ModelState.IsValid)
        {
            return;
        }

        Submitted = true;
    }

    public class RegistrationInput
    {
        [Required(ErrorMessage = "請輸入顯示名稱")]
        [StringLength(20, ErrorMessage = "顯示名稱最多 20 字")]
        [Display(Name = "顯示名稱")]
        public string DisplayName { get; set; } = string.Empty;

        [Required(ErrorMessage = "請輸入 Email")]
        [EmailAddress(ErrorMessage = "Email 格式不正確")]
        [StringLength(254, ErrorMessage = "Email 最多 254 字")]
        [Display(Name = "Email")]
        public string Email { get; set; } = string.Empty;

        [Required(ErrorMessage = "請選擇參加場次")]
        [RegularExpression("^(週三晚上|週六下午)$", ErrorMessage = "請選擇有效場次")]
        [StringLength(20)]
        [Display(Name = "參加場次")]
        public string Session { get; set; } = string.Empty;

        [StringLength(100, ErrorMessage = "備註最多 100 字")]
        [Display(Name = "備註")]
        public string? Note { get; set; }
    }
}
