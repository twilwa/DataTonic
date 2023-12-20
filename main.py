import json
import asyncio
<<<<<<< HEAD
from dotenv import load_dotenv
from datetime import datetime
from autogen.autogen_module import AutoGenModule
from semantic_kernel.semantic_kernel_module import SemanticKernelModule
from taskweaver.taskweaver_module import TaskweaverModule
from agent_builder import AgentBuilder
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

async def main():
    # Load environment variables from .env file
    load_dotenv()

    # Load the configuration list for different LLMs
=======
import os
from src.semantic_kernel.semantic_kernel_module import SemanticKernelDataModule
from src.taskweaver.taskweaver_module import TaskWeaverDataProcessor
from src.autogen.autogen_module import AutoGenModule

async def main():
>>>>>>> ac91e79fd632780ad30a01091b2579ef2a2240dc
    with open('OAI_CONFIG_LIST.json', 'r') as file:
        OAI_CONFIG_LIST = json.load(file)
    semantic_kernel = SemanticKernelDataModule()
    taskweaver = TaskWeaverDataProcessor()
    autogen_module = AutoGenModule(memgpt_memory_path="./src/autogen/MemGPT", openai_api_key=os.getenv('OPENAI_API_KEY'))
    autogen_module.semantic_kernel = semantic_kernel
    autogen_module.taskweaver = taskweaver

    user_input = input("Please provide a description for the task you'd like to perform, identify your objectives, a plan on how to achieve it according to you, and a list of the final results you expect: ")

    sow_document = await semantic_kernel.create_and_fetch_sow(user_input)

    executed_plan = autogen_module.AutoGenModule(sow_document)

    print(f"Executed Plan: \n{executed_plan}")

if __name__ == "__main__":
    asyncio.run(main())