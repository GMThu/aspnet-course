using Microsoft.EntityFrameworkCore;
using Week09Lab.Data;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddRazorPages();
builder.Services.AddDbContext<CampusActivityContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("CampusActivity")));

var app = builder.Build();
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();
app.MapRazorPages();
app.Run();

// 供獨立測試專案啟動；課堂不需修改。
public partial class Program { }
