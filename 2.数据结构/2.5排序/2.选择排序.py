def selectionSort(nums):
    for i in range(len(nums)-1):
        MinIndex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[MinIndex]:
                MinIndex=j
        nums[i],nums[MinIndex]=nums[MinIndex],nums[i]
    return nums
print(selectionSort([1,9,2,7,5,3]))