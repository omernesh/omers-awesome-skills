---
name: n8n-workflow-engineer---expert-automation-skill
description: Expert-level skill for designing, implementing, validating, and maintaining production-ready n8n automation workflows using comprehensive MCP tooling.
metadata:
  version: 1.0
---
**Created:** 2025-10-22 | **Type:** Technical Engineering Skill

## 🎯 Purpose

Expert-level skill for designing, implementing, validating, and maintaining production-ready n8n automation workflows using comprehensive MCP tooling. Handles everything from simple webhook-to-API flows to complex multi-agent AI systems.

---

## 📊 Knowledge Base

- **Node Count:** 537 total nodes (270 AI-capable, 108 triggers)
- **Template Library:** 2,653 community workflows
- **Documentation Coverage:** 88% (470 nodes documented)
- **User Instance:** https://your-n8n-instance.com (configure your own instance URL)

---

## 🛠️ Core Capabilities

### 1. Discovery & Research (Pre-Build Phase)

**When to use:** Before starting any workflow, always research available nodes and patterns.

#### Primary Tools:

- `search_nodes({query: "keyword", includeExamples: true})` - Find nodes with real-world examples
- `list_nodes({category: "trigger|transform|AI", limit: 200})` - Browse by category
- `search_templates({query: "chatbot"})` - Find pre-built workflows
- `list_node_templates({nodeTypes: ["n8n-nodes-base.httpRequest"]})` - Templates using specific nodes
- `get_templates_for_task({task: "ai_automation"})` - Curated templates by use case

#### Decision Matrix:

```

Query Type → Tool Selection
• "How do I..." → search\_nodes with includeExamples=true
• "Show me AI nodes" → list\_nodes({category: "AI"})
• "Chatbot workflows" → search\_templates({query: "chatbot"})
• "HTTP Request examples" → list\_node\_templates({nodeTypes: ["..."]})

```

### 2. Node Configuration (Build Phase)

**Philosophy:** Start small (essentials), validate often, expand as needed.

#### Configuration Strategy:

```

1.  get\_node\_essentials({nodeType: "nodes-base.httpRequest"})
       → Returns 10-20 key properties (95% smaller than full schema)
       → Perfect for initial configuration
       

2.  validate\_node\_minimal({nodeType: "...", config: {}})
       → Quick check for missing required fields
       → Returns: list of required fields only

3.  get\_node\_info({nodeType: "..."}) 
       → ONLY if advanced properties needed
       → Full 200+ property schema (100KB+ response)
       → Use sparingly due to size

<!-- end list -->

```

#### Property Discovery:

- `search_node_properties({nodeType: "nodes-base.httpRequest", query: "auth"})` - Find specific properties
- `get_property_dependencies({nodeType: "..."})` - See which fields unlock others
- `get_node_documentation({nodeType: "nodes-base.slack"})` - Human-readable docs (87% coverage)

### 3. Workflow Architecture (Design Phase)

#### Common Patterns Library:

##### Pattern A: Webhook → Process → Response

```

Use case: API endpoints, form submissions, external integrations
Components: Webhook (trigger) → Code/Transform → Respond to Webhook
Key: Webhook data is nested under .body property\!

Example flow:
[Webhook] → [Code: process $json.body] → [Respond to Webhook]

```

##### Pattern B: Scheduled Data Pipeline

```

Use case: ETL, monitoring, backups, reports
Components: Schedule Trigger → HTTP Request → Transform → Database/Notification

Example flow:
[Schedule: daily 6am] → [HTTP: fetch data] → [Code: transform] → [Postgres: insert]

```

##### Pattern C: AI Agent with Tools

```

Use case: Conversational AI, task automation, decision-making
Components: Chat Trigger → AI Agent + Language Model + Tools + Memory
CRITICAL: AI connections use sourceOutput parameter\!

Example flow:
[Chat Trigger] --main--\> [AI Agent]
[OpenAI Model] --ai\_languageModel--\> [AI Agent]
[HTTP Tool] --ai\_tool--\> [AI Agent]
[Memory] --ai\_memory--\> [AI Agent]

```

##### Pattern D: Error-Resilient Processing

```

Use case: Critical workflows, batch processing, API rate limits
Components: Any node with continueOnFail + Error Workflow

Example config:
{
  continueOnFail: true,
  retryOnFail: true,
  maxTries: 3,
  waitBetweenTries: 5000
}

````

### 4. Code Node Mastery

#### JavaScript Patterns:

```javascript
// ✅ CORRECT: Access webhook data
const webhookData = $json.body;
const { username, email } = webhookData;

