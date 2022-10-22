# Вычислить число π c заданной точностью d

# *Пример:* 

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def er(num):
    s = str(num)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0



pi = calc() 
print (pi, er(d))

