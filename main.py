
szo = input("Szó: ").lower()

betuk = []

for s in szo:
    betuk.append(s)

if ''.join(list(reversed(betuk))) == szo:
    print("Palindrom")
else:
    print("nem az")
