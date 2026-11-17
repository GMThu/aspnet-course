using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Week08TeacherDemo.Data;

#nullable disable

namespace Week08TeacherDemo.Migrations;

[DbContext(typeof(CampusActivityContext))]
public class CampusActivityContextModelSnapshot : ModelSnapshot
{
    protected override void BuildModel(ModelBuilder modelBuilder)
    {
#pragma warning disable 612, 618
        modelBuilder
            .HasAnnotation("ProductVersion", "10.0.14")
            .HasAnnotation("Relational:MaxIdentifierLength", 128);

        SqlServerModelBuilderExtensions.UseIdentityColumns(modelBuilder);

        modelBuilder.Entity("Week08TeacherDemo.Models.Registration", entity =>
        {
            entity.Property<int>("Id")
                .ValueGeneratedOnAdd()
                .HasColumnType("int");
            SqlServerPropertyBuilderExtensions.UseIdentityColumn(entity.Property<int>("Id"));
            entity.Property<DateTime>("CreatedAt").HasColumnType("datetime2");
            entity.Property<string>("DisplayName").IsRequired().HasColumnType("nvarchar(max)");
            entity.Property<string>("Email").IsRequired().HasColumnType("nvarchar(max)");
            entity.Property<string>("Note").HasColumnType("nvarchar(max)");
            entity.Property<string>("Session").IsRequired().HasColumnType("nvarchar(max)");
            entity.HasKey("Id");
            entity.ToTable("Registrations");
        });
#pragma warning restore 612, 618
    }
}
