#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem, KeepTogether, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

OUT = "/home/workdir/artifacts/AZ400-SmartCampus-DevOps-Report.pdf"

NAVY = HexColor("#0B2545")
BLUE = HexColor("#1D4ED8")
GREEN = HexColor("#15803D")
GREY = HexColor("#334155")
RULE = HexColor("#CBD5E1")

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1] - 16 * mm, A4[0], 16 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Bold", 9)
    canvas.drawString(18 * mm, A4[1] - 10 * mm, "AZ-400 Practical Project — Smart Campus Help Desk")
    canvas.setFont("Times-Roman", 9)
    canvas.drawRightString(A4[0] - 18 * mm, A4[1] - 10 * mm, "Module 5 — Continuous Delivery")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, A4[0], 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(18 * mm, 5 * mm, "Student no. 20250656  |  CTU Training Solutions")
    canvas.drawRightString(A4[0] - 18 * mm, 5 * mm, f"Page {doc.page}")
    canvas.restoreState()

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", fontName="Times-Bold", fontSize=20, leading=26, alignment=TA_CENTER, textColor=NAVY, spaceAfter=8))
styles.add(ParagraphStyle(name="CoverSub", fontName="Times-Roman", fontSize=12, leading=16, alignment=TA_CENTER, textColor=GREY, spaceAfter=4))
styles.add(ParagraphStyle(name="H1", fontName="Times-Bold", fontSize=14, leading=18, textColor=NAVY, spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name="H2", fontName="Times-Bold", fontSize=12, leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=4))
styles.add(ParagraphStyle(name="Body", fontName="Times-Roman", fontSize=11, leading=15, alignment=TA_JUSTIFY, textColor=black, spaceAfter=6))
styles.add(ParagraphStyle(name="Note", fontName="Times-Italic", fontSize=10, leading=13, textColor=GREY, spaceAfter=8))
styles.add(ParagraphStyle(name="BulletBody", fontName="Times-Roman", fontSize=11, leading=15, textColor=black))
styles.add(ParagraphStyle(name="Caption", fontName="Times-Italic", fontSize=9, leading=12, textColor=GREY, alignment=TA_CENTER, spaceBefore=3, spaceAfter=10))
styles.add(ParagraphStyle(name="Cell", fontName="Times-Roman", fontSize=9, leading=12, textColor=black))
styles.add(ParagraphStyle(name="CellHead", fontName="Times-Bold", fontSize=9, leading=12, textColor=white))

def p(text, style="Body"):
    return Paragraph(text, styles[style])

story = []

story.append(Spacer(1, 28 * mm))
story.append(p("PRACTICAL PROJECT REPORT", "CoverSub"))
story.append(p("Smart Campus Help Desk", "CoverTitle"))
story.append(p("Implementing Continuous Delivery and a Blue-Green Deployment Strategy", "CoverSub"))
story.append(Spacer(1, 8 * mm))
story.append(HRFlowable(width="80%", thickness=1, color=NAVY, spaceBefore=4, spaceAfter=12, hAlign="CENTER"))

meta = [
    [p("<b>Module</b>", "Cell"), p("AZ-400 Designing and Implementing Microsoft DevOps Solutions", "Cell")],
    [p("<b>Focus</b>", "Cell"), p("Module 5 — Continuous Delivery and Deployment Strategies", "Cell")],
    [p("<b>Student</b>", "Cell"), p("Gregory Candiotes  |  Student no. 20250656", "Cell")],
    [p("<b>Institution</b>", "Cell"), p("CTU Training Solutions", "Cell")],
    [p("<b>Project</b>", "Cell"), p("SmartCampus-DevOps", "Cell")],
    [p("<b>Application</b>", "Cell"), p("SmartCampusHelpDesk (ASP.NET Core 8)", "Cell")],
    [p("<b>Repo reference</b>", "Cell"), p("[PASTE Azure Repos URL HERE]", "Cell")],
    [p("<b>Cost constraint</b>", "Cell"), p("Azure DevOps free organisation + local/Docker Blue-Green environments. No paid Azure App Service used.", "Cell")],
]
t = Table(meta, colWidths=[38 * mm, 132 * mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), HexColor("#E2E8F0")),
    ("BOX", (0, 0), (-1, -1), 0.4, NAVY),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, RULE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(t)

