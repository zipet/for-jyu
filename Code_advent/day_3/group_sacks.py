from pathlib import Path
from string import ascii_letters
data = Path("Code_advent\\day_3\\group_sacks.txt").read_text()

# full str list
z = data.split()
j = 3
totalsum = 0
for i in range(0, len(z), 3):
    joinList = z[i:j]
    j += 3

    for prio, char in enumerate(ascii_letters):
        if char in joinList[0] and char in joinList[1] and char in joinList[2]:
            totalsum += prio + 1 
print(totalsum)

