import pandas as pd

seasons_1_20 = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)')

print(len(seasons_1_20)) 