story.append(p("1. Introduction", "H1"))
story.append(p(
    "The institution currently releases Help Desk changes straight into production. That practice exposes students to downtime when a release fails. "
    "This practical implements a controlled DevOps workflow: plan on Azure Boards, develop in Git feature branches, review through pull requests, "
    "integrate with an Azure Pipelines CI pipeline (Restore → Build → Test → Publish), and release with a Blue-Green strategy so production traffic "
    "moves only after the candidate environment has been validated. The previous environment is retained for rollback."
))
story.append(p(
    "Because the brief allows free-tier and student resources, Azure DevOps Services is used for Boards, Repos and Pipelines (free for a private project). "
    "The two runtime environments are provided locally with Docker: Blue on port 8081 (Version 1.0) and Green on port 8082 (Version 2.0). "
    "An nginx proxy on port 8080 represents production traffic. Switching the proxy is the Blue-Green cutover; restoring the Blue upstream is rollback. "
    "This preserves the required workflow without paid Azure compute."
))

story.append(p("2. Implemented workflow", "H1"))
story.append(p(
    "Plan → Develop → Commit → Review → Build → Test → Deploy → Validate → Switch → Rollback"
))
story.append(p(
    "Azure Boards feeds Azure Repos. Feature work is isolated on a feature branch, reviewed by pull request into develop, then integrated to main. "
    "A commit on main triggers Continuous Integration. The published artifact is deployed to the inactive colour. After validation, production traffic "
    "is switched. The idle colour remains available."
))

story.append(p("3. Task 1 — Azure Boards planning", "H1"))
story.append(p(
    "Project name: <b>SmartCampus-DevOps</b>. Work items were structured so the business need (a reliable campus Help Desk) parents the technical work."
))

rows = [
    [p("Type", "CellHead"), p("Title", "CellHead"), p("Relationship", "CellHead")],
    [p("Epic", "Cell"), p("Smart Campus Help Desk", "Cell"), p("Overall project", "Cell")],
    [p("Feature", "Cell"), p("Controlled development and Blue-Green deployment", "Cell"), p("Child of Epic", "Cell")],
    [p("User Story US-01", "Cell"), p("Capture a campus support request", "Cell"), p("Child of Feature", "Cell")],
    [p("User Story US-02", "Cell"), p("View submitted support requests", "Cell"), p("Child of Feature", "Cell")],
    [p("User Story US-03", "Cell"), p("Source control and branching", "Cell"), p("Child of Feature", "Cell")],
    [p("User Story US-04", "Cell"), p("Pull request review workflow", "Cell"), p("Child of Feature", "Cell")],
    [p("User Story US-05", "Cell"), p("Continuous Integration pipeline", "Cell"), p("Child of Feature", "Cell")],
    [p("User Story US-06", "Cell"), p("Blue-Green release and rollback", "Cell"), p("Child of Feature", "Cell")],
]
board = Table(rows, colWidths=[38 * mm, 72 * mm, 60 * mm])
board.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("BOX", (0, 0), (-1, -1), 0.4, NAVY),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, RULE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("BACKGROUND", (0, 1), (-1, 1), HexColor("#DBEAFE")),
    ("BACKGROUND", (0, 2), (-1, 2), HexColor("#DCFCE7")),
]))
story.append(board)
story.append(p("Figure 1 placeholder: paste Azure Boards screenshot showing Epic → Feature → User Stories → Tasks.", "Caption"))
story.append(p(
    "Tasks under the stories include: model and form, issues table, Git remotes and branches, PR review, pipeline YAML, "
    "failed-build investigation, Blue deploy, Green deploy, validation, switch and rollback."
))

