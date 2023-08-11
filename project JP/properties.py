def setFx_x(fx_x):
    dictVoima = {}
    count = 1
    for i in range(fx_x):
        voima = float(input(f"arvo voimalle fx_{i+1}: "))
        dictVoima[f"fx_{count}"] = voima
        count += 1
    return dictVoima

def setLx(lx):
    dictLength = {}
    count = 1
    for i in range(lx):
        pituus = float(input(f"arvo voiman pituudelle lx_{i+1}: "))
        dictLength[f"lx_{count}"] = pituus
        count += 1
    return dictLength

