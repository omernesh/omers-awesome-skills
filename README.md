# Omer's Awesome Skills

A collection of expert-level Claude Code skills for automation, AI agents, workflow engineering, and more.

## Available Skills

### n8n Workflow Engineer

Expert-level skill for designing, implementing, validating, and maintaining production-ready n8n automation workflows using comprehensive MCP tooling.

**Features:**
- Complete workflow design and implementation
- AI agent architecture with tool integration
- Validation and quality assurance
- Error handling and resilience patterns
- Support for 537+ n8n nodes
- Access to 2,653+ community templates

**Use Cases:**
- REST API integrations
- AI chatbots with tools
- Scheduled data pipelines
- Complex multi-agent AI systems

[View Full Documentation](./n8n-workflow-engineer/skill.md)

## Installation

### Using Claude Code

To use these skills in Claude Code, add this repository as a plugin marketplace:

```bash
/plugin marketplace add omernesh/omers-awesome-skills
```

Then install the skills:

```bash
/plugin install n8n-workflow-engineer@omers-awesome-skills
```

Or browse and install via the UI:

1. Run `/plugin marketplace add omernesh/omers-awesome-skills`
2. Select "Browse and install plugins"
3. Select "omers-awesome-skills"
4. Select the skill you want to install
5. Select "Install now"

### Using Claude.ai or API

Download the skill folder as a ZIP file and upload it through:

- **Claude.ai**: Settings → Skills → Upload custom skill
- **API**: Use the [Skills API](https://docs.claude.com/en/api/skills-guide#creating-a-skill)

### Configuration

After installation, configure your n8n MCP server with:

- Your n8n instance URL
- API credentials
- Appropriate timezone settings

## Requirements

- Claude Code with MCP support
- n8n instance (self-hosted or cloud)
- n8n MCP server configured

## Contributing

Feel free to submit issues, suggestions, or pull requests to improve these skills!

## License

MIT License - feel free to use and modify as needed.

## Author

Created by [omernesh](https://github.com/omernesh)