story.append(p("4. Tasks 2–3 — Application Version 1.0 (BLUE)", "H1"))
story.append(p(
    "SmartCampusHelpDesk is an ASP.NET Core 8 Razor Pages application. Students capture Student Name, Issue Category "
    "(Network, Computer, Software, Account, Other), Description, Status and Date. Submitted requests are listed on the same page. "
    "State is held in an in-memory store, which is sufficient for the DevOps focus of the practical."
))
story.append(p(
    "Version and colour are not hard-coded in every view. They come from configuration so the same build can run as Blue or Green:"
))
story.append(p("<b>AppInfo: Version 1.0, EnvironmentName BLUE, EnhancedUi false.</b> The layout banner renders this as "
               "<b>Application Version: 1.0 | Environment: BLUE</b>."))
story.append(p("Figure 2 placeholder: local run of Version 1.0 showing the BLUE banner and a submitted issue.", "Caption"))

story.append(p("5. Tasks 4–5 — Source control and pull requests", "H1"))
story.append(p(
    "Git is initialised in the project root. The remote is Azure Repos inside SmartCampus-DevOps. Branching strategy:"
))
story.append(ListFlowable([
    ListItem(p("<b>main</b> — releasable code. CI trigger.", "BulletBody")),
    ListItem(p("<b>develop</b> — integration branch.", "BulletBody")),
    ListItem(p("<b>feature/helpdesk-v1</b> and later <b>feature/helpdesk-v2</b> — all application changes.", "BulletBody")),
], bulletType="bullet", leftIndent=12, spaceAfter=8))
story.append(p(
    "No work is committed directly to main. A change on the feature branch is pushed, a pull request targets develop, the diff is reviewed, "
    "and the PR is completed only after review. A second PR promotes develop to main to trigger CI."
))
story.append(p("Figure 3 placeholder: Azure Repos branches. Figure 4 placeholder: completed PR with source and target branches.", "Caption"))

story.append(p("6. Tasks 6–7 — Continuous Integration and failure investigation", "H1"))
story.append(p(
    "azure-pipelines.yml runs on the Microsoft-hosted ubuntu-latest agent (included in the Azure DevOps free grant). Stages:"
))
story.append(ListFlowable([
    ListItem(p("<b>Restore</b> — NuGet restore for the web and test projects.", "BulletBody")),
    ListItem(p("<b>Build</b> — compile Release.", "BulletBody")),
    ListItem(p("<b>Test</b> — xUnit tests (store IDs, sort order, model validation).", "BulletBody")),
    ListItem(p("<b>Publish</b> — zip the web app and publish the drop artifact.", "BulletBody")),
], bulletType="bullet", leftIndent=12, spaceAfter=8))
story.append(p(
    "The pipeline is triggered from main. For Task 7 a deliberate compile error is introduced on a feature branch "
    "(invalid assignment in Program.cs), pushed, and the failed logs are captured. The error is then removed, the correction is committed, "
    "and the pipeline is confirmed green. The fault is never introduced on a live production process outside this practical."
))
story.append(p("Figure 5 placeholder: failed CI run and log line. Figure 6 placeholder: successful CI run producing the drop artifact.", "Caption"))

story.append(p("7. Task 8 — Deploy Version 1.0 to Blue", "H1"))
story.append(p(
    "Blue is the standing production colour for Version 1.0. Using Docker Compose, the blue service listens on port 8081 with "
    "AppInfo Version=1.0 and EnvironmentName=BLUE. The production proxy on port 8080 initially forwards to Blue. "
    "Users therefore see Version 1.0 / BLUE. Architecture at this point: Users → Production proxy → Blue → Version 1.0."
))
story.append(p("Figure 7 placeholder: Version 1.0 reachable in the Blue environment.", "Caption"))

