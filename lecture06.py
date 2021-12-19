from SymPy import solveset, symbols, Interval, Min, Max, sqrt, sin, cos, pi
x = symbols('x')

l = int(input("Введите значение начала отрезка: "))
r = int(input("ведите значение конца отрезка: "))
f = x**2 + 4*x + 2

zeros = solveset(f, x, domain=Interval(l, r))
assert zeros.is_FiniteSet
min1 = Min(f.subs(x, left), f.subs(x, right), *[f.subs(x, i) for i in zeros])
max1 = Max(f.subs(x, left), f.subs(x, right), *[f.subs(x, i) for i in zeros])

print('max: ', max1 )
print('min: ', min1 )
