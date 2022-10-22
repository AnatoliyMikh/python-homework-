# Вычислить число π c заданной точностью d

# *Пример:* 

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def er(num):    # подсчет количества знаков после запятой
    s = str(num)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

def calc():     # вычисление числа π
    k = 1
    x = 0
    for k in range(1, 300):
        x = x+4*((-1)**(k+1))/(2*k-1)
    return x

d = input('Input d: ')

pi = calc() 
print (pi, er(d))