// ✅ CORRECT: Process all items
const allItems = $input.all();
const total = allItems.reduce((sum, item) => 
  sum + (item.json.amount || 0), 0);

// ✅ CORRECT: Return format (MUST be array with json property)
return [{
  json: {
    result: "success",
    processedAt: DateTime.now().toISO(),
    data: processedData
  }
}];

// ❌ WRONG: Common mistakes
const data = $json.name; // Missing .body for webhooks
return { result: "success" }; // Missing array wrapper and json property
````

#### Available Built-ins:

  - `$helpers.httpRequest()` - Make HTTP calls
  - `DateTime` (Luxon) - Date/time handling
  - `$jmespath()` - JSON querying
  - crypto, Buffer, URL - Node.js built-ins

### 5\. AI Agent Architecture

#### Essential Connection Types (8 types):

```
1. ai_languageModel: Model → AI Agent (REQUIRED, 1-2)
2. ai_tool: Tools → AI Agent (recommended 1+)
3. ai_memory: Memory → AI Agent (optional, 0-1)
4. ai_outputParser: Parser → AI Agent (optional)
5. ai_embedding: Embeddings → Vector Store (for RAG)
6. ai_vectorStore: Vector Store → Vector Store Tool
7. ai_document: Documents → Vector Store
8. ai_textSplitter: Splitter → Document chain
```

#### AI Tool Configuration Requirements:

##### HTTP Request Tool:

```javascript
CRITICAL Requirements:
• toolDescription: 15+ chars, explain WHEN to use
• url: Can include {placeholders}
• placeholderDefinitions: Define all placeholders
• auth: Credentials if needed

Example:
{
  method: "POST",
  url: "[https://api.github.com/repos/](https://api.github.com/repos/){owner}/{repo}/issues",
  toolDescription: "Create GitHub issues. Requires owner (username), repo (repository name), title, and body.",
  placeholderDefinitions: {
    values: [
      {name: "owner", description: "Repository owner"},
      {name: "repo", description: "Repository name"},
      {name: "title", description: "Issue title"},
      {name: "body", description: "Issue description"}
    ]
  },
  sendBody: true,
  jsonBody: "={{ { title: $json.title, body: $json.body } }}"
}
```

##### Code Tool:

```javascript
CRITICAL Requirements:
• name: Alphanumeric + underscore only
• description: 10+ chars explaining purpose
• code: JavaScript or Python
• inputSchema: Recommended for type safety

Example:
{
  name: "calculate_shipping",
  description: "Calculate shipping cost based on weight (kg) and distance (km)",
  language: "javaScript",
  code: `
    const cost = 5 + ($input.weight * 2) + ($input.distance * 0.1);
    return { cost: parseFloat(cost.toFixed(2)), currency: 'USD' };
  `,
  specifyInputSchema: true,
  inputSchema: JSON.stringify({
    type: "object",
    properties: {
      weight: {type: "number", description: "Package weight in kg"},
      distance: {type: "number", description: "Distance in km"}
    },
    required: ["weight", "distance"]
  })
}
```

#### Streaming vs Non-Streaming:

```
Streaming Mode:
• Chat Trigger: responseMode = "streaming"
• AI Agent: NO main output connections
• Response streams back through Chat Trigger automatically
• Best for: Real-time chat UX

Non-Streaming Mode:
• Chat Trigger: responseMode = "lastNode"
• AI Agent: Can have main output connections
• Response from last node
• Best for: Post-processing, multiple outputs
```

### 6\. Validation & Quality Assurance

#### Validation Hierarchy (Always validate before deploy\!):

```
Level 1 - Individual Nodes:
→ validate_node_minimal({nodeType, config}) 
  • Fast check for missing required fields
  • Use during iterative build
  
→ validate_node_operation({nodeType, config, profile: "runtime"})
  • Full validation with warnings/suggestions
  • Profiles: minimal, runtime, ai-friendly, strict
  • Returns automated fix suggestions

Level 2 - Workflow Components:
→ validate_workflow_connections({workflow})
  • Structure only: nodes, connections, cycles, triggers
  • Fast pre-deployment check

→ validate_workflow_expressions({workflow})
  • n8n expression syntax: {{}}, $json, $node references
  • Returns errors with locations

Level 3 - Complete Workflow:
→ n8n_validate_workflow({id: "workflow_id"})
  • Validates live workflow from n8n instance
  • Checks: nodes, connections, expressions, AI tools
  • Returns: errors, warnings, suggestions, fixes

→ validate_workflow({workflow, options})
  • Validates workflow JSON object
  • Configurable validation options
  • Most comprehensive check
```

