using SmartCampusHelpDesk.Models;

namespace SmartCampusHelpDesk.Services;

public class IssueStore
{
    private readonly List<HelpDeskIssue> _issues = new();
    private readonly object _lock = new();
    private int _nextId = 1;

    public IReadOnlyList<HelpDeskIssue> GetAll()
    {
        lock (_lock)
        {
            return _issues.OrderByDescending(i => i.Date).ToList();
        }
    }

    public HelpDeskIssue Add(HelpDeskIssue issue)
    {
        lock (_lock)
        {
            issue.Id = _nextId++;
            if (issue.Date == default)
            {
                issue.Date = DateTime.Now;
            }

            _issues.Add(issue);
            return issue;
        }
    }

    public int Count
    {
        get
        {
            lock (_lock)
            {
                return _issues.Count;
            }
        }
    }
}
