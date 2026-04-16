def a():
    return 5
print(a())


def a(): 
    return 5 
print(a()+a())


def a(): 
    return 5 
    return 10 
print(a())

def a(): 
    return 5 
    print(10) 
print(a())

def a(): 
    print(5) 
x = a() 
print(x)


def a(b,c): 
    print(b+c) 
print(a(1,2) + a(2,3))


def a(b,c): 
    return str(b)+str(c) 
print(a(2,5))

def a(): 
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10 
    return 7 
print(a())


def a(b,c): 
    if b<c: 
        return 7 
    else: 
        return 14 
    return 3 
print(a(2,3)) 
print(a(5,3)) 
print(a(2,3) + a(5,3))


def a(b,c): 
    return b+c 
    return 10 
print(a(3,5))


