import sys
import openai as open
import openkeys as keys
from os import system, name

user_input = sys.argv[1:]

open.api_key = keys.keys()
# prompt = (f"whats at the center of the universe") -> ''.join(user_input)
prompt = input(f"Enter Question for the Open Bot -> ")

completions = open.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

print(completions.choices[0].text)

# class OpenBot():
#     def __init__(self) -> None:
#         self.clear()
#         self.main_msg()

#     def clear(self) -> None: # system agnostic 
#         if(name == 'nt'):
#             _ = system('cls')
#         else:
#             _ = system('clear')




# try:
#     if __name__ == "__main__":
#         gmres = GMRES()
#         pause(STOP)
#         gmres.main()
# except:
#     system('cls') if name == 'nt' else system('clear')
#     print("...\n")
#     print("-----------------------------------------------------------------|")
#     print("ERROR, Please check your configuration                           ")
#     print("...\n                                                            ")
#     print("Install the appropriate modules as well               ")
#     print("...\n                                                            ") 
#     print("pip install :: scipy.stats,  numpy, warnings, scipy.sparse       ")
#     print("...\n                                                            ")
#     print("-----------------------------------------------------------------|")


'''
Loop prompt

while True:
    user_input = input("Please enter a number, or type 'exit' to quit: ")
    if user_input == "exit":
        break
    else:
        print(int(user_input)**2)


'''