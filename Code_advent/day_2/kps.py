from pathlib import Path

data = Path("Code_advent\\day_2\\guide.txt").read_text()
lista = []
for i in data:
    stripped_lines = i.strip()
    lista.append(stripped_lines)

my_points = 0
for i in lista:
    if i == "A":
        for k in lista:
            if k == "X":
                my_points += 4
                lista.remove(k)
                break
            elif k == "Y":
                my_points += 8
                lista.remove(k)
                break
            elif k == "Z":
                my_points += 3
                lista.remove(k)
                break
    elif i == "B": 
        for k in lista:
            if k == "X":
                my_points += 1
                lista.remove(k)
                break
            elif k == "Y":
                my_points += 5
                lista.remove(k)
                break
            elif k == "Z":
                my_points += 9
                lista.remove(k)
                break       
    elif i == "C":
        for k in lista:
            if k == "X":
                my_points += 7
                lista.remove(k)
                break
            elif k == "Y":
                my_points += 2
                lista.remove(k)
                break
            elif k == "Z":
                my_points += 6
                lista.remove(k)
                break

print(my_points)

            


    
