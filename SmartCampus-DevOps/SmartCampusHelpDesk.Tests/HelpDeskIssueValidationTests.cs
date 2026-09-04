using System.ComponentModel.DataAnnotations;
using SmartCampusHelpDesk.Models;

namespace SmartCampusHelpDesk.Tests;

public class HelpDeskIssueValidationTests
{
    [Fact]
    public void ValidIssue_PassesValidation()
    {
        var issue = new HelpDeskIssue
        {
            StudentName = "Lebo Mokoena",
            Category = "Network",
            Description = "No internet in residence block B",
            Status = "Open"
        };

        var results = Validate(issue);
        Assert.Empty(results);
    }

    [Fact]
    public void MissingName_FailsValidation()
    {
        var issue = new HelpDeskIssue
        {
            Category = "Computer",
            Description = "Keyboard not working"
        };

        var results = Validate(issue);
        Assert.Contains(results, r => r.MemberNames.Contains(nameof(HelpDeskIssue.StudentName)));
    }

    private static List<ValidationResult> Validate(HelpDeskIssue issue)
    {
        var results = new List<ValidationResult>();
        Validator.TryValidateObject(issue, new ValidationContext(issue), results, true);
        return results;
    }
}
