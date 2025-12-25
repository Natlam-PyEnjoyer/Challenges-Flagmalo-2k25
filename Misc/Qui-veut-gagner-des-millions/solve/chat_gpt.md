Résolvons l’énigme étape par étape.

On cherche **un numéro composé de x chiffres**, avec **2 ≤ x ≤ 6**, tel que :

* **La somme des chiffres = 8**
* **Le produit des chiffres = 10**

---

## 🔎 Recherche des combinaisons possibles

Le produit doit être **10**, donc les chiffres doivent être choisis parmi les facteurs de 10 :

* 10 = **1 × 10** → impossible car **10 n’est pas un chiffre**
* 10 = **2 × 5**
* 10 = **1 × 2 × 5**
* 10 = **1 × 1 × 2 × 5**
* etc. (on peut rajouter des 1 sans changer le produit)

Puis on vérifie si **la somme = 8**.

### ✦ Cas minimal (2 chiffres)

* (2, 5) → somme = 7 ❌
  Aucun numéro à deux chiffres.

### ✦ Cas à 3 chiffres

Ajoutons un **1** (ne change pas le produit) :

* (1, 2, 5) → somme = 8 ✔️
  → **125** est une solution
  Toutes permutations valides : **125, 152, 215, 251, 512, 521**

### ✦ Cas à 4 chiffres

Ajoutons un deuxième **1** :

* (1, 1, 2, 5) → somme = 9 ❌
  Donc aucun numéro à 4 chiffres.

### ✦ Cas à 5 chiffres

Ajoutons un **1** de plus :
(1, 1, 1, 2, 5) → somme = 10 ❌
Pas de solution.

### ✦ Cas à 6 chiffres

Encore un **1** :
(1, 1, 1, 1, 2, 5) → somme = 11 ❌
Pas de solution.

---

## ✅ **Solutions possibles**

Les seuls numéros qui respectent toutes les conditions sont donc :

### **→ Tous les arrangements des chiffres 1, 2 et 5**

c’est-à-dire :

**125, 152, 215, 251, 512, 521**

---

Si tu veux, je peux aussi :
📞 t’aider à trouver "le bon" selon un contexte,
🔢 expliquer pourquoi il n’y en a pas d’autres,
🎲 générer l’énigme inverse, etc.
