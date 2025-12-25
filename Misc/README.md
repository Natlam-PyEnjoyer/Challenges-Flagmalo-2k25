# Flag'Malo 2025

## Téléphonie

> ### Mise en place de l'infrastructure

---

Challenges fait en collaboration avec **[Boutnath](https://github.com/Butnath)**

---

### Serveur 

#### Asterisk

Mise en place d'un serveur Asterisk sur une VM du Proxmox de l'infrastructure du CTF.

[![Asterisk](./infra_telephonie/img/asterisk.png)](https://www.asterisk.org/)

### Configuration des comptes joueurs

#### pjsip.conf

**Extrait de la configuration :**

```
;===============TRANSPORT===============

[simpletrans]
type=transport
protocol=udp
bind=0.0.0.0

;===============ENDPOINT TEMPLATES===============

[endpoint-basic](!)
type=endpoint
context=internal
sub_min_expiry=1200
language=fr
disallow=all
allow=alaw
;allow=all

[auth-userpass](!)
type=auth
auth_type=userpass

[aor-single-reg](!)
type=aor
minimum_expiration=1200
max_contacts=6

;===================================================
;===============CONFIGURATION Admin===============
;===================================================

[12344321](endpoint-basic)
auth=auth12344321
aors=12344321

[auth12344321](auth-userpass)
password=FMCTF_2025_TelAdmfe5310!
username=12344321

[12344321](aor-single-reg)
max_contacts=30

;===================================================
;===============CONFIGURATION EQUIPES===============
;===================================================


;===============EXTENSION 3060=============== Equipe 1

[3060](endpoint-basic)
auth=auth3060
aors=3060

[auth3060](auth-userpass)
password=n7-?U@z9?l,9h`:
username=3060

[3060](aor-single-reg)

...
```

Fichier complet : [pjsip.conf](./infra_telephonie/conf/pjsip.conf)

### Configuration des interactions/appels

#### extensions.conf

```
[internal]

exten => 0869696969,1,Dial(PJSIP/${CALLERID(num)},1,b(header^addheader^1))
 same => n,Playback(what-is-this-melody)
 same => n,agi(googletts.agi, "Vous avez essayé de joindre : Gérard Bouchard", fr)
 same => n,Hangup()

exten => 10,1,Goto(svis,300,1)
exten => 666666,1,agi(googletts.agi, "Votre correspondant est actuellement injoignable 18654", fr)
exten => 521,1,Goto(svis,100,1)

[header]
exten => addheader,1,Set(PJSIP_HEADER(add,X-FMCTF-Flag)=FMCTF{gerard_bouchard_compose_le_0869696969})

[answers]
exten => t,1,agi(googletts.agi, "Bravo, vous connaissez le LORE sur le bout des doigts (ou vous vous êtes peut-être cassé les dents plusieurs fois sur les questions)", fr)
 same => n,agi(googletts.agi, "Voici le flag : C'est votre dernier mot 7621")
exten => f,1,agi(googletts.agi, "Dommage, vous avez au moins répondu de la mauvaise façon à une des réponses.", fr)
 same => n,agi(googletts.agi, "Vous aurez peut-être plus de chance de réussir avec un peu plus d'entraînement.", fr)

[svis]
exten => 300,1,Goto(isl,s,1)
exten => 100,1,Goto(svi,s,1)
exten => 101,1,Goto(svi1t,s,1)
exten => 102,1,Goto(svi2t,s,1)
exten => 103,1,Goto(svi3t,s,1)
exten => 104,1,Goto(svi4t,s,1)
exten => 105,1,Goto(svi5t,s,1)
exten => 201,1,Goto(svi1f,s,1)
exten => 202,1,Goto(svi2f,s,1)
exten => 203,1,Goto(svi3f,s,1)
exten => 204,1,Goto(svi4f,s,1)
exten => 205,1,Goto(svi5f,s,1)

[isl]
exten => s,1,Answer()
 same => n,Set(TIMEOUT(response)=10)
 same => n,agi(googletts.agi, "hlustaðu vandlega", is)
 same => n,Wait(4)
 same => n,agi(googletts.agi, "Stofnunarár Háskólans í Rennes", is)
 same => n,Wait(4)
 same => n,agi(googletts.agi, "Nafn forstöðumanns Háskólans í Rennes", is)
 same => n,Wait(4)
 same => n,agi(googletts.agi, "deildarnúmer Mayenne", is)
 same => n,Wait(4)
 same => n,agi(googletts.agi, "Fjöldi nemenda við Háskólann í Rennes árið 2018", is)
 same => n,Wait(4)
 same => n,agi(googletts.agi, "Fjöldi þrepa upp í, Eiffelturninn", is)
 same => n,agi(googletts.agi, "Dame de fer", fr)
 same => n,Wait(4)
 same => n,agi(googletts.agi, "Til að hlusta aftur, ýttu á 0", is)
 same => n,WaitExten()
exten => 0,1,agi(googletts.agi,"Yfirferð á valkostum",is)
 same => n,Goto(s,1)
exten => i,1,agi(googletts.agi,"Rangt val",is)
 same => n,Goto(s,1)
exten => t,1,agi(googletts.agi,"Þú átt í vandræðum með að velja, bless",is)
 same => n,Hangup()
...
```

Fichier complet : [extensions.conf](./infra_telephonie/conf/extensions.conf)


