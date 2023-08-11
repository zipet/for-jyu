How to.

Avaa komentokehote kirjoittamalla "cmd" windows hakuun ja paina enter.
Tarkista Python versio kirjoittamalla "python -V". Jos tulos on 3.8 tai vanhempi, päivitä Python.
asenna kaksi python kirjastoa kirjoittamalla "pip3 install pandas" ja "pip3 install openpyxl"

Kopioi "remote_locations.py" työpöydälle tai haluamasi sijaintiin ja
lisää samaan kansioon(esim työpöytä) myös kiinteät sijainnit ja vapautetut tuotteet excel tiedostot.
Nimeä kiinteiden sijaintien excel -> "Fixed product locations" ja vapautettujen tuotteitten excel -> "Items".

Shift + oikea hiirennäppäin ja "Avaa PowerShell-ikkuna tähän" TAI 
Navigoi komentokehotteessa työpöydälle kirjoittamalla "cd desktop" tai haluamasi kansion polku.

Aja ohjelma PowerShell:ssä/komentokehotteessa kirjoittamalla "python remote_locations.py"
Ohjelman suoritettuaan näyttää ensimmäiset 20 riviä ja luo tiedoston "output.xlsx"

Ohjelma testattu Python 3.9.13 versiolla
