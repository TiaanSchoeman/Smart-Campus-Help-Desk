# Smart Campus Help Desk

Web application through which students report campus technical problems, built
for the AZ-400 practical on continuous delivery and Blue-Green deployment.

## Branching strategy

| Branch | Purpose | Protected |
|---|---|---|
| `main` | Release branch. CI triggers here; deployments build from it. | Yes |
| `develop` | Integration branch. All feature work merges here first. | Yes |
| `feature/*` | Short-lived. One branch per change, deleted after merge. | No |

Both long-lived branches carry a blocking policy requiring one approving
reviewer who is not the author, all comments resolved, and basic merge only.
Direct pushes are rejected.

## Working on this

```bash
git switch develop && git pull
git switch -c feature/short-description
# ...change something...
git add -A
git commit -m "Describe the change, not the file"
git push -u origin feature/short-description
```

Then open a Pull Request into `develop` and link the work item it implements.

## Environments

| Environment | Version | Role |
|---|---|---|
| Blue | 1.0 | Current stable production release |
| Green | 2.0 | Candidate release, validated before promotion |

The running application displays its version and environment in the interface.
That banner is the evidence artifact for every deployment task — if it is
wrong, the deployment evidence is wrong.

> The version and environment values must **not** be marked as deployment slot
> settings in App Service. Slot-sticky settings stay behind during a swap, so
> production would keep reporting BLUE after Green was promoted.
