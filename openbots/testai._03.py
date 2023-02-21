from os import system, name
import openkeys as keys
import subprocess 
import openai
import sys
import readline

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
    def __init__(self, api_key, model_engine) -> None:
        self.api_key = api_key
        self.model_engine = model_engine
        openai.api_key = self.api_key
        
    def generate_response(self, prompt, max_tokens=MAX_TOKEN, n=MAX_N, stop=None, temperature=MAX_TEMPERATURE) -> str:
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
        question_history = []  # initialize an empty list to store the history of questions asked
        while True:
            # use readline to enable up arrow key
            question = input(PROMPT_USER)
            if question == RETURN_0:
                break
            elif question == UNIX_SYS_CLEAR:
                subprocess.run(SYSTEM_C)
                continue
            elif question == "":
                try:
                    question = question_history[-1]  # get the last question asked from history
                except IndexError:
                    continue  # if history is empty, go to next iteration of loop
            else:
                question_history.append(question)  # add new question to history
                open_bot = OpenBot(api_key=keys.keys(), model_engine=MODEL_ENGINE)
                response = open_bot.generate_response(prompt=question)
            print(response)
except:
    print(sys.exc_info())
