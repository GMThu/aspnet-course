using Microsoft.EntityFrameworkCore;
using Week09Lab.Models;

namespace Week09Lab.Data;

public class CampusActivityContext : DbContext
{
    public CampusActivityContext(DbContextOptions<CampusActivityContext> options)
        : base(options) { }

    public DbSet<Registration> Registrations => Set<Registration>();
}
