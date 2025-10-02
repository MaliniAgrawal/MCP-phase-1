# mcp-aws-cli-generator (phase-1)

Short helper repo for generating AWS CLI commands via MCP server.

Important notes
- This repository includes a project-level `.gitignore` that excludes virtual environments, Python caches, IDE files, AWS/SAM build artifacts, and local AWS credentials. It helps avoid accidentally committing secrets or environment-specific files.
- If you accidentally committed credentials or other sensitive files, remove them from the repo history and untrack them locally. A safe way to stop tracking a file while keeping it locally is:

```bash
# stop tracking a file already committed (example: .aws/credentials)
git rm --cached .aws/credentials
git commit -m "remove local credentials from repo"
```

For full secrets removal from history consider using `git filter-repo` or `git filter-branch` (follow your organization's policy before rewriting history).

Contact
- For questions about development setup or deployment, check `requirements.txt` and `deployment/template.yaml`.

# MCP-phase-1
