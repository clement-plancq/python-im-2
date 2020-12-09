# https://www.codingame.com/ide/puzzle/dwarfs-standing-on-the-shoulders-of-giants
# Pas facile-facile celui-là. Pour comprendre l'exécution des fonctions récursives
# utilisez http://pythontutor.com/

from collections import defaultdict

def find_max_length(relations, start, length, max):
    """
    Fonction récursive de recherche de la plus longue chaîne d'influences
    Args:
        relations: dict des relations données en input
        start: début de la chaîne (1ère personne)
        length: la taille de la chaîne courante
        max: la taille de la + grande chaîne jusqu'à présent
    """
    if start in relations:
        length += 1
        for item in relations[start]:
            max = find_max_length(relations, item, length, max)
    else:
        if length > max:
            return length
        else:
            return max
    return max

relations = defaultdict(list)
n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    relations[x].append(y)



# Write an answer using print
print(max([find_max_length(relations, item, 1, 0) for item in relations]))
