global grav
grav = 9.81 #m/^2

# Tukivoima B, Osa ratkaisu kokonaisuutta.
def voimaB(kok_pituus, fx_1, defVoimaF):
    if fx_1 > kok_pituus:
        print("vitun homo, fx_1 ei voi olla suurempi, kuin kokopituus")
        quit()          
    by = (fx_1 * defVoimaF) / kok_pituus
    return float(by)

# voimaF = m * grav * varmuuskerroin. Palkkiin vaikuttama voima
def voimaF(m, grav, varmuuskerroin):
    voimaF = m * grav * varmuuskerroin
    return voimaF

# Laskee yhteen dict arvoja
def addFx_x(**krwags):
    count = 0
    for v in krwags.values():
        count += v
    print(f"addFx_x tulos = {count}")    
        # for k, v in krwags.items():
        # print("%s = %s" % (k, v))
        