#### Auto-Fix Capabilities:

```javascript
n8n_autofix_workflow({
  id: "workflow_id",
  applyFixes: true,
  fixTypes: [
    "expression-format",      // Fix {{}} syntax
    "typeversion-correction", // Update node versions
    "error-output-config",    // Fix error handling
    "webhook-missing-path"    // Add webhook paths
  ],
  confidenceThreshold: "high" // high|medium|low
})
```

### 7\. Workflow Management (CRUD Operations)

#### Create Workflow:

```javascript
n8n_create_workflow({
  name: "My Workflow",
  nodes: [
    {
      id: "webhook_1",
      name: "Webhook",
      type: "n8n-nodes-base.webhook",
      position: [100, 100],
      typeVersion: 2,
      parameters: {
        path: "my-endpoint",
        httpMethod: "POST"
      }
    }
  ],
  connections: {
    "Webhook": {
      main: [[{node: "Next Node", type: "main", index: 0}]]
    }
  }
})

Returns: workflow object with ID
Created: INACTIVE by default (activate separately)
```

#### Update Strategies:

##### Full Update (Replace everything):

```javascript
n8n_update_full_workflow({
  id: "workflow_id",
  name: "Updated Name",
  nodes: [...complete nodes array...],
  connections: {...complete connections...}
})

Use when: Complete redesign, migration, major refactor
```

##### Partial Update (Recommended - Incremental changes):

```javascript
n8n_update_partial_workflow({
  id: "workflow_id",
  operations: [
    // Add node
    {
      type: "addNode",
      node: {
        name: "New HTTP Request",
        type: "n8n-nodes-base.httpRequest",
        position: [300, 200],
        parameters: {...}
      }
    },
    
    // Connect nodes
    {
      type: "addConnection",
      source: "Webhook",
      target: "New HTTP Request",
      sourceOutput: "main" // or ai_languageModel, ai_tool, etc.
    },

    // Update node parameters
    {
      type: "updateNode",
      nodeName: "HTTP Request",
      updates: {
        "parameters.url": "[https://new-api.com](https://new-api.com)",
        "parameters.method": "POST"
      }
    },

    // Enable/disable
    {type: "enableNode", nodeName: "HTTP Request"},
    {type: "disableNode", nodeName: "Old Node"},

    // Remove
    {type: "removeNode", nodeName: "Old Node"},
    {type: "removeConnection", source: "A", target: "B"}
  ],
  continueOnError: false // true = best-effort mode
})

✅ Best Practice: Use partial updates for iterative development
✅ Supports smart parameters for multi-output nodes (branch, case)
✅ Full AI connection support (ai_languageModel, ai_tool, etc.)
```

#### Read Operations:

```
• n8n_list_workflows({limit: 100, active: true})
  → Minimal metadata: id, name, active, tags, dates
  → Pagination via cursor (before/after)
  
• n8n_get_workflow({id})
  → Complete workflow: nodes, connections, settings

• n8n_get_workflow_structure({id})
  → Nodes + connections only (no parameters)

• n8n_get_workflow_minimal({id})
  → Just: id, name, active, tags
```

#### Execution Management:

```javascript
// Smart data retrieval (avoid token limits!)
Step 1: Preview
n8n_get_execution({id, mode: "preview"})
→ Structure + counts only, no actual data
→ Assess size before fetching

Step 2: Fetch appropriately
n8n_get_execution({
id,
mode: "summary", // 2 items per node (default)
// OR mode: "filtered", // Custom filtering
// OR mode: "full", // All data (use carefully!)
nodeNames: ["HTTP Request"], // Filter to specific nodes
itemsLimit: 5, // Items per node
includeInputData: false // Inputs + outputs vs outputs only
})

// List executions
n8n_list_executions({
workflowId: "...",
status: "success|error|waiting",
limit: 100
})
```

### 8\. Best Practices Checklist

#### Pre-Build Phase:

```
☑ Research available nodes (search_nodes with examples)
☑ Check existing templates (search_templates)
☑ Review documentation (get_node_documentation)
☑ Plan workflow architecture (triggers → processors → outputs)
```

