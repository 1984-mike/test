# GitHub MCP Usage Guide

## Overview

The GitHub Model Context Protocol (MCP) provides a comprehensive set of tools for interacting with GitHub repositories directly from Claude. This allows you to perform repository management, code analysis, issue tracking, and collaboration tasks without leaving your conversation.

## Prerequisites

- Access to GitHub repositories (public or private with appropriate permissions)
- Basic understanding of Git and GitHub concepts
- Knowledge of repository owner/organization names and repository names

## Core Repository Operations

### 1. Repository Exploration

#### Get Repository Contents
```
Get file contents from: owner/repo/path
```
- **Use case**: Examine files, directories, or entire repository structure
- **Parameters**: owner, repo, path, branch (optional)
- **Returns**: File contents or directory listing

#### Search Repositories
```
Search for repositories with query: "python calculator"
```
- **Use case**: Find repositories by keywords, language, or topics
- **Parameters**: query, page, perPage
- **Advanced queries**: Use GitHub search syntax (language:python, stars:>100, etc.)

### 2. Repository Management

#### Create New Repository
```
Create repository: "my-new-project"
```
- **Parameters**: name, description, private (boolean), autoInit
- **Best practice**: Include meaningful description and choose appropriate visibility

#### Fork Repository
```
Fork repository: owner/repo to my account
```
- **Use case**: Create your own copy for contributions or experimentation
- **Parameters**: owner, repo, organization (optional)

## File Operations

### 1. Single File Management

#### Create or Update Files
```
Create/update file at: owner/repo/path/filename.py
```
- **Parameters**: owner, repo, path, content, message, branch, sha (for updates)
- **Note**: SHA required when updating existing files

#### Read Multiple Files
```
Get contents of: file1.py, file2.js, README.md
```
- **Use case**: Batch file examination for code analysis or documentation review

### 2. Batch Operations

#### Push Multiple Files
```
Push files to: owner/repo/branch with commit message
```
- **Parameters**: owner, repo, branch, files (array), message
- **Use case**: Deploy multiple changes in a single commit
- **Structure**: Each file needs path and content

## Branch Management

### Create Branches
```
Create branch: "feature/new-calculator" from main
```
- **Parameters**: owner, repo, branch, from_branch (optional)
- **Best practice**: Use descriptive branch names following naming conventions

### List Commits
```
Get commit history for: owner/repo
```
- **Parameters**: owner, repo, sha (optional), page, perPage
- **Use case**: Code history analysis, debugging, or audit trails

## Issue Management

### 1. Issue Operations

#### Create Issues
```
Create issue: "Bug in calculator division"
```
- **Parameters**: owner, repo, title, body, labels, assignees, milestone
- **Best practice**: Include reproduction steps and expected vs actual behavior

#### List and Filter Issues
```
List issues: state=open, labels=["bug", "priority-high"]
```
- **Parameters**: owner, repo, state, labels, sort, direction, since
- **Filtering**: Combine multiple criteria for precise issue management

#### Update Issues
```
Update issue #123: change state to closed
```
- **Parameters**: owner, repo, issue_number, title, body, state, labels, assignees

### 2. Issue Interaction

#### Add Comments
```
Comment on issue #123: "Fixed in PR #124"
```
- **Parameters**: owner, repo, issue_number, body
- **Use case**: Progress updates, additional information, or resolution details

#### Get Issue Details
```
Get details for issue #123
```
- **Returns**: Complete issue information including comments, labels, and status

## Pull Request Workflow

### 1. Pull Request Creation

#### Create Pull Request
```
Create PR: merge "feature-branch" into "main"
```
- **Parameters**: owner, repo, title, head, base, body, draft
- **Best practice**: Include clear description of changes and testing performed

#### List Pull Requests
```
List PRs: state=open, base=main
```
- **Parameters**: owner, repo, state, head, base, sort, direction
- **Filtering**: Filter by branch, state, or other criteria

### 2. Pull Request Management

#### Get PR Details
```
Get details for PR #45
```
- **Returns**: PR metadata, changed files, status checks, and reviews

