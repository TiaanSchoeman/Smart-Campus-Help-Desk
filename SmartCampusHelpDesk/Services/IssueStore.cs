using SmartCampusHelpDesk.Models;

namespace SmartCampusHelpDesk.Services;

/// <summary>
/// Simple in-memory store for HelpDeskIssue records.
/// Not thread-safe by design — acceptable for this practical/demo scope.
/// </summary>
public static class IssueStore
{
    private static readonly List<HelpDeskIssue> _issues = new();
    private static int _nextId = 1;

    public static IReadOnlyList<HelpDeskIssue> Issues => _issues;

    public static void Add(HelpDeskIssue issue)
    {
        issue.Id = _nextId++;
        _issues.Add(issue);
    }
}
