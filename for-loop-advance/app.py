def biggie_size(nums):
    value = []
    for i in nums :
        if(i > 0):
            value.append('big')
        else:
            value.append(i)
    return value

print(biggie_size([-1, 3, 5, -5]))

#######################################

def count_positives(nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    nums[-1] = count
    return nums
print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

#######################################

def sum_total(nums):
    sum = 0
    for i in nums:
        sum+=i
    return sum
print(sum_total([1,2,3,4]))

#######################################

def length (nums):
    count = 0
    for i in nums:
        count+=1
    return count
print(length([]))

#######################################

def minimum (nums):
    val = nums[0]
    for i in nums:
        if(i < val):
            val = i
    return val
print (minimum([37,2,1,-9]))

#######################################

def maximum (nums):
    val = nums[0]
    for i in nums:
        if(i > val):
            val = i
    return val
print (maximum([37,2,1,-9]))

#######################################

def ultimate_analysis(nums):
    min = nums[0]
    max = nums[0]
    count = 0
    sum = 0
    for i in nums:
        count+=1
        sum+=i
        if(i < min):
            min = i
        else:
            max = i
    avarage = sum / count
    return {
        'sumTotal' : sum,
        'avarage' : avarage,
        'minimum' : min,
        'maximum' : max,
        'lenght' : count
    }

print(ultimate_analysis([37,2,1,-9]))

#######################################

def reverse_list(nums):
    for i in range(len(nums) // 2):
        nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
    return nums
print(reverse_list([37, 2, 1, -9]))
