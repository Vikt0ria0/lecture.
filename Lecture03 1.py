#Задача 1
n = int(input("Введите верхнюю границу диапазона: "))
s = set(range(2, n+1))
while s:
    prime = min(s)
    print(prime, end = "\t")
    s -= set(range(prime, n+1, prime))

    
