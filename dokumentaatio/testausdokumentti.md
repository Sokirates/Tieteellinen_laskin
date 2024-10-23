# Testausdokumentti

Ohjelman yksikkötestaus on suoritettu käyttäen unittest-kirjastoa.
Testiä myös on analysoitu coverage.py-työkalulla. Testauksen tavoitteena oli varmistaa,
että ohjelma toimii oikein keskeisten funktioiden ja luokkien toimintaa eri syöteskenaariossa sekä nostaa tarkan virheilmoituksen.

## Mitä on testattu?
- syötteet eli numerot, muuttujat, operaattorit ja sulkeet käsitellään oikein
- infix-muotoiset lausekkeet muunnetaan oikeaan postfix-muotoon
- virheenkäsittelyt: nollalla jako, ylimääräset sulkeet, odottamattomat syötteet ja virheviestit palautetaan oikein.

![](https://github.com/user-attachments/assets/c7325e7b-2924-4670-985a-8d96fa4a9b35)

## Testien suoritus

```bash
poetry run coverage run --branch -m pytest src; coverage html
```
