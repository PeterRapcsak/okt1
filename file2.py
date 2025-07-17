#1. Caesar titkosító
def caesarCipher(text: str, shift: int) -> str:
    lista = []
    for betu in "abcdefghijklmnopqrstuvwxyz":
        lista.append(betu)

    result = ""
  
    for i in text:
        valami = lista.index(i)
        ujvalami = (valami + shift) % 26
        result += lista[ujvalami] #ujvalamiadik elemet hozzáadjuk a result stringhez

    return result

def main():
  x = int(input("input a number: "))
  titkositando = input("input the stuff to be encrypted: ")
  titkositott = caesarCipher(titkositando, x)
  return titkositott

print(main())