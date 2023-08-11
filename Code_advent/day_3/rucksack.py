from pathlib import Path
from string import ascii_letters
data = Path("Code_advent\\day_3\\rucksacks.txt").read_text()

# full str list
z = data.split()
totalsum = 0

for i in z: # Fill list with int
    divide = len(i) // 2
    left = set(i[:divide])
    right = set(i[divide:])
    
    for prio, char in enumerate(ascii_letters):
        if char in left and char in right:
            totalsum += prio + 1 

    
print(totalsum)








