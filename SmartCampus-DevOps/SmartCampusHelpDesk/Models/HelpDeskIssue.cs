using System.ComponentModel.DataAnnotations;

namespace SmartCampusHelpDesk.Models;

public class HelpDeskIssue
{
    public int Id { get; set; }

    [Required(ErrorMessage = "Student name is required.")]
    [Display(Name = "Student Name")]
    [StringLength(80, MinimumLength = 2)]
    public string StudentName { get; set; } = string.Empty;

    [Required(ErrorMessage = "Category is required.")]
    [Display(Name = "Issue Category")]
    public string Category { get; set; } = string.Empty;

    [Required(ErrorMessage = "Description is required.")]
    [StringLength(500, MinimumLength = 5)]
    public string Description { get; set; } = string.Empty;

    public string Status { get; set; } = "Open";

    [Display(Name = "Date")]
    public DateTime Date { get; set; } = DateTime.Now;
}
