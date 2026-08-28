using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using SmartCampusHelpDesk.Models;
using SmartCampusHelpDesk.Services;

namespace SmartCampusHelpDesk.Pages;

public class IndexModel : PageModel
{
    private readonly ILogger<IndexModel> _logger;

    public IndexModel(ILogger<IndexModel> logger)
    {
        _logger = logger;
    }

    [BindProperty]
    public HelpDeskIssue NewIssue { get; set; } = new();

    public IReadOnlyList<HelpDeskIssue> Issues { get; private set; } = new List<HelpDeskIssue>();

    public List<string> Categories { get; } = new()
    {
        "Network",
        "Computer",
        "Software",
        "Account",
        "Other"
    };

    /// <summary>Open (non-Closed) issue count per category, for the v2.0 homepage category cards.</summary>
    public IReadOnlyDictionary<string, int> OpenCountsByCategory { get; private set; } =
        new Dictionary<string, int>();

    public List<string> Statuses { get; } = new()
    {
        "Open",
        "In Progress",
        "Closed"
    };

    public void OnGet()
    {
        Issues = IssueStore.Issues.OrderByDescending(i => i.Date).ToList();
        OpenCountsByCategory = Categories.ToDictionary(
            c => c,
            c => IssueStore.Issues.Count(i => i.Category == c && i.Status != "Closed"));
    }

    public IActionResult OnPost()
    {
        if (!ModelState.IsValid)
        {
            Issues = IssueStore.Issues.OrderByDescending(i => i.Date).ToList();
            OpenCountsByCategory = Categories.ToDictionary(
                c => c,
                c => IssueStore.Issues.Count(i => i.Category == c && i.Status != "Closed"));
            return Page();
        }

        NewIssue.Date = DateTime.Now;
        IssueStore.Add(NewIssue);

        return RedirectToPage();
    }
}
