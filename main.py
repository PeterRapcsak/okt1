
szamok = [85, 92, 47, 78, 95, 88, 76, 82, 90, 85, 45, 79, 91, 88, 84, 77, 93, 86, 60, 80, 89, 94, 87, 65]

data = [[],[],[],[],[]]

for szam in szamok:
    if 90 <= szam <= 100:
        data[4].append(szam)
    elif 80 <= szam <= 89:
        data[3].append(szam)

print(data)
print(len(data[3]))

