from sympy.solvers import solve
from sympy import Symbol




x = Symbol('x')
y = solve(x**3 + 3*x**2 - 10*x , x)
print('Solutions of x^3 + 3x^2 - 10x are {}'.format(y))