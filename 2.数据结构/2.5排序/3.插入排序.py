def insertionSort(nums):
    for i in range(len(nums)-1):
        curNum, preIndex = nums[i + 1], i  # curNum 保存当前待插入的数
        while preIndex >= 0 and curNum < nums[preIndex]:  # 将比 curNum 大的元素向后移动
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = curNum  # 待插入的数的正确位置
    return nums