# 18/11/2020 — Évaluation Langages de script, M2 IM 2020


## Consignes

  - Vous avez trois heures : 9h - 12h  
  - À 12h au plus tard, vous m'envoyez par mail un script nommé `examen_python_nom_prenom.py`  
  - Vous pouvez poser des questions dans le chat mais vous travaillez seule.

## Sujet

Vous travaillerez sur deux fichiers :
  - [les-titres-les-plus-pretes.csv](les-titres-les-plus-pretes.csv) (vient de [https://opendata.paris.fr/explore/dataset/les-titres-les-plus-pretes/information/](https://opendata.paris.fr/explore/dataset/les-titres-les-plus-pretes/information/))
  - [fr_sequoia-ud-dev.conllu](../data/fr_sequoia-ud-dev.conllu) (ou pourquoi pas un fichier conllu d'une autre langue si vous préferez).

Votre script ne devra lire qu'*une seule fois* chacun de ces deux fichiers de données.



### Titres empruntés

1. Combien de titres sont listés dans ce fichier ? (1)
2. Listez les « types de documents » classés par ordre décroissant de prêts. Indiquez le type et le nombre de prêts cumulés dans votre réponse. (4)
3. Indiquez le nombre de titres classés dans un type de document "jeunesse" et le nombre de titres non jeunesse. (4)
4. Affichez les 10 titres les plus empruntés en 2007. (2)

### Fichier conllu
<small>[doc format CoNLL-U](https://universaldependencies.org/format.html)</small>

1. Combien de phrases, combien de tokens dans le fichier ? (2)
2. Comptez et indiquez le nombre de tokens par POS. (2)
2. Indiquez quels sont les tokens qui sont la tête (*head*) d'au moins trois autres tokens. Vous donnerez en sortie l'identifiant de la phrase, l'identifiant du token, sa forme et entre parenthèses les ids des tokens régis. (6)  
Exemple de sortie :  
`annodis.er_00014 4 changé (2,3,6,15,34)`

