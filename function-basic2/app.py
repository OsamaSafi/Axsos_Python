
def countDown(number):
    a = []
    for i in range(number,-1,-1):
        a.append(i)
    return a
print(countDown(5))

####################################

def print_and_return(nums):
    print(nums[0])
    return nums[1]

print_and_return([1, 2])
print(print_and_return([1, 2]))

####################################

def first_plus_length(nums):
    sum = nums[0] + len(nums)
    return sum

print(first_plus_length([1,2,3,4,5]))

####################################

def values_greater_than_second(nums):
    greater = []
    for i in nums:
        if(i > nums[1]):
            greater.append(i)
    print(greater) 
values_greater_than_second([5,2,3,2,1,4])

####################################

def length_and_value(a,b):
    value = []
    for i in range(0 , a):
        value.append(b)
    return value
print(length_and_value(6,2))