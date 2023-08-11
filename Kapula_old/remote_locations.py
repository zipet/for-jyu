import pandas as pd 
import os


# Avaa sekä lajittelee kiinteät sijainnit ja vapautetut tuotteet 
try: 
    df1 = pd.read_excel(os.path.expanduser("Fixed product locations.xlsx"), engine="openpyxl")
    df1.sort_values(by = "Item number")
except FileNotFoundError:
    print("Ei voitu avata 'Fixed product locations.xlsx' tiedostoa. Onko se nimetty oikein?")
    quit()
try:
    df2 = pd.read_excel(os.path.expanduser("Items.xlsx"), engine="openpyxl")
    df2.sort_values(by = "Item number")
except FileNotFoundError:
    print("Ei voitu avata 'Items.xlsx' tiedostoa. Onko se nimetty oikein?")
    quit()    


# Yhdistää molemmat tiedostot yhteen -> output.xlsx tiedostoon 

df3 = pd.merge(df1, df2, on = "Item number", how = "inner")
Item_number = df3["Item number"]
df3["Item number"] = df3["Item number"] + ";" + df3["Location"] + ";" + df3["Product number"]
df3["Käännetty"] = df3["Product number"] + ";" + df3["Location"] + ";" + Item_number
df3.drop(columns=["Location", "Product number", "Product name_x", "Site", "Warehouse", "Product name_y", "Search name", "Product type", "Product subtype"], axis = 1, inplace=True)
df3.to_excel("output.xlsx", sheet_name="Remote")


# Näyttää terminaalissa 10 riviin asti syötteenä 

results = df3.iloc[:10]
print(results)