#### Get Changed Files
```
Get files changed in PR #45
```
- **Use case**: Code review preparation or impact analysis

#### Review Pull Requests
```
Create review for PR #45: APPROVE with comments
```
- **Parameters**: owner, repo, pull_number, body, event, comments
- **Events**: APPROVE, REQUEST_CHANGES, COMMENT

### 3. Pull Request Completion

#### Merge Pull Request
```
Merge PR #45 using squash method
```
- **Parameters**: owner, repo, pull_number, merge_method, commit_title, commit_message
- **Methods**: merge, squash, rebase

#### Update PR Branch
```
Update PR #45 branch with latest changes
```
- **Use case**: Resolve conflicts or incorporate recent changes

## Search and Discovery

### 1. Code Search
```
Search code: "function calculateTotal" in language:javascript
```
- **Parameters**: q (query), sort, order, page, per_page
- **Advanced**: Use GitHub's code search syntax for precise results

### 2. Issue Search
```
Search issues: "bug calculator" state:open label:priority-high
```
- **Parameters**: q (query), sort, order, page, per_page
- **Use case**: Find related issues across repositories

### 3. User Search
```
Search users: "location:sanfrancisco language:python"
```
- **Parameters**: q (query), sort, order, page, per_page
- **Use case**: Find collaborators or community members

## Advanced Workflows

### 1. Repository Analysis
```
1. Get repository structure
2. Examine key files (README, package.json, requirements.txt)
3. Review recent commits
4. Check open issues and PRs
5. Analyze code patterns
```

### 2. Collaborative Development
```
1. Fork repository
2. Create feature branch
3. Make changes across multiple files
4. Push changes with descriptive commit
5. Create pull request
6. Participate in code review
7. Merge when approved
```

### 3. Project Management
```
1. Create issues for tasks/bugs
2. Label and assign issues
3. Track progress through comments
4. Link PRs to issues
5. Close issues when resolved
```

## Best Practices

### Repository Management
- Use clear, descriptive commit messages
- Follow consistent branching strategies
- Keep repositories organized with proper folder structure
- Include comprehensive README files

### Issue Tracking
- Use descriptive titles and detailed descriptions
- Apply appropriate labels for categorization
- Assign issues to responsible team members
- Link related issues and PRs

### Code Review
- Provide constructive feedback
- Focus on code quality, security, and maintainability
- Test changes before approval
- Use PR templates for consistency

### Security Considerations
- Never commit sensitive information (passwords, API keys)
- Review file changes carefully before pushing
- Use private repositories for confidential projects
- Implement proper access controls

## Error Handling

### Common Issues
- **File not found**: Verify repository, path, and branch names
- **Permission denied**: Check repository access rights
- **SHA required**: Get current file SHA when updating existing files
- **Branch conflicts**: Resolve merge conflicts before operations

### Troubleshooting Steps
1. Verify repository ownership and permissions
2. Check branch existence and naming
3. Confirm file paths and structure
4. Review GitHub API rate limits
5. Validate required parameters

## Integration Patterns

### Automated Workflows
- **CI/CD Integration**: Trigger builds on code changes
- **Issue Automation**: Auto-create issues from error reports
- **Documentation Sync**: Update docs when code changes
- **Release Management**: Automate version tagging and releases

### Development Workflows
- **Feature Development**: Branch → Code → PR → Review → Merge
- **Bug Fixes**: Issue → Branch → Fix → Test → PR → Merge
- **Documentation**: Write → Review → Update → Deploy
- **Collaboration**: Fork → Modify → PR → Discuss → Integrate

## Conclusion

The GitHub MCP provides powerful capabilities for repository management, code collaboration, and project organization. By combining these tools effectively, you can streamline development workflows, improve code quality, and enhance team collaboration.

Remember to follow GitHub best practices, maintain clear communication through issues and PRs, and leverage the search capabilities to discover and learn from the broader GitHub community.

---

*This guide covers the essential GitHub MCP functions. For specific use cases or advanced scenarios, experiment with combining multiple operations to achieve your goals.*