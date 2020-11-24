# -*- coding: utf-8 -*-

"""
Correction de l'évaluation du 18 novembre 2020
https://clement-plancq.github.io/python-im-2/evaluation/
"""

import argparse
import csv
from collections import Counter, defaultdict
import exo_conllu


def conllu(input_file):
    """
    La partie sur le fichier conllu
    """
    # parsing
    sents = []
    sent = exo_conllu.Sentence()
    with open(input_file) as conllu_file:
        for line in conllu_file:
            line = line.rstrip()
            if line == "":  # ligne vide pour une fin de phrase
                if len(sent) > 0:
                    sents.append(sent)
                    sent = exo_conllu.Sentence()
            elif line.startswith("# sent_id"):
                sent.id = line[len("# send_id = "):]
            elif line.startswith("# text"):
                sent.text = line[len("# text = "):]
            elif line[0].isdigit():
                sent.add_word(line)
        # En cas de fichier qui ne termine pas par une ligne vide
        if len(sent) > 0:
            sents.append(sent)

    print("\n--- Conllu ---")

    #  Question 1 : combien de phrases, combien de tokens
    nb_tokens = 0
    for sent in sents:
        nb_tokens += len(sent.words)
    print("Question 1")
    print(f"\tLe fichier contient {len(sents)} phrases et {nb_tokens} tokens.")

    # Question 2 : nb de tokens par POS
    tok_pos = Counter()
    for sent in sents:
        for w in sent.words:
            tok_pos[w.upos] += 1
    print("Question 2 : nombre de tokens par POS")
    for it, nb in tok_pos.most_common():
        print(f"\t{it} ({nb})")

    # Question 3 : tête avec au moins 3 régis
    print("Question 3 : les tokens qui sont la tête d'au moins trois autres tokens")
    for sent in sents:
        heads = defaultdict(list)  # dictionnaire head : liste des régis
        for w in sent.words:
            heads[w.head].append(w.id)
        for it in heads:
            if len(heads[it]) > 2:
                if it == "_":  # cas particulier des articles contractés (head = _)
                    print(f"\t{sent.id} {it} ({','.join(heads[it])})")
                else:
                    form = sent.words[int(it) - 1]
                    print(f"\t{sent.id} {it} {form} ({','.join(heads[it])})")


def titres_pretes(input_file):
    """
    La partie sur les titres
    """
    titres = []
    with open(input_file) as data:
        reader = csv.DictReader(data, delimiter=";")
        for row in reader:
            titres.append(row)

    print("--- Titres ---")
    # Question 1
    print(f"Question 1 : {len(titres)} titres listés")

    # Question 2
    print("Question 2 : types de document")
    types = Counter()
    for item in titres:
        types[item["Type de document"]] += int(
            item["Nombre de prêt total"]
        )  #  Mais 'Prêts' c'est bon aussi
    for item, nb in types.most_common():
        print(f"\t{item} : {nb}")

    # most_common() c'est tellement bien. Mais vous pouviez faire autrement :
    # version avec get
    #for item in sorted(types, key=types.get, reverse=True):
    #    print(f"\t{item} : {types[item]}")

    # version avec fct lambda (celle que vous trouvez en premier sur le net ;-))
    #for item, nb in sorted(types.items(), key=lambda t: t[1], reverse=True):
    #    print(f"\t{item} : {nb}")

    # Question 3 jeunesse / pas jeunesse
    nb_jeunesse = len([it for it in titres if "jeunesse" in it["Type de document"]])
    # ou bien
    # for item in titres:
    #    if "jeunesse" in item['Type de document']:
    #        nb_jeunesse += 1
    print("Question 3 : jeunesse / pas jeunesse")
    print(f"\t jeunesse : {nb_jeunesse}")
    print(f"\t pas jeunesse : {len(titres) - nb_jeunesse}")

    # Question 4
    prets_2017 = Counter()
    for item in titres:
        prets_2017[item["Titre"]] += int(item["Nombre de prêts 2017"])
    print("Question 4 : prêts 2017")
    for it, nb in prets_2017.most_common(10):
        print(f"\t{it} ({nb})")


def main():
    parser = argparse.ArgumentParser(description="Eval")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("titres", help="le fichier titres")
    parser.add_argument("conllu", help="le fichier conllu")
    args = parser.parse_args()

    titres_pretes(args.titres)
    conllu(args.conllu)


if __name__ == "__main__":
    main()
