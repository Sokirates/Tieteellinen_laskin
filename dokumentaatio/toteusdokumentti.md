# Toteutusdokumentti

## Ohjelman yleisrakenne
Ohjelma on tieteellinen laskin, joka käyttää shunting yard algoritmia.
Algoritmi muuntaa infix-merkintäisen lausekkeen postfix-merkintäiseen, joka on laskettavissa 
yksinkertaisesti pinon avulla. Ohjelma tukee peruslaskutoimituksia (yhteen-, vähennys-, 
kerto- ja jakolasku), eksponenttilaskentaa, neliöjuurilaskentaa, sulkeiden käsittelyä sekä 
trigonometrisiä funktioita. Ohjelmalla voi myös tallentaa muuttujia, joita voi käyttää 
seuraavissa lausekkeissa.

## Saavutetut aika- ja tilavaativuudet
Käytämme shunting yard algoritmiä, joka toimii O(n) aikavuudessa.
Tilavaativuus on myös O(n), koska pinojen koko kasvaa syötteen koon mukaan.

## Työn mahdolliset puutteet ja parannusehdotuksetUusien 
- Funktioiden lisääminen: Koodiin voisi lisätä erilaisia laskentafunktioita, kuten
min, max ja log.

-Koodin selkeyden parantaminen ja refaktorointi: Tiedostossa index.py on edelleen muuttujien 
hallintaan liittyvää toiminnallisuutta, vaikka tarkoitukseen on eriytetty tiedosto 
variable_manager.py. Tämä toiminnallisuus olisi hyvä siirtää variable_manager.py
puolelle, jolloin index.py voisi keskittyä ydintoimintoihin ja koodin rakenne selkeytyisi.

- Muuttujien arvojen käsittely: Jos muuttujalle tallennetaan uusi arvo, vanha arvo korvautuu 
nykyisellään automaattisesti ilman varoitusta.

## Laajojen kielimallien käyttö
Kehityksessä ei olla käytetty laajoja kielimalleja.

## Viitteet
- Wikipedia (2024): https://en.wikipedia.org/wiki/Shunting_yard_algorithm
- Wikipedia (2024): https://en.wikipedia.org/wiki/Reverse_Polish_notation
