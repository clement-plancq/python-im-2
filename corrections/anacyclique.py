# -*- coding: utf-8 -*-

"""
Exo sur les anacycliques avec timeit
Trouver tous les anacycliques dans les données de lexique.org
"""

import csv
import timeit
import argparse

def find_anacycliques(words):
    """
    Trouve les anacycliques dans les données passées en paramètre
    words est une séquence (peut être list, dict ou set)
    """
    res = []
    for word in words:
        if word[::-1] in words:
            res.append((word, word[::-1]))
    return res

def main():
    parser = argparse.ArgumentParser(description="Trouver les anacycliques dans le fichier lexique.org")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("file", help="le fichier tsv")
    args = parser.parse_args()
    input_file = args.file

    global words
    words = {}
    with open(input_file) as lexique:
        reader = csv.DictReader(lexique, delimiter='\t')
        for row in reader:
            words[row['ortho']] = ""
    
    print(find_anacycliques(words))
    #print(timeit.timeit('find_anacycliques(words)', globals=globals(), number=1000))


if __name__ == "__main__":
    main()