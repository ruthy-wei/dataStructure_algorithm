'''
题目：给定一个没有重复数字的序列，返回其所有可能的全排列。
输入: [1,2,3]
输出:
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
#全排列，没有重复元素
def permute(nums):
    if len(nums) == 0:
        return []
    used = [False] * len(nums)
    res = []
    dfs(nums, 0, [], used, res)
    return res
def dfs(nums, index, pre, used, res):
    # 先写递归终止条件
    if index == len(nums):
        res.append(pre.copy())
        return
    for i in range(len(nums)):
        if not used[i]:
            # 如果没有用过，就用它
            used[i] = True
            pre.append(nums[i])
            # 在 dfs 前后，代码是对称的
            dfs(nums, index + 1, pre, used, res)
            used[i] = False
            pre.pop()

print(permute([1,2,3]))