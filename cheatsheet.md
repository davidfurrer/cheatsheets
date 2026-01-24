# Claude Code

Anthropic's official CLI for Claude - an interactive command-line tool for software engineering tasks.

Official Repository: https://github.com/anthropics/claude-code

## Installation

```bash
npm install -g @anthropic-ai/claude-code
```

## Basic Usage

```bash
# Start Claude Code
claude

# Start with a specific message
claude "help me debug this error"

# Use a specific model
claude --model sonnet  # or opus, haiku
```

## Slash Commands

Available commands during a Claude Code session:

| Command | Description |
| ------- | ----------- |
| `/help` | Get help with using Claude Code |
| `/clear` | Clear conversation history |
| `/exit` | Exit Claude Code |

## Key Features

### Model Selection

- **Opus**: Most capable model for complex tasks
- **Sonnet**: Balanced performance and speed (default)
- **Haiku**: Fast, efficient for straightforward tasks

### File Operations

Claude Code can:
- Read any file in your directory
- Edit files using exact string replacement
- Create new files (use sparingly - prefer editing)
- Search codebases with pattern matching

### Git Integration

```bash
# Claude Code can help with:
git status    # Check repository status
git diff      # Review changes
git add       # Stage files
git commit    # Create commits
git push      # Push to remote
gh pr create  # Create pull requests
```

**Git Safety**:
- Never runs destructive commands without confirmation
- Follows commit message conventions from git log
- Respects pre-commit hooks
- Creates descriptive commit messages

### Task Management

Claude Code uses an internal todo system to:
- Break down complex tasks into steps
- Track progress on multi-step operations
- Ensure all requirements are met

## Configuration

### Settings Location

```bash
~/.config/claude-code/settings.json
```

### Common Settings

- Model preferences
- Hook configurations
- MCP server integrations
- IDE integrations

### Hooks

Hooks are shell commands that execute in response to events:

```json
{
  "hooks": {
    "user-prompt-submit": "echo 'Processing...'",
    "tool-call": "notify-send 'Tool called'"
  }
}
```

## MCP Servers

Model Context Protocol servers extend Claude Code with additional capabilities:
- Database connections
- API integrations
- Custom tools

## Best Practices

### Effective Communication

```bash
# Be specific
❌ "fix the bug"
✅ "fix the authentication error in src/auth.js:42"

# Provide context
❌ "add a feature"
✅ "add user registration with email validation to the auth system"
```

### File References

Reference code with `file_path:line_number`:
```
Check the error handling in src/utils/api.ts:156
```

### Task Breakdown

For complex tasks:
1. Ask Claude to plan the implementation first
2. Review the plan
3. Execute step by step
4. Test after each major change

### Code Quality

Claude Code automatically:
- Preserves existing code style
- Maintains proper indentation
- Avoids over-engineering
- Focuses on requested changes only

## Common Workflows

### Debugging

```bash
claude "analyze the error in app.log and suggest fixes"
```

### Feature Implementation

```bash
claude "add a dark mode toggle to components/Settings.tsx"
```

### Code Review

```bash
claude "review the changes in my last commit for security issues"
```

### Refactoring

```bash
claude "refactor the UserService class to use async/await"
```

## Tips

1. **Start Simple**: Let Claude read files before asking for changes
2. **Iterate**: Make changes incrementally and test
3. **Be Specific**: Provide exact file paths and line numbers when possible
4. **Review Changes**: Always review diffs before committing
5. **Use Context**: Claude remembers conversation history

## Limitations

- No interactive commands (avoid `git rebase -i`, `git add -i`)
- Command timeout: 2 minutes (default), 10 minutes (max)
- Requires API key with sufficient credits

## Troubleshooting

### Authentication Issues

```bash
# Set API key
export ANTHROPIC_API_KEY=your_key_here
```

### Network Errors

Claude Code automatically retries failed operations with exponential backoff.

### Hook Failures

If blocked by a hook, check hook configuration:
```bash
cat ~/.config/claude-code/settings.json
```

## Resources

- [GitHub Issues](https://github.com/anthropics/claude-code/issues) - Report bugs and feedback
- [Documentation](https://docs.anthropic.com) - Full API documentation
- [Claude API Reference](https://docs.anthropic.com/api) - API details

## Examples

### Create a New Feature

```
User: Add a user profile page with avatar upload
Claude: I'll help you create a user profile page. Let me first explore
        the current routing structure and components...

        [Reads relevant files, plans implementation, creates components]
```

### Debug an Error

```
User: The build is failing with type errors
Claude: Let me run the build and analyze the errors...

        [Runs build, identifies errors, fixes them one by one]
```

### Git Workflow

```
User: Create a commit with my changes
Claude: [Checks git status, reviews diffs, creates descriptive commit]

User: Create a pull request
Claude: [Analyzes commits, creates PR with summary and test plan]
```

## Advanced Features

### Parallel Tool Execution

Claude Code can execute multiple independent operations simultaneously for better performance.

### Background Tasks

Long-running commands can be executed in the background while Claude continues working.

### Specialized Agents

Claude Code can spawn specialized agents for:
- Codebase exploration
- Test running
- Documentation generation
- Security analysis

## Security

Claude Code:
- Never runs destructive commands without context
- Validates security vulnerabilities (XSS, SQL injection, etc.)
- Refuses malicious requests
- Respects `.gitignore` patterns

## Cost Optimization

- Use Haiku for simple tasks (faster, cheaper)
- Use Sonnet for general development (balanced)
- Use Opus for complex architecture decisions
