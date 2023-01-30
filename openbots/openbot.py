import openkeys as keys
import openai

MAX_TEMPERATURE = 0b1 / 0b10
MAX_TOKEN = 0b10000000000
MAX_N = 0b1

class OpenBot:
    def __init__(self, api_key, model_engine):
        self.api_key = api_key
        self.model_engine = model_engine
        openai.api_key = self.api_key
        
    def generate_response(self, prompt, max_tokens=MAX_TOKEN, n=1, stop=None, temperature=0.5):
        completions = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )
        return completions.choices[0].text

# Initialize class
open_bot = OpenBot(api_key=keys.keys(), model_engine="text-davinci-002")

# Response instance
question = input(f" Enter your question -> ")
response = open_bot.generate_response(prompt=question)

# Response
print(response)


'''
Loop prompt
while True:
    user_input = input("Please enter a number, or type 'exit' to quit: ")
    if user_input == "exit":
        break
    else:
        print(int(user_input)**2)
'''