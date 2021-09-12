from sympy import integrate, Symbol, init_printing, ln
from math import sin
from scipy.integrate import quad




x = Symbol('x')
res1 = integrate(x * ln(x), x)
res2, _ = quad(lambda y: sin(y) / ( y + 1 ), 0, 1)

print('Result of integrate x * ln(x): {}'.format(res1))
print('Result of integrate sin(x) / ( x + 1 ) from 0 to 1: {}'.format(res2))