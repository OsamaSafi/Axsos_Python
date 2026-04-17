import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min
    if max < 0:
        pass
    num = random.random() * (max - min) + min    
    return round(num)
print(randInt())
print(randInt(max=50))