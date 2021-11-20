import math
a, b = int (input ()),int (input())
if a<0 and b<0:
    print('неверно')
    exit()
while a!= 0 and b!= 0:
    if a>b:
        a%=b
    else:
        b%=a
print (math.gcd (a, b))

#print ('Введите значения')
#print ('a = ')
#a = int(input())
#if a<0:
#    print('неверно')
#    exit()
#print ('b = ')
#b = int(input())
#if b < 0:
#    print ('nеверно')
#    exit ()
#while a != 0 and b != 0:
#    if a > b:
#        a %= b
#    else:
#       b %= a
#gcd = a+b
#print(gcd)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


while True:
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        if gcd(a, b):
            print("Наибольший общий делитель чисел A и B:", gcd(a, b))
        exit(0)
    except (TypeError, ValueError) as e:
        print("Неправильно введены ")
        
