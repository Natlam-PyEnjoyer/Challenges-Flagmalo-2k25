# Flag'Malo 2025

## Qui-veut-gagner-des-millions

> ### Misc - Facile

---

### Solution

#### 1 - Trouver le numéro 

L'indice pour trouver le numéro était : `Le numéro à appeler est composé d'un nombre x de chiffres avec x compris entre 2 et 6, la somme des chiffres qui le composent fait 8 et le produit fait 10.`
En voyant ça, on comprend qu'il va falloir réfléchir un peu plus que pour `Communication-Established`. 2 Solutions :
- `GOAT-WAY` : Faire les calculs à la main ou à l'aide d'une calculatrice : 
  - 2 Chiffres : pas de possibilités
  - 3 chiffres : des possibilités avec `{2,5,1}` ex : `125 152 215 251 ...`
  - 4 chiffres : pas de possibilités
  - 5 chiffres : pas de possibilités
  - 6 chiffres : pas de possibilités
  - **Donc en tout, il y avait (3!)/((3-3)!) possibilités soit 6 possiblités, raisonnable à tester manuellement**
  - Voir cours combinatoire pour la théorie mathématique : [Combinatoire](https://www.maths-et-tiques.fr/telech/20Combi.pdf)
    - _Pour ce problème, voir la partie sur les k-uplets d'éléments distincts dans un ensemble fini à n éléments._
- `SHAME-WAY` : Demander à Chat GPT de résoudre ce problème : 
  - Pour la science, j'ai testé pour voir ce qu'il me réponderait :
    - Prompt : 
      - _Pourrais-tu résoudre l'énigme suivante, je n'ai pas la force d'essayer de trouver par mes propres moyens : 
      "Le numéro à appeler est composé d'un nombre x de chiffres avec x compris entre 2 et 6, la somme des chiffres qui le composent fait 8 et le produit fait 10"_
    - Réponse : 
      - [Réponse Chat GPT](./chat_gpt.md)
  - Il suffit ensuite comme pour la méthode précédente de tester tous les numéros possibles.

Le bon numéro était le ___521___

---

#### 2 - Comprendre ce qu'il se cache derrière ce numéro

Ce qui se cache derrière ce numéro, c'est un enchaînement de SVI (Lien pour comprendre ce qu'est un SVI : [SVI-Definition](https://www.napsis.fr/telephonie-ip/serveur-vocal-interactif-svi/)) pour faire une sorte de QCM avec des questions en lien avec le LORE de l'évènement.
Il y a 6 questions, 4 réponses possibles par question, ce qui équivaut 6^4^ possibiltés soit 4096 possibilités et une seule menant au flag. Vu qu'il était mal paramètré, aucun moyen d'envoyer un message avant la fin de la lecture des options donc une tentative prenait 3 minutes.
Impossible à brute force.

**PROBLEME :** Toutes les réponses des questions liées au LORE pas disponible aux joueurs le jour de l'évènement. Pour éviter qu'il soit infaisable, demande d'une des réponses trouvable le jour J pour avoir les réponses aux questions du SVI.

---

#### 3 - Récupérer le flag

Même principe que pour le flag de `Communication-Established`, un message AGI à la fin pour te dire si tu as réussi ou non et si c'est le cas, flag donné à l'oral.
Pour éviter d'avoir à faire la manip plusieurs fois, il est possible de lancer une capture `Wireshark` pour pouvoir réécouter l'appel à tout moment.
Avec ce message récupéré, il suffit de suivre la consigne à savoir : 
  - `mots et/ou nombres séparés par des underscores : **_** et les mots sont en minuscule`

---

#### Réponse attendue : 

`FMCTF{c_est_votre_dernier_mot_7621}`



