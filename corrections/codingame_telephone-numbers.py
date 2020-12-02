import sys
import math

#https://www.codingame.com/ide/puzzle/telephone-numbers

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
"""
Version 1. Avec le code vu en cours sur les tries.
Dans la Classe Trie on a supprimé ce dont on avait pas besoin
Ajout d'un attribut length pour compter le nb de nœuds
"""

class Node:
    """
    Un nœud de trie. Il a un caractère et des nœuds enfants (vide à l'initialisation)
    """
    def __init__(self, char):
        self.value = char
        self.children = {}
        self.end = False

class Trie:
    """
    trie
    """
    def __init__(self):
        """
        À l'initialisation on a juste un nœud racine vide
        """
        self.root = Node("")
        self.length = 0
    
    def insert(self, word):
        """
        Un nouveau mot dans le trie
        """
        node = self.root
        
        # on parcourt car. par car.
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # Si un caractère du mot est inconnu
                # on ajoute un nouveau nœud
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
                self.length += 1
        node.end = True


annuaire = Trie()
n = int(input())
for i in range(n):
    telephone = input()
    annuaire.insert(telephone)

print(annuaire.length)



"""
Version 2. Un peu de la triche ok.
Le jeu ne demande que le nb d'éléments stockés. Même pas 
besoin de stocker les numéros pour passer les tests.
"""

annuaire = set()
n = int(input())
for i in range(n):
    telephone = input()
    for j in range(1, len(telephone)+1):
        annuaire.add(telephone[:j])

print(len(annuaire))