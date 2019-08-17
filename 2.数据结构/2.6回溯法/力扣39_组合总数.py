'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[[7],[2,2,3]]
'''
def combinationSum(candidates,target):
    temp,res=[],[]
    sorted(candidates)
    dfs(candidates,target,temp,res,0)
    return res
def dfs(candidates,target,temp,res,index):
    if target==0:
        res.append(temp[:])
        return
    for i in range(index,len(candidates)):
        if target-candidates[i]>=0:
            temp.append(candidates[i])
            dfs(candidates,target-candidates[i],temp,res,i)
            temp.pop()

print(combinationSum([2,3,6,7],7))