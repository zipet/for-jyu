data = open("C:\\Users\\aleks\\Desktop\\Projects\\Code advent\\day_2\\calories.txt", "r")
lines = data.readlines()

lista = []
lista_int = []
add = 0
for line in lines:
    stripped_lines = line.strip()
    lista.append(stripped_lines) 
 
for i in lista:
    if i != "":
        num = int(i)
        lista_int.append(num)
    else:
        continue
    
del lista

lista_int.sort(reverse=True)

print(lista_int[:3])

for i in lista_int[:3]:
    add += i

print(add)

# KOODI TOIMI. MUTTA PYYDETTIIN "RYHMÄN" ELI TONTUN ARVOJA, EI YKSITTÄISIÄ :D:D:D