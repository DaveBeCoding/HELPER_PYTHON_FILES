"""OpenBot

Returns:
    AI Assistant: "Hey OpenBot" helps with daily tasks.

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
MAX_TOKEN = 0b10000000000
WINDOWS_SYS_CLEAR = 'cls'
DUNDER_MAIN = "__main__"
UNIX_SYS_CLEAR = 'clear()'
RETURN_0 = "exit()"
WINDOWS_SYS = 'nt'
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
    
    def on_press_key(key):
        if key == keyboard.Key.ctrl_l:
            print('You Pressed CTRL+L!')
        # keyboard.on_press_key(on_press_key)

try:
    if __name__ == DUNDER_MAIN:
        while True:
            # open_bot = OpenBot(api_key=keys.keys(), 
            #             model_engine=MODEL_ENGINE)
            question = input(PROMPT_USER)
            if question == RETURN_0:
                break
            elif question == UNIX_SYS_CLEAR:
                # keyboard.on_press_key(on_press_key) # setup keyboard listener
                cmd = SYSTEM_C
                subprocess.run(cmd)
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

                # question = input(PROMPT_USER)
            # open_bot = OpenBot(api_key=keys.keys(), 
                        # model_engine=MODEL_ENGINE)
            # response = open_bot.generate_response(prompt=question)
            print(response)
except:
    print(sys.exc_info())
