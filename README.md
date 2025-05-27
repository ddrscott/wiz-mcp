# Wiz MCP

A command-line tool that connects to N8N MCP servers using smolagents and LiteLLM.

## Usage

### Basic Usage

```bash
uv run main.py --n8n-api-key YOUR_API_KEY "Your message here"
```

### With Custom LLM Model

```bash
uv run main.py \
  --llm-model "ollama/llama3:latest" \
  --n8n-api-key YOUR_API_KEY \
  "Analyze my recent emails"
```

### With Custom LLM URL

```bash
uv run main.py \
  --llm-url "http://localhost:8080" \
  --llm-model "gpt-4o-mini" \
  --n8n-api-key YOUR_API_KEY \
  "Help me organize my inbox"
```

### With Custom N8N SSE URL

```bash
uv run main.py \
  --n8n-sse-url "https://your-n8n.domain.com/mcp/gmail-v2/sse" \
  --n8n-api-key YOUR_API_KEY \
  "What are my unread emails?"
```

### Full Configuration

```bash
uv run main.py \
  --llm-model "ollama/gemma3:latest" \
  --llm-url "http://localhost:11434" \
  --n8n-sse-url "https://n8n.example.com/mcp/gmail-v2/sse" \
  --n8n-api-key YOUR_API_KEY \
  --temperature 0.2 \
  "Draft a response to my latest email from John"
```

## Options

- `--llm-model`, `-m`: The model to use for the agent (default: `ollama/gemma3:latest`)
- `--llm-url`, `-u`: The base URL for the LLM API (default: `http://localhost:11434`)
- `--n8n-sse-url`, `-s`: The SSE URL for the MCP server (default: `https://n8n.example.com/mcp/gmail-v2/sse`)
- `--n8n-api-key`, `-k`: The API key for N8N (required)
- `--temperature`, `-t`: The temperature for the LLM model (default: `0.1`)

## Environment Variables

You can also set the N8N API key as an environment variable:

```bash
export N8N_API_KEY="your-api-key-here"
uv run main.py --n8n-api-key "$N8N_API_KEY" "Your message"
```
