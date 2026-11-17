using Microsoft.EntityFrameworkCore;
using Week08TeacherDemo.Models;

namespace Week08TeacherDemo.Data;

public class CampusActivityContext : DbContext
{
    public CampusActivityContext(DbContextOptions<CampusActivityContext> options)
        : base(options)
    {
    }

    public DbSet<Registration> Registrations => Set<Registration>();
}
