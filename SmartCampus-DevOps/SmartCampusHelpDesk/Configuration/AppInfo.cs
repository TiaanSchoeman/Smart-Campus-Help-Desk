namespace SmartCampusHelpDesk.Configuration;

public class AppInfo
{
    public const string SectionName = "AppInfo";

    public string Version { get; set; } = "1.0";
    public string EnvironmentName { get; set; } = "BLUE";
    public bool EnhancedUi { get; set; }
}
