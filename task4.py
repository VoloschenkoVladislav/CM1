from sympy import Symbol, sin, cos, tan, ln




x, y = Symbol('x'), Symbol('y')
func = sin(x) + cos(x**2) * tan(y) + ln(x)
print('Derivative of function sin(x) + cos(x^2) * tan(y) + ln(x) is {}'.format(func.diff(x)))