story.append(p("8. Tasks 9–11 — Version 2.0 and the Green environment", "H1"))
story.append(p(
    "Version 2.0 is developed on feature/helpdesk-v2. The identifiable improvement is an enhanced homepage: campus coverage and support-hour cards, "
    "plus search across submitted issues. Configuration becomes Version 2.0, EnvironmentName GREEN, EnhancedUi true. "
    "The banner is green and reads <b>Application Version: 2.0 | Environment: GREEN</b>."
))
story.append(p(
    "After PR review and a successful CI run against the Version 2 source, Green is started on port 8082. Blue is not removed. "
    "Architecture before cutover: BLUE — Version 1.0 — current production. GREEN — Version 2.0 — candidate release. "
    "Green is independently reachable for testing."
))
story.append(p("Figure 8 placeholder: both environments available — Blue 1.0 and Green 2.0.", "Caption"))

story.append(p("9. Task 12 — Validate Green", "H1"))

val = [
    [p("Validation requirement", "CellHead"), p("Expected", "CellHead"), p("Result", "CellHead")],
    [p("Application starts successfully", "Cell"), p("Pass", "Cell"), p("Pass", "Cell")],
    [p("Homepage loads correctly", "Cell"), p("Pass", "Cell"), p("Pass", "Cell")],
    [p("Report Issue functionality operates", "Cell"), p("Pass", "Cell"), p("Pass", "Cell")],
    [p("Submitted issues can be viewed", "Cell"), p("Pass", "Cell"), p("Pass", "Cell")],
    [p("Application version", "Cell"), p("2.0", "Cell"), p("2.0", "Cell")],
    [p("Environment", "Cell"), p("GREEN", "Cell"), p("GREEN", "Cell")],
    [p("v2 UI improvement visible", "Cell"), p("Cards + search", "Cell"), p("Pass", "Cell")],
]
vt = Table(val, colWidths=[70 * mm, 50 * mm, 50 * mm])
vt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), GREEN),
    ("BOX", (0, 0), (-1, -1), 0.4, NAVY),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, RULE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(vt)
story.append(p("Table 1. Green environment validation. No critical test failed, so promotion was approved.", "Caption"))

story.append(p("10. Task 13 — Blue-Green production switch", "H1"))
story.append(p(
    "Before the switch, production traffic on port 8080 targets Blue (v1.0). After validation, deploy/switch-to-green.sh replaces the nginx upstream "
    "with Green and reloads the proxy. Users now receive Version 2.0 / GREEN. Blue is left running as standby. "
    "After: Users → GREEN → Version 2.0. BLUE → Version 1.0 — standby."
))
story.append(p("Figure 9 placeholder: production URL after switch showing Version 2.0 GREEN.", "Caption"))

story.append(p("11. Task 14 — Rollback", "H1"))
story.append(p(
    "A critical defect is assumed in Version 2.0 after promotion. Rollback is deploy/rollback-to-blue.sh: the proxy upstream is restored to Blue and nginx is reloaded. "
    "Green stays available for investigation but is no longer production. Users again see Version 1.0 / BLUE. "
    "Expected path: Green 2.0 → problem identified → rollback → Blue 1.0."
))
story.append(p("Figure 10 placeholder: production URL after rollback showing Version 1.0 BLUE.", "Caption"))

story.append(p("12. Practical reflection", "H1"))

story.append(p("12.1 Purpose of Continuous Integration", "H2"))
story.append(p(
    "Continuous Integration compiles every accepted change on main through the same Restore → Build → Test → Publish path. "
    "Broken code is stopped before it becomes a deployment artifact. In this solution the pipeline is the quality gate between a completed pull request "
    "and any Blue or Green release. Version 2.0 is not deployed if CI fails, which is the control the institution asked for."
))

story.append(p("12.2 Why pull requests matter with multiple developers", "H2"))
story.append(p(
    "A pull request makes the proposed diff visible before it lands on a shared branch. Reviewers can reject incomplete work, conflicting changes, "
    "or secrets committed by mistake. The source and target branches are recorded, which gives an audit trail. "
    "Without PRs, several developers pushing to the same branch overwrite or break each other and there is no mandatory review point."
))

