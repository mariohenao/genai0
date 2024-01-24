import sys, os
import asyncio
from dotenv import load_dotenv

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    OpenAIChatCompletion,
    AzureChatCompletion,
)
from semantic_kernel.planning.basic_planner import BasicPlanner

kernel = sk.Kernel()

useAzureOpenAI = True

load_dotenv()
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
# deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_chat_service("chat_completion",
                        AzureChatCompletion(deployment_name=deployment, 
                                            endpoint=endpoint, 
                                            api_key=api_key))

planner = BasicPlanner()

#native
sys.path.append("../plugins/native")
from operations_plugin import OpsPlugin
ops_plugin = kernel.import_plugin(OpsPlugin(), "OpsPlugin")

#semantic
custom_plugins_directory = "../plugins/semantic"
make_verse_plugin = kernel.import_semantic_plugin_from_directory(custom_plugins_directory, "VersePlugin")

idea = input("Provide some idea: ")
ask = f"""
The MH index of an idea is the result of:
1. Creating a 4 bars verse from the idea.
2. Counting the words of that 4 bars verse 
3. Computing 2 to the power of the number of words. 

Take this idea: '''{idea}''' compute its MH index
"""

async def main():
    # Assuming planner is an instance of some class that provides the async methods
    # and custom_ask and kernel are defined earlier in your script
    basic_plan = await planner.create_plan_async(ask, kernel)
    print(basic_plan.generated_plan)
    # results = await planner.execute_plan_async(basic_plan, kernel)

    # Do something with results
    # print(results)

asyncio.run(main())


