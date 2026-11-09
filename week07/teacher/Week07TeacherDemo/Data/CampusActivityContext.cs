using Microsoft.EntityFrameworkCore;
using Week07TeacherDemo.Models;

namespace Week07TeacherDemo.Data;

public class CampusActivityContext : DbContext
{
    public CampusActivityContext(DbContextOptions<CampusActivityContext> options)
        : base(options)
    {
    }

    public DbSet<Registration> Registrations => Set<Registration>();
}
