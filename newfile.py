def put(a, b):
    if a + b == 'CH' or a + b == 'HC':
        return 'B'
    elif a + b == 'HH':
        return 'N'
    elif a + b == 'CB':
        return 'H'
    elif a + b == 'NH' or a + b == 'HN':
        return 'C'
    elif a + b == 'HB':
        return 'C'
    elif a + b == 'NN':
        return 'C'
    elif a + b == 'BH':
        return 'H'
    elif a + b == 'NC':
        return 'B'
    elif a + b == 'NB' or a + b == 'BN':
        return 'B'
    elif a + b == 'BB':
        return 'N'
    elif a + b == 'BC':
        return 'B'
    elif a + b == 'CC':
        return 'N'
    elif a + b == 'CN':
        return 'C'

step = int(10)
x = input()
y  = []

for j in range(step):
    for i in range(len(x) - 1):
        y.append(x[i])
        y.append(put(x[i], x[i + 1]))
    y.append(x[-1])
    print('B count: ', y.count('B'), 'C count: ', y.count('C'), 'N count: ', y.count('N'), 'H count: ', y.count('H'), ' ', j + 1)
    print(' ')
    x = y
    y = []
print(x.count('B') - x.count('H'))