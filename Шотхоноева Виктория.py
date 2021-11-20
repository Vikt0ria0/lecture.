print ('Номера видов тренировок:\n0 - Зарядка \n1 - Тренировка на пресс \n2 - Тренировка на спину \n3 - Тренировка на ноги \n4 - Тренировка на руки \n5 - Кардио-тренировка \n6 - Растяжка \n7 - Бег \n8 - Плавание\n')

from string import digits

number = input("Номер вида тренирови (Введите число от 0 до 8): ").strip()

result = ''

if (len(number) <= 0 or len(number) > 1) or (number[0] not in digits) or (len(number) == 2 and number[1] not in digits):
    print('Неправильный ввод. '
          'Запустите программу снова и введите число от 0 до 8')
    exit()

    
t = int(input('Сколько минут тренировки: '))

k = 0

for i in range(t):
    if number[-1] == '0':
        k += 4
        result = "Зарядка"
    if number[0] == '1':
         k += 8
         result = 'Тренировка на пресс'
    if number[0] == '2':
         k += 6.9
         result = 'Тренировка на спину'
    if number[0] == '3':
         k += 8.2
         result = 'Тренировка на ноги'
    if number[0] == '4':
         k += 5.1
         result = 'Тренировка на руки'
    if number[0] == '5':
         k += 7.6
         result = 'Тренировка на кардио-тренировка'
    if number[0] == '6':
         k += 4.5
         result = 'Тренировка на растяжка'
    if number[0] == '6':
         k += 10
         result = 'Бег'
    if number[0] == '7':
         k += 10.3
         result = 'Плавание' 
print('(На массой человека 65 кг.) Сожжено около {} каллорий: '.format(k))
      





