

szam = int(input("Szam: "))

for x in range(1, szam + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz Buzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)





n = 10

fib = [0, 1]

for x in range(2, n):
    fib.append(fib[-1] + fib[-2])

print(fib)




'''
n = 10

a = 0
b = 1

for x in range(n):
    print(a)
    a, b = b, a + b

'''