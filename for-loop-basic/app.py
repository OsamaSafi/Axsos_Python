for i in range(0,151,1):
    print (i)


for i in range(5,1001,1):
    if i % 5 == 0 :
        print(i)

# or

for i in range(5, 1001, 5):
    print(i)


for i in range(0 ,101 ,1):
    if i % 5 == 0 :
        print('coding')
    else :
        print('coding dojo')

sum = 0
for i in range(0,500001,1):
    if i % 2 != 0 :
        sum += i
print(sum)


for i in range(2018,-1,-4):
    print(i)


lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)