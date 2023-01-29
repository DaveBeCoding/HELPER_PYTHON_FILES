import openai as open
import openkeys as keys

open.api_key = keys.keys()
prompt = (f"whats at the center of the universe")

completions = open.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

print(completions.choices[0].text)

