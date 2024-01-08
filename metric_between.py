from thefuzz import fuzz
from unidecode import unidecode


def metric_between(data_incorrect, glossary, len_s=None):
    """
    This function is used to compare the data_incorrect with the glossary
    :param data_incorrect: List of words that are not in the glossary
    :param glossary: List of words that are in the glossary
    :return: List of tuples with the word and the score
    """

    match_between = [[(y, x, fuzz.WRatio(unidecode(y.lower()), unidecode(x.lower()))) for x in glossary] for y in data_incorrect]
    match = []

    for list_words in match_between:
        tuple_valor = max(list_words, key=lambda item: item[-1])
        max_valor = tuple_valor[-1]

        if max_valor > 65:
            match.append(tuple_valor[1])
        if max_valor <= 65:
            match.append(tuple_valor[0])

    indice = 0
    groups = []

    for i in len_s:
        grupo = []
        for _ in range(i):
            grupo.append(match[indice])
            indice += 1
        groups.append("/".join(grupo))

    return groups
