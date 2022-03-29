
from operator import pow, truediv, mul, add, sub, floordiv

import math

operators = {
  '+': add,
  '-': sub,
  '//': floordiv,
  '*': mul,
  '/': truediv,
  '^': pow
}

pi_e = {
'pi': math.pi,
'e': math.e
}

def calculate(s):
    try:
        x = float(s)
    except:
        pass
    else:
        return float(s)

    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            try:
                return operators[operator](calculate(left), calculate(right))
            except:
                print("Input is not correct")
                exit(1)

calc = input("Type calculation:\n")

calc = calc.replace('**', '^')
for c in pi_e.keys():
    calc=calc.replace(c,str(pi_e[c]))

print("Answer: " + str(calculate(calc)))