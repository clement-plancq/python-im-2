# -*- coding: utf-8 -*-

"""
Exo sur fichier conllu pour cours POO
"""

import argparse
from dataclasses import dataclass, field

@dataclass
class Word:
    """ Word : a word in conllu format """
    id: str
    form: str
    lemma: str
    upos: str
    xpos: str
    feats: str
    head: str
    deprel: str
    deps: str
    misc: str    

    def __repr__(self):
        return self.form

    def is_inflected(self):
        """
        Returns True is the word is inflected
        False otherwise
        """
        if self.form.lower() != self.lemma:
            return True
        else:
            return False

class Sentence:
    """
    A sentence is composed of a list of Word objects, an id and a text string
    """
    def __init__(self):
        self.words = []
        self.id = ""
        self.text = ""

    def add_word(self, line):
        """
        Add a Word to the words list
        Args:
            line (str): a line of an orfeo file with a word informations
        """
        features = line.split('\t')
        if features:
            self.words.append(Word(*features))

    def __len__(self):
        return len(self.words)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.words):
            current_word = self.words[self.n]
            self.n += 1
            return current_word
        else:
            raise StopIteration

def main():
    parser = argparse.ArgumentParser(description="Exo conllu")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("file", help="le fichier conllu")
    args = parser.parse_args()

    sents = []
    sent = Sentence()
    with open(args.file) as conllu:
        for line in conllu:
            line = line.rstrip()
            if line == "": # ligne vide pour une fin de phrase
                if len(sent) > 0:
                    sents.append(sent)
                    sent = Sentence()
            elif line.startswith("# sent_id"):
                sent.id = line[len('# send_id = '):]
            elif line.startswith("# text"):
                sent.text = line[len('# text = '):]
            elif line[0].isdigit():
                sent.add_word(line)
        # En cas de fichier qui ne termine pas par une ligne vide
        if len(sent) > 0:
            sents.append(sent)
    
    print(f"Le fichier contient {len(sents)} phrases.")
    
if __name__ == "__main__":
    main()