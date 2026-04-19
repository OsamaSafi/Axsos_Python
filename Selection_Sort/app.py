def selection_sort(nums):
    for i in range(len(nums)):
        min_val = i
        for j in range(i+1,len(nums)):
            if(nums[j] < nums[min_val]):
                min_val = j
        nums[i],nums[min_val] = nums[min_val],nums[i]
    return nums

print(selection_sort([0, 5, 6, 7, 1, 9]))