using System.ComponentModel.DataAnnotations;

namespace SmartCampusHelpDesk.Models;

public class HelpDeskIssue
{
    public int Id { get; set; }

    [Required(ErrorMessage = "Student name is required.")]
    [Display(Name = "Student Name")]
    public string StudentName { get; set; } = string.Empty;

    [Required(ErrorMessage = "Category is required.")]
    public string Category { get; set; } = string.Empty;

    [Required(ErrorMessage = "Description is required.")]
    public string Description { get; set; } = string.Empty;

    public string Status { get; set; } = "Open";

    public DateTime Date { get; set; } = DateTime.Now;
}
