using SmartCampusHelpDesk.Configuration;
using SmartCampusHelpDesk.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.Configure<AppInfo>(builder.Configuration.GetSection(AppInfo.SectionName));
builder.Services.AddSingleton<IssueStore>();
builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();
app.MapRazorPages();
app.Run();
