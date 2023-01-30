import sys
import openai
import openkeys as keys
from os import system, name

MAX_TEMPERATURE = 0b1 / 0b10
MAX_TOKEN = 0b10000000000
DUNDER_MAIN = "__main__"
PROMPT_USER = f" \nEnter your question, type exit to quit -> "
MODEL_ENGINE = "text-davinci-002"
RETURN_0 = "exit"
WINDOWS_SYS = 'nt'
WINDOWS_SYS_CLEAR = 'cls'
UNIX_SYS_CLEAR = 'clear'
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
            _ = system('cls')
        else:
            _ = system('clear')
        
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
        return completions.choices[0b0].text

try:
    if __name__ == DUNDER_MAIN:
        while True:
            open_bot = OpenBot(api_key=keys.keys(), 
                        model_engine=MODEL_ENGINE)
            question = input(PROMPT_USER)
            if question == RETURN_0:
                break
            response = open_bot.generate_response(prompt=question)
            print(response)
except:
    print(sys.exc_info())