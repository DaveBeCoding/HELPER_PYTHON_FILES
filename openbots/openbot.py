"""OpenBot

Returns:
    AI Terminal Assistant: "Hey OpenBot" helps with daily tasks.

"""
from os import system, name
import openkeys as keys
import subprocess 
import keyboard
import openai
import sys

PROMPT_USER = f" \n****** Enter your question, type exit to quit *****\n-> "
MODEL_ENGINE = "text-davinci-002"
MAX_TEMPERATURE = 0b1 / 0b10
UNIX_SYS_CLEAR = 'clear()'
MAX_TOKEN = 0b10000000000
DUNDER_MODE = "__main__"
RETURN_0 = "exit()"
SYSTEM_C = 'clear'
MAX_START = 0b0
STOP = 0b11
MAX_N = 0b1

class OpenBot:
    def __init__(self, api_key, 
                    model_engine) -> None:
        self.api_key = api_key
        self.model_engine = model_engine
        openai.api_key = self.api_key
        
    def generate_response(self, prompt, max_tokens=MAX_TOKEN, n=MAX_N, 
                                stop=None, temperature=MAX_TEMPERATURE) -> str:
        completions = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )
        return completions.choices[MAX_START].text
        
try:
    if __name__ == DUNDER_MODE:
        while True:
            question = input(PROMPT_USER)
            if question == RETURN_0:
                break
            elif question == UNIX_SYS_CLEAR:
                subprocess.run(SYSTEM_C)
                question = input(PROMPT_USER)
                if question == RETURN_0:
                    break
                open_bot = OpenBot(api_key=keys.keys(), 
                        model_engine=MODEL_ENGINE)
                response = open_bot.generate_response(prompt=question)
            else:
                open_bot = OpenBot(api_key=keys.keys(), 
                        model_engine=MODEL_ENGINE)
                response = open_bot.generate_response(prompt=question)
            print(response)
except:
    print(sys.exc_info())
