# Flag'Malo 2025

## Communication-Established

> ### Misc - Intro

---

### Solution

#### 1 - Installer/Configurer un softphone sur machine physique ou VM en mode accès par pont

Voir le fichier pdf pour la procédure d'installation et configuration d'un softphone (twinkle sous linux (Debian), VM ou machine physique).

Pour Zoiper ou MicroSIP, l'interface de configuration demande plus ou moins les mêmes infos et les informations sont plutôt claires sur les sites officiels pour installer les logiciels sur n'importe quel OS/Distribution.

La partie 5.2 du fichier pdf est réalisé par le challmaker sur l'infra du CTF

---

#### 2 - Enregistrer son softphone

Suivant les versions et les logiciels, le softphone teste de s'enregistrer directement ou a besoin d'une interaction utilisateur (cliquer sur un bouton du type "Register" ou "Enregistrer").

---

#### 3 - Appeler le numéro demandé dans l'ennoncé

Quand on appelle le numéro demandé, on obtient le message suivant `Votre correspondant est actuellement injoignable 18654`

Pas très malin de la part du challmaker (beaucoup de personnes ont pris ce message pour un message d'erreur).

Avec ce message récupéré, il suffit de suivre la consigne à savoir : 
- `mots et/ou nombres séparés par des underscores : **_** et les mots sont en minuscule`

---

#### Réponse attendue : 

`FMCTF{votre_correspondant_est_actuellement_injoignable_18654}`



