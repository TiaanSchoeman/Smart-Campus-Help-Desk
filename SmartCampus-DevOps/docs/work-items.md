# Azure Boards work items — copy exactly

Epic
- Title: Smart Campus Help Desk
- Description: Deliver a campus help-desk web app with source control, CI and Blue-Green releases.

Feature
- Title: Controlled development and Blue-Green deployment
- Parent: Epic above

User Stories (parent = Feature)

1. US-01 Capture a campus support request
   - Tasks: Create HelpDeskIssue model; Build submit form; Persist in memory store

2. US-02 View submitted support requests
   - Tasks: Build issues table; Add date and status columns

3. US-03 Source control and branching
   - Tasks: Init Git; Create Azure Repos remote; Create main, develop, feature branches

4. US-04 Pull request review workflow
   - Tasks: Push feature change; Open PR; Review diff; Complete PR

5. US-05 Continuous Integration pipeline
   - Tasks: Add azure-pipelines.yml; Restore/Build/Test/Publish; Capture success and failure runs

6. US-06 Blue-Green release and rollback
   - Tasks: Deploy v1 to Blue; Deploy v2 to Green; Validate Green; Switch production; Demonstrate rollback
