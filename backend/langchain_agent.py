from langchain.llms.base import LLM
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from typing import Any, List, Optional
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class DeepSeekWrapper(LLM):
    api_key: str
    model_name: str
    temperature: float
    api_url: str

    def __init__(self, model_name="deepseek-chat", temperature=0):
        super().__init__()
        # Initialize with parent class first
        super().__init__()
        # Then set the values
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.model_name = model_name
        self.temperature = temperature
        self.api_url = "https://api.deepseek.com/v1/chat/completions"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.temperature
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            raise Exception(f"API call failed: {str(e)}")

    @property
    def _llm_type(self) -> str:
        return "deepseek"

    @property
    def _identifying_params(self) -> dict[str, Any]:
        """Get the identifying parameters."""
        return {
            "model_name": self.model_name,
            "temperature": self.temperature
        }

# Initialize the DeepSeek wrapper
llm = DeepSeekWrapper(
    model_name="deepseek-chat",
    temperature=0
)

# Example tool for testing
def calculator(query):
    """Useful for when you need to answer questions about math"""
    try:
        return eval(query)
    except:
        return "I couldn't calculate that."

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for when you need to perform mathematical calculations"
    )
]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def generate_response(prompt):
    try:
        response = agent.run(prompt)
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"
