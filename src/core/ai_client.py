import openai
import os
import json
from colorama import Fore, Style
from src.utils.config import config

class AIclient:
    def __init__(self):
        self.model = "openai/gpt-oss-120b"
        self.deepinfra_key = config().get_deepinfra_api_key()
        self.client = openai.OpenAI(
            api_key=self.deepinfra_key,
            base_url="https://api.deepinfra.com/v1/openai"
        ) 

    def ai_respond(self, prompt):
        print(f"{Style.BRIGHT}{Fore.WHITE} User question in generate_response: {Style.RESET_ALL}")
        print(f"    {Fore.CYAN} {prompt} {Style.RESET_ALL}")
        print()

        deepinfra_response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )

        print(f"{Style.BRIGHT}{Fore.WHITE} DeepInfra response: {Style.RESET_ALL}")
        print(f"    {Fore.CYAN}{deepinfra_response}{Style.RESET_ALL}")
        print()

        response_to_user = deepinfra_response.choices[0].message.content

        print(f"{Style.BRIGHT}{Fore.WHITE} AI message: {Style.RESET_ALL}")
        print(f"    {Fore.CYAN}{response_to_user}{Style.RESET_ALL}")
        print()

        return response_to_user