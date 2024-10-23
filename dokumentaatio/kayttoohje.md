# Ohjelman käyttöohje

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon.

Ohjelman pystyy suorittamaan komennolla:

```bash
python3 src/index.py
```

## testien suoritus

Riippuvuuksien asennus:
```bash
poetry install
```
Poetry-ympäristöön siirtyminen:
```bash
poetry shell
```
Testien suoritus:
```bash
pytest
```
Testikattavuusraportin generointi:
```bash
poetry run coverage run --branch -m pytest src; coverage html
```