#### Build Phase:

```
☑ Start with get_node_essentials (not full schema)
☑ Validate each node (validate_node_minimal)
☑ Build incrementally with partial updates
☑ Test connections as you go
☑ Use meaningful node names
☑ Add notes/documentation to complex nodes
```

#### AI Agent Phase:

```
☑ Connect language model BEFORE creating AI Agent
☑ Minimum 1 tool (more tools = more capabilities)
☑ Every tool MUST have clear description (15+ chars)
☑ Use streaming for real-time UX
☑ Set appropriate maxIterations (default 10, max 50)
☑ Consider fallback model for production (needsFallback=true)
☑ NO main outputs from AI Agent in streaming mode
```

#### Validation Phase:

```
☑ validate_workflow_connections (structure check)
☑ validate_workflow_expressions (syntax check)
☑ n8n_validate_workflow (comprehensive check)
☑ Review all errors/warnings/suggestions
☑ Consider auto-fix for common issues
☑ Test with real data before deploying
```

#### Deployment Phase:

```
☑ Final validation passed
☑ Error handling configured (continueOnFail, retryOnFail)
☑ Credentials tested
☑ Webhook paths verified
☑ Activate workflow
☑ Monitor first executions
☑ Document workflow purpose and maintenance notes
```

## 🎓 Common Use Cases & Solutions

### Use Case 1: REST API Integration

```
Task: Create endpoint that receives webhooks, calls external API, responds
Tools:
1. search_nodes({query: "webhook http", includeExamples: true})
2. get_node_essentials({nodeType: "nodes-base.webhook"})
3. get_node_essentials({nodeType: "nodes-base.httpRequest"})
4. n8n_create_workflow → Build structure
5. n8n_validate_workflow → Check before deploy

Pattern:
[Webhook] → [Code: transform] → [HTTP Request] → [Respond to Webhook]

Key Points:
• Webhook data under .body property
• Use Respond to Webhook (not just HTTP Response)
• Add error handling with continueOnFail
```

### Use Case 2: AI Chatbot with Tools

```
Task: Chat interface with AI that can search knowledge base and call APIs
Tools:
1. tools_documentation({topic: "ai_agents_guide"})
2. search_nodes({query: "AI agent chat", includeExamples: true})
3. get_node_essentials for: Chat Trigger, AI Agent, OpenAI, HTTP Tool
4. n8n_create_workflow with AI architecture
5. n8n_validate_workflow (critical for AI connections!)

Pattern:
[Chat Trigger] --main--> [AI Agent]
[OpenAI Model] --ai_languageModel--> [AI Agent]
[Vector Store Tool] --ai_tool--> [AI Agent]
[HTTP Request Tool] --ai_tool--> [AI Agent]
[Window Buffer Memory] --ai_memory--> [AI Agent]

Key Points:
• Language model connected FIRST
• sourceOutput: "ai_languageModel" (critical!)
• sourceOutput: "ai_tool" for all tools
• Tool descriptions = 15+ chars, explain WHEN to use
• responseMode: "streaming" for real-time UX
```

### Use Case 3: Data Pipeline with Error Recovery

```
Task: Scheduled data sync from API to database with retry logic
Tools:
1. search_nodes({query: "schedule database postgres"})
2. get_node_essentials for: Schedule, HTTP Request, Postgres
3. Configure error handling properties
4. n8n_create_workflow
5. Test with n8n_list_executions

Pattern:
[Schedule Trigger] → [HTTP: fetch] → [Code: transform] → [Postgres: upsert]

Error Handling Config:
{
  continueOnFail: true,
  retryOnFail: true,
  maxTries: 3,
  waitBetweenTries: 5000,
  onError: "continueErrorOutput" // Modern error routing
}

Key Points:
• Use schedules in user's timezone (configure in n8n settings)
• Validate data before database insert
• Log errors for monitoring
• Use upsert for idempotency
```

## 🚨 Troubleshooting Guide

### Problem: "AI Agent has no language model"

```javascript
Cause: Language model not connected or wrong sourceOutput
Solution:
n8n_update_partial_workflow({
  operations: [{
    type: "addConnection",
    source: "OpenAI Chat Model",
    target: "AI Agent",
    sourceOutput: "ai_languageModel" // ← CRITICAL!
  }]
})
```

### Problem: "Tool has no description"

