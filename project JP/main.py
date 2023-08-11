import math
from equations import *
from properties import *

# Varmistaa käyttäjältä, että varmuuskerroin ei ole 0 tai negatiivinen luku. 

while True:
    varmuuskerroin = float(input("Anna varmuuskerroin (Vähintään 1): "))
    if varmuuskerroin < 1:
        print("Vitun idiootti. Vähintään 1!!!")
    elif varmuuskerroin >= 1:    
        break
m = float(input("Anna paino kg: ")) # Kappaleen massa
kok_pituus = float(input("kokonaispituus: ")) # Kappaleen kokopituus tukien päällä
voimia = int(input("Monta voimaa lisäksi? ")) # Määrä voimia ja niille arvot
_fxdict = setFx_x(voimia) #setFx_x luo properties.py dictionaryn voimille.
addFx_x(**_fxdict) # TODO: tehdä tästä käytännöllinen funktio. Testinä toimivuudesta.
"""
for k, v in _fxdict.items():
    print(k,v)
"""
calcVoimaF = voimaF(m, grav, varmuuskerroin)
calcVoimaB = voimaB(kok_pituus, _fxdict["fx_1"], calcVoimaF)
Ay = calcVoimaF - calcVoimaB # Ay = Tukivoima Ay

print(calcVoimaF, "N")
print(calcVoimaB, "N")
print("Ay =",Ay, "N")
print("Mmax =",Ay * _fxdict["fx_1"], "Nm") # Mmax = Ay * Fx_1 (Nm)

