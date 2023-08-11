import pandas as pd 
import os


# Avaa KIINTEIDEN SIJAINTIEN tiedoston sekä lajittelee Nimiketunnuksen mukaan
curr_dir = os.path.dirname(os.path.realpath(__file__))

try:
    df1 = pd.read_excel(os.path.expanduser(curr_dir + "\\Fixed product locations.xlsx"), engine="openpyxl")
    df1.sort_values(by = "Item number")
except FileNotFoundError:
    print("ENG:Ei voitu avata 'Fixed product locations.xlsx' tiedostoa. Onko se nimetty oikein ja samassa sijainnissa .py tiedoston kanssa?")
    quit()
except KeyError:
    df1 = pd.read_excel(os.path.expanduser(curr_dir + "\\Fixed product locations.xlsx"), engine="openpyxl")
    df1.sort_values(by = "Nimiketunnus")
# Avaa VAPAUTETTUJEN TUOTTEIDEN tiedoston sekä lajittelee Nimiketunnuksen mukaan
try:
    df2 = pd.read_excel(os.path.expanduser(curr_dir + "\\Items.xlsx"), engine="openpyxl")
    df2.sort_values(by = "Item number")
except FileNotFoundError:
    print("FI:Ei voitu avata 'Items.xlsx' tiedostoa. Onko se nimetty oikein ja samassa sijainnissa .py tiedoston kanssa??")
    quit()
except KeyError:
    df2 = pd.read_excel(os.path.expanduser(curr_dir + "\\Items.xlsx"), engine="openpyxl")
    df2.sort_values(by = "Nimiketunnus")   

# Yhdistää molemmat tiedostot yhteen -> output.xlsx tiedostoon 

try:
    df3 = pd.merge(df1, df2, on = "Item number", how = "inner")
except KeyError:
    df3 = pd.merge(df1, df2, on = "Nimiketunnus", how = "inner")

try:
    Item_number = df3["Item number"]
except KeyError:
    Nimike = df3["Nimiketunnus"]
# else:
#     Nimike = df3["Nimiketunnus"]

try:
    df3["Item number"] = df3["Product number"] + ";" + df3["Item number"] + ";" + df3["Location"] 
    df3["Käännetty"] = df3["Location"] + ";" + Item_number + ";" + df3["Product number"]  
    df3.drop(columns=["Location", "Product number", "Product name_x", "Site", "Warehouse", "Product name_y", "Search name", "Product type", "Product subtype"], axis = 1, inplace=True)
    df3.to_excel(curr_dir + "\\output.xlsx", sheet_name="Remote")
except:
    df3["Nimiketunnus"] = df3["Hae nimellä"] + ";" + df3["Nimiketunnus"] + ";" + df3["Sijainti"] 
    df3["Käännetty"] = df3["Sijainti"] + ";" + Nimike +  ";" + df3["Hae nimellä"]
    df3.drop(columns=["Tuotteen nimi_x", "Toimipaikka", "Varasto", "Sijainti", "Tuotteen nimi_y", "Hae nimellä", "Tuotetyyppi", "Tuotteen alatyyppi", "Tuotedimension ryhmät", "Tuotteen elinkaaren tila"], axis = 1, inplace=True)
    df3.to_excel(curr_dir + "\\output.xlsx", sheet_name="Remote")


# Näyttää terminaalissa 10 riviin asti syötteenä 

results = df3.iloc[:10]
print(results)
print("output.xlsx tiedosto luotu")
