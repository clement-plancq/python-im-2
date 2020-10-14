# -*- coding: utf-8 -*-

"""
Python M2. Cours 2 : exercices sur la liste de Swadesh des langues austronésiennes
"""

import csv
import collections


def get_austro_words(lang1, lang2, words, file="../data/austronesian_swadesh.csv"):
    """
    Exo 1
    Reçoit un couple de langues (langue1, langue2) et une liste de mots (words)
    Cherche dans la liste Swadesh des langues austronésiennes les traductions des mots
    dans ces deux langues.
    Renvoie un dictionnaire {'langue1': [w1, w2], 'langue2': [w1, w2]}
    Liste vide si la langue n'est pas répertoriée dans la liste
    """
    res = collections.defaultdict(list)
    with open(file) as swadesh:
        reader = csv.DictReader(swadesh)
        if not (lang1 in reader.fieldnames):
            res[lang1] = []
        if not (lang2 in reader.fieldnames):
            res[lang2] = []
        for row in reader:
            if row["English"] in words:
                if lang1 in row:
                    res[lang1].append(row[lang1])
                if lang2 in row:
                    res[lang2].append(row[lang2])
        return res

def same_prefix(cebuano_word, word):
    """
    Vérifie si deux mots ont le même préfixe (longueur 2 ou 3)
    Si les premières lettres sont des voyelles on les considère similaires
    """
    if cebuano_word and word:
        if cebuano_word[0] in "aeiou" and word[0] in "eaiou":
            return cebuano_word[1:2] == word[1:2]
        else:
            return cebuano_word[0:2] == word[0:2]
    else:
        return False

def find_words_same_prefix(file="../data/austronesian_swadesh.csv"):
    """
    Pour chaque mot du Cebuano de la liste Swadesh austronésienne, trouvez les mots des autres langues
    qui ont les deux ou trois premiers caractères en commun.
    (optionnel si vous voulez jouer avec les expressions régulières) Si le mot commence par une voyelle, 
    elle pourra différer dans les autres langues. Ex: isa / usa seront considérées comme similaires (i/u) 
    parce qu'à part la première lettre voyelle elles sont similaires.
    """
    res = collections.defaultdict(list)
    with open(file) as swadesh:
        reader = csv.DictReader(swadesh)
        for row in reader:
            cebuano_w = row['Cebuano']
            for lang, cell in row.items():
                if lang == 'Cebuano':
                    continue
                for word in cell.split(','):# parce qu'on a des cellules avec plusieurs mots
                    if same_prefix(cebuano_w, word):
                        res[cebuano_w].append({lang:word})
    return res

def main():
    #print(get_austro_words("Arab", "Russian", []))
    res = find_words_same_prefix()
    for cebuano_word, similars in res.items():
        print(f"{cebuano_word} -> ", end="")
        print(" | ".join([f"{w} ({lang})" for it in similars for lang, w in it.items()]), end="")
        #for it in similars:
            #for lang, w in it.items():
                #print(f"{w} ({lang})", end=" | ")
        print("")


if __name__ == "__main__":
    main()