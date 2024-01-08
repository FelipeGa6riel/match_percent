import time
import pandas as pd
from metric_between import metric_between

start = time.time()
# Read in the data
df = pd.read_excel("./data/DADOS_CENTRO_2023_JAN_OUT.xlsx")

glossary = ["Sexual", "Patrimonial", "Física",
            "Psicológica", "Emocional", "Moral"]

words_incorrect = []
len_ = []

for words in df["tipologia da violencia"]:
    if "/" in words:
        words = words.split("/")
        words_incorrect.extend(words)
        len_.append(len(words))
    else:
        words_incorrect.append(words)
        len_.append(1)
# df = df.reindex(range(63))
# função de match
df["match"] = metric_between(words_incorrect, glossary, len_)

print(df[["tipologia da violencia", "match"]].to_string())
# teste

end = time.time()

print(f">>>>>>>>>>>Runtime is: {end - start : 0.2f}")
