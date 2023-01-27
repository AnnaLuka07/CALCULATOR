
x = 0
y = 0
def init(a, b):
    global x
    global y
    x = a
    y = b

def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        print('На 0 делить нельзя!')
def exponent(a, b):
    return a ** b
def remaind(a, b):
    return a % b
def integer(a, b):
    return a // b

def operation (a, b, op):
    result = None
    if op == '1':
        result = sum (a, b)
    elif op == '2':
        result = sub(a, b)
    elif op == '3':
        result = mult(a, b)
    elif op == '4':
        result = div(a, b)
    elif op == '5':
        result = exponent(a, b)
    elif op == '6':
        result = remaind(a, b)
    elif op == '7':
        result = integer(a, b)
    else:
        print('Неизвестная операция')
    return result