```javascript
Cause: Missing toolDescription on HTTP Tool or description on Code Tool
Solution:
{
  type: "updateNode",
  nodeName: "HTTP Request Tool",
  updates: {
    "parameters.toolDescription": "Get weather for a city. Provide city name (e.g., 'London')."
  }
}
Minimum: 15 characters, explain WHEN to use
```

### Problem: "Cannot access webhook data"

```javascript
Cause: Trying to access $json.name when webhook data is under $json.body
Solution in Code node:
// ❌ WRONG
const name = $json.name;

// ✅ CORRECT
const { name, email } = $json.body;
```

### Problem: "Validation shows 'invalid return format'"

```javascript
Cause: Code node not returning array with json property
Solution:
// ❌ WRONG
return { result: "success" };

// ✅ CORRECT
return [{
  json: { result: "success" }
}];
```

### Problem: "Streaming mode not working"

```javascript
Causes:
1. Chat Trigger not set to streaming
2. AI Agent has main output connections (not allowed in streaming!)
3. Target of Chat Trigger is not AI Agent

Solutions:
// 1. Enable streaming on Chat Trigger
{
  type: "updateNode",
  nodeName: "Chat Trigger",
  updates: {"parameters.options.responseMode": "streaming"}
}

// 2. Remove AI Agent main outputs
{
  type: "removeConnection",
  source: "AI Agent",
  target: "Any Output Node"
}
```

## 📚 Reference Quick Links

### Essential Documentation:

  - `tools_documentation()` - Overview of all MCP tools
  - `tools_documentation({topic: "ai_agents_guide"})` - Complete AI Agent guide
  - `tools_documentation({topic: "javascript_code_node_guide"})` - JavaScript patterns
  - `tools_documentation({topic: "python_code_node_guide"})` - Python patterns

### Node Discovery:

  - `search_nodes({query, includeExamples: true})` - Search with real examples
  - `list_nodes({category, limit})` - Browse by category
  - `get_database_statistics()` - Node inventory stats

### Configuration:

  - `get_node_essentials({nodeType, includeExamples: true})` - Minimal config (preferred)
  - `get_node_info({nodeType})` - Full schema (use sparingly)
  - `get_node_documentation({nodeType})` - Human-readable docs

### Validation:

  - `validate_node_minimal({nodeType, config})` - Quick required fields check
  - `validate_node_operation({nodeType, config, profile})` - Full node validation
  - `n8n_validate_workflow({id})` - Complete workflow validation
  - `n8n_autofix_workflow({id, applyFixes})` - Auto-fix common issues

### Management:

  - `n8n_create_workflow({name, nodes, connections})` - Create new
  - `n8n_update_partial_workflow({id, operations})` - Incremental updates
  - `n8n_list_workflows({limit, active})` - List all
  - `n8n_get_execution({id, mode})` - Check execution results

## 🔧 Configuration

To use this skill, configure your n8n MCP server with:
- Your n8n instance URL
- API credentials
- Appropriate timezone settings

```
Node Count: 537+ nodes available
Templates: 2,653+ community workflows
Documentation: 88% coverage
```

## 💡 Pro Tips

1.  **Always start small:** Use get\_node\_essentials first, not full schema
2.  **Validate often:** After each significant change, run validation
3.  **Use examples:** Set includeExamples=true to see real configurations
4.  **Partial updates:** Build incrementally with n8n\_update\_partial\_workflow
5.  **AI connections:** sourceOutput parameter is critical for AI flows
6.  **Error handling:** Always configure continueOnFail for production
7.  **Test executions:** Use mode="preview" first to avoid token overflow
8.  **Documentation:** Check get\_node\_documentation before get\_node\_info
9.  **Templates:** Search existing workflows before building from scratch
10. **Webhook data:** Remember .body property for webhook payloads\!

## 🎯 Success Metrics

  - 82% of users create workflows after diagnostics
  - Most common action: n8n\_update\_partial\_workflow (iterative development)
  - Typical build time: 6-14 minutes for full workflow
  - Validation reduces deployment errors by 70%+

## 📞 Related Skills

  - API Integration
  - Database Management
  - AI Agent Development
  - JavaScript/Python Programming
  - Workflow Optimization

-----

*This skill leverages the complete n8n MCP toolset with 38 available tools (22 documentation + 16 management tools). Always use the MCP tools for n8n operations rather than manual API calls.*

**Last Updated:** 2025-10-22  
**Skill Version:** 1.0  
**Maintenance:** Review quarterly or when n8n MCP updates

```
```