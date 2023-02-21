import os
import subprocess
import keyboard
import openai
import sys
import openkeys as keys

PROMPT_USER = "\n****** Enter your question, type exit to quit *****\n-> "
MODEL_ENGINE = "text-davinci-002"
MAX_TOKEN_LENGTH = 1024
STOP_CHARACTERS = ["\n"]
MAX_N = 1

class OpenBot:
    def __init__(self, api_key, model_engine):
        self.api_key = api_key
        self.model_engine = model_engine
        openai.api_key = self.api_key
        
    def generate_response(self, prompt, max_tokens=MAX_TOKEN_LENGTH, n=MAX_N, stop=STOP_CHARACTERS, temperature=0.5):
        completions = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )
        return completions.choices[0].text
        
if __name__ == "__main__":
    try:
        while True:
            question = input(PROMPT_USER)
            if question == "exit()":
                break
            elif question == "clear()":
                subprocess.call("clear", shell=True)
                continue
            open_bot = OpenBot(api_key=keys.keys(), model_engine=MODEL_ENGINE)
            response = open_bot.generate_response(prompt=question)
            print(response)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
