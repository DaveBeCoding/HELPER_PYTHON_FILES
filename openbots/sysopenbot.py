#! /usr/bin/python

import sys
import openai
# import argparse
import openkeys as keys
from os import system, name

PROMPT_USER = f" \n****** Enter your question, type exit to quit *****\n-> "
MODEL_ENGINE = "text-davinci-002"
MAX_TEMPERATURE = 0b1 / 0b10
MAX_TOKEN = 0b10000000000
WINDOWS_SYS_CLEAR = 'cls'
DUNDER_MAIN = "__main__"
UNIX_SYS_CLEAR = 'clear'
WINDOWS_SYS = 'nt'
RETURN_0 = "exit"
MAX_START = 0b0
STOP = 0b11
MAX_N = 0b1


# parser = argparse.ArgumentParser()

# parser.add_argument("--question", type=str, required=True, help="Pull Request Status")

# args = parser.parse_args()

# pull_request_status = args.prstatus

class OpenBot:
    def __init__(self, api_key, 
                    model_engine) -> None:
        self.api_key = api_key
        self.model_engine = model_engine
        openai.api_key = self.api_key
    
    def clear(self) -> None: # system agnostic 
        if(name == WINDOWS_SYS):
            _ = system(WINDOWS_SYS_CLEAR)
        else:
            _ = system(UNIX_SYS_CLEAR)
        
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
    if __name__ == DUNDER_MAIN:
        while True:
            open_bot = OpenBot(api_key=keys.keys(), 
                        model_engine=MODEL_ENGINE)
            question = input(PROMPT_USER)
            # questionargs = " "
            if question == RETURN_0:
                break
            response = open_bot.generate_response(prompt=question)
            print(response)
except:
    print(sys.exc_info())
#  python -m pydoc