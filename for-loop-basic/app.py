# Basic
for i in range(0,151,1):
    print (i)

# Multiples of Five
for i in range(5,1001,1):
    if i % 5 == 0 :
        print(i)

# or
for i in range(5, 1001, 5):
    print(i)



# Counting, the Dojo Way
for i in range(0 ,101 ,1):
    if i % 5 == 0 :
        print('coding')
    else :
        print('coding dojo')



# Whoa. That Sucker's Huge
sum = 0
for i in range(0,500001,1):
    if i % 2 != 0 :
        sum += i
print(sum)



# Countdown by Fours
for i in range(2018,-1,-4):
    print(i)



# Flexible Counter
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)