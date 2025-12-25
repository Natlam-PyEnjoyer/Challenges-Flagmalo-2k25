# Flag'Malo 2025

## PunkRev

> ### Prog - Facile

---

### Solution

#### 1 - Lire le code et essayer de comprendre son utilisation/fonctionnement

Il y a 2 points importants à voir dans les fichiers Java de ce challenge : 
- Des listes de `byte`
- L'utilisation de fonctions sur l'entrée utilisateur et sur ces chaines de `byte`
  - Utilisateur : 
    - Cyberchain (fonction mère) suivie de quatres fonctions filles : 
      - neuroShift -> ghostInject -> datastreamMorph -> nanoModulate (dans cet ordre précis)
    - Ces fonctions enchainés permette de coder la chaine de caractère donnée en entrée (input utilisateur)
  - Chaines de `byte`
    - VaultPayload (Cette fonction permet de retourner un string à partir d'une liste de `byte`)

---

#### 2 - Faire en sorte d'inverser le chiffrement avec son propre code

Maintenant qu'on a compris comment fonctionne l'encodage, on va faire en sorte de décoder les listes de `byte`
Pour cela, on va faire les opérations dans le sens inverse, avec le langage de programmation dans lequel on est le plus à l'aise, par exemple, en python : [Décodage-Python](./solve.py) -> (fichier possible de solve avec des commentaires pour explication)

---

#### 3 - Trouver le bon flag parmi ceux que l'on a trouvé

Deux techniques possibles après avoir trouvé les chaines décodées : 
- Le BRUTFORCE, tester toutes les combinaisons sachant qu'il y en a une qui va marcher
- L' ANALYSE, voir dans le code punkrev que le code utilisé pour débloquer le mécanisme est le troisième code (Ch4rs), au niveau du test de finalSolutionToLive et que le reste, c'est juste du vent pour essayer d'embrouiller les gens.

---

#### Réponse attendue : 

`FMCTF{Try_Rev_eFbDa}`
