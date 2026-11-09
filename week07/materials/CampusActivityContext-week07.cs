using Microsoft.EntityFrameworkCore;
using Week07Registration.Models;

namespace Week07Registration.Data;

public class CampusActivityContext : DbContext
{
    public CampusActivityContext(
        DbContextOptions<CampusActivityContext> options)
        : base(options)
    {
    }

    public DbSet<Registration> Registrations => Set<Registration>();
}

// 若你的專案名稱不同，請調整 using 與 namespace。
