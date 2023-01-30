import sys
import openai
import openkeys as keys
from os import system, name

MAX_TEMPERATURE = 0b1 / 0b10
MAX_TOKEN = 0b10000000000
STOP = 0b11
MAX_N = 0b1

class OpenBot:
    def __init__(self, api_key, model_engine) -> None:
        self.api_key = api_key
        self.model_engine = model_engine
        openai.api_key = self.api_key
    
    def clear(self) -> None: # system agnostic 
        if(name == 'nt'):
            _ = system('cls')
        else:
            _ = system('clear')
        
    def generate_response(self, prompt, max_tokens=MAX_TOKEN, n=MAX_N, stop=None, temperature=MAX_TEMPERATURE) -> str:
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
    if __name__ == "__main__":
        while True:
            open_bot = OpenBot(api_key=keys.keys(), model_engine="text-davinci-002")
            question = input(f" \nEnter your question, type exit to quit -> ")
            if question == "exit":
                break
            response = open_bot.generate_response(prompt=question)
            print(response)
except:
    print(sys.exc_info())