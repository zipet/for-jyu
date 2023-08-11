data = open("C:\\Users\\aleks\\Desktop\\Projects\\Code advent\\day_1\\calories.txt", "r")
lines = data.readlines()
lista = []
for line in lines:
    stripped_lines = line.strip()
    lista.append(stripped_lines)
print(len(lista))   
add_list = []

num2 = 0  
for line in lista:
    num = 0
    if line != "":
        num = int(line)
        num2 += num
    else:
        add_list.append(int(num2))
        num2 = 0

del lista
   
add_list.sort()
print(add_list)

add_list.sort(reverse=True)

print(add_list[:3])

add = 0
for i in add_list[:3]:
    add += i

print(add)