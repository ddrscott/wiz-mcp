# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "qwen-agent[gui,mcp]",
# ]
# ///

import os
import json

from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI

ROOT_RESOURCE = os.path.join(os.path.dirname(__file__), 'resource')


def init_agent_service():
    llm_cfg = {
        'model': 'qwen3:14b',
        'model_server': 'https://webui.dataturd.com/api/',  # base_url, also known as api_base
        'api_key': os.environ.get('WEBUI_API_KEY', None)
    }
    system = ('You are a helpful assistant that uses N8N to help the user.')
    tools = [json.loads(open('server.json').read())]
    bot = Assistant(
        llm=llm_cfg,
        name='Nate',
        description='N8n Assistant',
        system_message=system,
        function_list=tools,
    )

    return bot


def app_gui():
    # Define the agent
    bot = init_agent_service()
    chatbot_config = {
        'name': 'Nate',
        'input.placeholder': 'What can I do for you?',
        'prompt.suggestions': [
            'Draft and email to scott@pierce.com about the meeting next week',
            'How much older is Tom Hanks than Tom Holland in days?',
            'Which teams will be in the NBA finals this year? And what are their chances of winning?',
        ]
    }
    WebUI(
        bot,
        chatbot_config=chatbot_config,
    ).run()


if __name__ == '__main__':
    app_gui()