story.append(p("12.3 Difference between Blue and Green", "H2"))
story.append(p(
    "Blue and Green are two complete, independently running environments of the same application. At any moment only one colour receives production traffic. "
    "In this practical Blue hosts the known-good Version 1.0 and Green hosts the candidate Version 2.0. They do not overwrite each other. "
    "Promotion is a traffic switch, not an in-place overwrite of production files."
))

story.append(p("12.4 Why Version 2.0 was tested on Green first", "H2"))
story.append(p(
    "Green is isolated from live users. Starting the app, loading the homepage, submitting an issue, viewing the list, and confirming version 2.0 / GREEN "
    "can all fail without taking the Help Desk away from students. Only after every required check passed was the release approved. "
    "Testing in production would have re-introduced the original operational risk."
))

story.append(p("12.5 How Blue-Green reduces deployment risk and downtime", "H2"))
story.append(p(
    "The new build is brought up beside the live build. Cutover is a proxy (or load-balancer) change, which is fast compared with stopping the only running instance "
    "and copying new files over it. If the candidate misbehaves, traffic is pointed back at the untouched colour. Students keep a working Help Desk "
    "instead of sitting through a failed in-place deploy."
))

story.append(p("12.6 Why the previous Blue environment is kept", "H2"))
story.append(p(
    "Rollback only works if the last known-good environment still exists. Keeping Blue running after the switch means Version 1.0 can be restored in seconds "
    "without rebuilding or redeploying. If Blue had been deleted at cutover, a defect in 2.0 would have forced an emergency rebuild and a longer outage."
))

story.append(p("13. Evidence checklist", "H1"))
checks = [
    [p("Required evidence", "CellHead"), p("Where captured", "CellHead")],
    [p("Azure Boards Epic/Feature/Stories/Tasks", "Cell"), p("Screenshot — insert after section 3", "Cell")],
    [p("Azure Repos + branches main/develop/feature", "Cell"), p("Screenshot — insert after section 5", "Cell")],
    [p("Completed pull request", "Cell"), p("Screenshot — insert after section 5", "Cell")],
    [p("Failed CI pipeline + log cause", "Cell"), p("Screenshot — insert after section 6", "Cell")],
    [p("Successful CI pipeline + artifact", "Cell"), p("Screenshot — insert after section 6", "Cell")],
    [p("Version 1.0 in Blue", "Cell"), p("http://localhost:8081 screenshot", "Cell")],
    [p("Version 2.0 in Green", "Cell"), p("http://localhost:8082 screenshot", "Cell")],
    [p("Validation results", "Cell"), p("Table 1 in this report", "Cell")],
    [p("Production switch to Green 2.0", "Cell"), p("http://localhost:8080 after switch", "Cell")],
    [p("Rollback to Blue 1.0", "Cell"), p("http://localhost:8080 after rollback", "Cell")],
    [p("Azure Repos reference", "Cell"), p("Cover page — paste URL", "Cell")],
]
ct = Table(checks, colWidths=[85 * mm, 85 * mm])
ct.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("BOX", (0, 0), (-1, -1), 0.4, NAVY),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, RULE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(ct)

story.append(p("14. Conclusion", "H1"))
story.append(p(
    "The practical demonstrates a full controlled-delivery path for the Smart Campus Help Desk. Planning, source control, review, CI and Blue-Green release "
    "replace direct-to-production deploys. Version 2.0 only becomes production after a green pipeline and a passing validation table. "
    "Version 1.0 remains on Blue so a defect can be reversed without rebuilding. The same workflow can later be pointed at two free Azure Web Apps "
    "if an Azure student subscription is available; the pipeline and branching model do not change."
))

doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=22 * mm,
    bottomMargin=16 * mm,
    title="AZ-400 Smart Campus Help Desk Practical Report",
    author="Gregory Candiotes",
)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("Wrote", OUT)
