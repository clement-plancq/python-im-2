# -*- coding: utf-8 -*-

"""
Exo sur output treetagger
"""

import argparse

class Word:
    """ Classe Word : définit un mot simple de la langue """
    def __init__(self, form, lemma, pos):
        self.form = form
        self.lemma = lemma
        self.pos = pos
    
    def __repr__(self):
        return f"{self.form}"
    
    def brown_string(self):
        return f"{self.form}/{self.lemma}/{self.pos}"
    
    def is_inflected(self):
        """
        Returns True is the word is inflected
        False otherwise
        """
        if self.form.lower() != self.lemma:
            return True
        else:
            return False
def main():
    parser = argparse.ArgumentParser(description="Exo output treetagger")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("file", help="le fichier tsv")
    args = parser.parse_args()

    words = []
    with open(args.file) as tt:
        for line in tt:
            line = line.rstrip()
            items = line.split('\t')
            words.append(Word(items[0], items[2], items[1]))
    
    res = [w for w in words if w.is_inflected() and w.pos != "PUN"]
    print(res)

if __name__ == "__main__":
    main()