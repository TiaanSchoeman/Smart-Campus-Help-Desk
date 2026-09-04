# Smart Campus Help Desk — AZ-400 Practical

Zero-cost CI/CD + Blue-Green pack. Azure DevOps itself is free. No paid Azure resources required.

## What this repo contains

- ASP.NET Core 8 Razor Pages Help Desk
- Version/environment driven by config (`AppInfo`)
- xUnit tests for the CI Test stage
- `azure-pipelines.yml` — Restore → Build → Test → Publish
- Docker Blue (v1.0) + Green (v2.0) + nginx production switch

## Local Version 1.0 (BLUE)

```bash
cd SmartCampusHelpDesk
dotnet run
```

Banner must show `Application Version: 1.0 | Environment: BLUE`.

## Local Version 2.0 (GREEN)

```bash
cd SmartCampusHelpDesk
dotnet run --environment Green
```

Or:

```bash
AppInfo__Version=2.0 AppInfo__EnvironmentName=GREEN AppInfo__EnhancedUi=true dotnet run
```

v2 adds campus coverage cards, support hours, and issue search.

## Free Blue-Green (Docker, R0)

```bash
docker compose up --build
```

| URL | Role |
|---|---|
| http://localhost:8081 | BLUE v1.0 |
| http://localhost:8082 | GREEN v2.0 |
| http://localhost:8080 | Production proxy (starts on BLUE) |

Switch:

```bash
./deploy/switch-to-green.sh
```

Rollback:

```bash
./deploy/rollback-to-blue.sh
```

## Azure DevOps (free, no card)

1. https://dev.azure.com → create org → new project `SmartCampus-DevOps`
2. Boards → create the work items in `docs/work-items.md`
3. Repos → push this folder
4. Branches: `main`, `develop`, `feature/helpdesk-v1`, then later `feature/helpdesk-v2`
5. PR: feature → develop, then develop → main
6. Pipelines → New pipeline → Azure Repos Git → existing `azure-pipelines.yml`
7. Task 7 failure: add `int broken = "x";` in `Program.cs`, push, capture failed run, revert, capture green run

Pipeline does not deploy to paid App Service. Blue/Green evidence is the two local/Docker environments plus the production proxy switch. That matches the required workflow without spend.

## Evidence you still have to screenshot yourself

Azure Boards hierarchy, Azure Repos + branches, completed PR, failed CI, successful CI, Blue v1, Green v2, validation table, switch, rollback.

Drop those screenshots into the PDF report.
