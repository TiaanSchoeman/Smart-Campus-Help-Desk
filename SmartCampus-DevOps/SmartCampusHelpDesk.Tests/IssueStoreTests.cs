using SmartCampusHelpDesk.Models;
using SmartCampusHelpDesk.Services;

namespace SmartCampusHelpDesk.Tests;

public class IssueStoreTests
{
    [Fact]
    public void Add_AssignsIncrementalIds()
    {
        var store = new IssueStore();

        var first = store.Add(new HelpDeskIssue
        {
            StudentName = "Anele",
            Category = "Network",
            Description = "Wi-Fi down in Lab 3",
            Status = "Open"
        });

        var second = store.Add(new HelpDeskIssue
        {
            StudentName = "Thabo",
            Category = "Account",
            Description = "Cannot reset campus password",
            Status = "Open"
        });

        Assert.Equal(1, first.Id);
        Assert.Equal(2, second.Id);
        Assert.Equal(2, store.Count);
    }

    [Fact]
    public void GetAll_ReturnsNewestFirst()
    {
        var store = new IssueStore();
        store.Add(new HelpDeskIssue
        {
            StudentName = "First",
            Category = "Software",
            Description = "Office will not launch",
            Date = DateTime.Now.AddMinutes(-10)
        });
        store.Add(new HelpDeskIssue
        {
            StudentName = "Second",
            Category = "Computer",
            Description = "Lab PC will not boot",
            Date = DateTime.Now
        });

        var issues = store.GetAll();
        Assert.Equal("Second", issues[0].StudentName);
    }
}
