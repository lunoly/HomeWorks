
from operator import pow, truediv, mul, add, sub, floordiv

import math
import re

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

isnumbers = ('0','1','2','3','4','5','6','7','8','9','.')

def calculate(s):
    isnumber = 1
    for c in s:
        if c not in isnumbers:
            isnumber = 0
    if isnumber:
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            try:
                return operators[operator](calculate(left), calculate(right))
            except:
                print("Input is not correct")
                exit(1)

def brackets(s):
    results = set()
    stmp = ''
    print(results)
    for start in range(len(s)):
        string = s[start:]
        results.update(re.findall('\(.*?\)', string))
    for sres in results:
        if str(sres).count('(') == 1:
            stmp = str(sres)
    print(type(stmp))
    if stmp.strip()!='':
        calcinbrackets = str(calculate(stmp[1:-1]))
        s = s.replace(stmp,calcinbrackets)
        return brackets(s)
    else:
        return s

#    return results[-1]


calc = input("Type calculation:\n")

calc = calc.replace('**', '^')

for c in pi_e.keys():
    calc=calc.replace(c,str(pi_e[c]))

calc = brackets(calc)

print('calc: ',calc)

print("Answer: " + str(calculate(calc)))