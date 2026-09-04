using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Options;
using SmartCampusHelpDesk.Configuration;
using SmartCampusHelpDesk.Models;
using SmartCampusHelpDesk.Services;

namespace SmartCampusHelpDesk.Pages;

public class IndexModel : PageModel
{
    private readonly IssueStore _store;
    private readonly AppInfo _appInfo;

    public IndexModel(IssueStore store, IOptions<AppInfo> appInfo)
    {
        _store = store;
        _appInfo = appInfo.Value;
    }

    [BindProperty]
    public HelpDeskIssue NewIssue { get; set; } = new();

    [BindProperty(SupportsGet = true)]
    public string? Search { get; set; }

    public IReadOnlyList<HelpDeskIssue> Issues { get; private set; } = new List<HelpDeskIssue>();

    public bool EnhancedUi => _appInfo.EnhancedUi;

    public List<string> Categories { get; } = new()
    {
        "Network",
        "Computer",
        "Software",
        "Account",
        "Other"
    };

    public List<string> Statuses { get; } = new()
    {
        "Open",
        "In Progress",
        "Closed"
    };

    public void OnGet()
    {
        Issues = Filter(_store.GetAll());
    }

    public IActionResult OnPost()
    {
        if (!ModelState.IsValid)
        {
            Issues = Filter(_store.GetAll());
            return Page();
        }

        NewIssue.Date = DateTime.Now;
        _store.Add(NewIssue);
        return RedirectToPage(new { Search });
    }

    private IReadOnlyList<HelpDeskIssue> Filter(IReadOnlyList<HelpDeskIssue> source)
    {
        if (string.IsNullOrWhiteSpace(Search))
        {
            return source;
        }

        var term = Search.Trim();
        return source
            .Where(i =>
                i.StudentName.Contains(term, StringComparison.OrdinalIgnoreCase) ||
                i.Category.Contains(term, StringComparison.OrdinalIgnoreCase) ||
                i.Description.Contains(term, StringComparison.OrdinalIgnoreCase) ||
                i.Status.Contains(term, StringComparison.OrdinalIgnoreCase))
            .ToList();
    }
}
