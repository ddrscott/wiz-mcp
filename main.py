# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "smolagents[litellm,mcp]",
# ]
# ///

import click
from smolagents import MCPClient, CodeAgent, LiteLLMModel
from mcp import StdioServerParameters

@click.command()
@click.option('--llm-model', '-m', default='ollama/gemma3:latest', help='The model to use for the agent.')
@click.option('--llm-url', '-u', default='http://localhost:11434', help='The base URL for the LLM API.')
@click.option('--n8n-sse-url', '-s', default='https://n8n.localhost.com/mcp/gmail-v2/sse', help='The SSE URL for the MCP server.')
@click.option('--n8n-api-key', '-k', required=True, help='The API key for N8N.')
@click.option('--temperature', '-t', default=0.1, help='The temperature for the LLM model.')
@click.argument("messages", type=str, nargs=-1)
def main(llm_model, llm_url, n8n_sse_url, n8n_api_key, temperature, messages):
    messages = ' '.join(messages)
    server_parameters = StdioServerParameters(
        command="npx",
        args=[
          "-y",
          "supergateway",
          "--sse",
          n8n_sse_url,
          "--header",
          f"Authorization: Bearer {n8n_api_key}",
        ],
    )
    llm = LiteLLMModel(model_id=llm_model, api_base=llm_url, temperature=temperature)

    with MCPClient([server_parameters]) as tools:
        agent = CodeAgent(tools=tools, model=llm)
        agent.run(messages)

if __name__ == "__main__":
    main()
