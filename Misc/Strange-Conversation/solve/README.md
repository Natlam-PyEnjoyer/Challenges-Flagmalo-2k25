# Flag'Malo 2025

## Strange-Conversation

> ### Misc - Facile

---

### Solution

#### 1 - Appeler le numéro et comprendre ce qu'il se cache derrière

L'extension attribuée à ce chall est le numéro 10. Ce qui se cache derrière ce numéro, c'est un SVI (Lien pour comprendre ce qu'est un SVI : [SVI-Definition](https://www.napsis.fr/telephonie-ip/serveur-vocal-interactif-svi/)) pour faire une sorte de rébus/charade dans une langue peu connue (en France).
**PROBLEME :** Toutes les réponses des questions liées au LORE pas disponible aux joueurs le jour de l'évènement. Pour éviter qu'il soit infaisable, demande d'une des réponses trouvable le jour J pour avoir les réponses aux questions du SVI.

---

#### 3 - Extraire l'audio pour pouvoir le traduire

Solutions pour extraire l'audio : 
Une solution (dans des conditions optimales) est de mettre son casque au niveau du micro du téléphone et laisser google traduction faire son travail. Etant donné le bruit dans la salle, cette solution n'était pas réaliste. Aucune autre solution n'avait été prévu pour le jour du CTF. 

---

Une autre solution (trouvée après coup) est de faire une capture `Wireshark` pour récupérer les `flux RTP` de l'appel. Ensuite, en lisant les flux RTP, on peut les exporter en `.wav` (du type [isl.wav](./isl_svi.wav)). Avec ce .wav, on peut l'utilise dans des transcripteurs en ligne pour récupérer un texte. 
Ne sachant pas quelle langue est utilisée, un le premier site à utiliser serait un site avec détection automatique (par exemple : [transcri](https://transcri.io/fr/transcription-audio-en-texte)) pour découvrir la langue (mettre le texte dans google traduction avec détection de langue pour le découvrir). 
Etant donné que les transcripteurs ne sont pas d'une précision chirurgicale, utiliser plusieurs outils ou plusieurs niveaux de précision d'un outil est une bonne idée. Dans mon cas, j'ai fait une transcription avec [transcri](https://transcri.io/fr/transcription-audio-en-texte) et 2 avec [turboscribe](https://turboscribe.ai/fr/dashboard) (une précise et une alliant précision et vitesse). Pour les infos des transcriptions, je les ai mis dans les fichiers suivant :
- [transcri-detectlangue](./transcriptions_traductions/transcri.md)
- [turboscribe-rapide](./transcriptions_traductions/turboscrib_precis-.md)
- [turboscribe-precis](./transcriptions_traductions/turboscrib_precis+.md)

---

#### 4 - Assembler les informations pour récupérer le flag

En recoupant toutes les informations, on a une suite d'enigme ressemblant à ça :
- Année de fondation de l'université de Rennes (l'autre n'a pas de sens)
- Nom du directeur de l'univesité de Rennes (les autres n'ont pas de sens)
- Numéro du département ou nombre de personne (dans l'audio on entend clairement le mot "Mayenne" même s'il y a un accent)
- Nombre d'étudiant de l'université de Rennes en 2000 ou 2018 ou nombre de comités de l'université de Rennes en 2008
- Nombre de marche de la Tour Eiffel (l'autre n'a pas de sens)
On se retouve donc avec des énigmes dont on est à peu près sûr et d'autres qui sont floues. Ne pouvant pas être beaucoup plus précis, il ne reste plus qu'à `BRUTFORCE`
Le flag comme les précédents est de la forme suivante : 
- `mots et/ou nombres séparés par des underscores : **_** et les mots sont en minuscule`
Donc le flag devrait ressembler à ça : `FMCTF{1460_alis_x_y_z}` avec x,y et z des valeurs qui ne sont pas fixes
Il y a 3 données qui sont trop peu précises : 
- x peut être 15 000 (nombre d'étudiants en 2000), 30630 (nombre d'étudiants en 2018), la dernière paraît trop vague, pas de résultat facile à trouver, donc on réduit x à 2 propositions
- y peut être 53 (numéro du département de la Mayenne) ou 305 437 (nombre d'habitant en Mayenne)
- z peut être 674 (nombre de marches jusqu'au 2ème étage) ou 1665 (nombre de marches jusqu'au sommet)

Les flags possibles sont donc les suivants : 
- `FMCTF{1460_alis_15000_53_674}`
- `FMCTF{1460_alis_15000_305437_674}`
- `FMCTF{1460_alis_15000_305437_1665}`
- `FMCTF{1460_alis_15000_53_1665}`
- `FMCTF{1460_alis_30630_53_674}`
- `FMCTF{1460_alis_30630_305437_674}`
- `FMCTF{1460_alis_30630_305437_1665}`
- `FMCTF{1460_alis_30630_53_1665}`

---

#### Réponse attendue : 

`FMCTF{1460_alis_53_30630_674}`



