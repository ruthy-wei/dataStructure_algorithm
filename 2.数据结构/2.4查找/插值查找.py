'''
 插值查找是根据要查找的关键字key与查找表中最大最小记录的关键字比较后的 查找方法，
 其核心就在于插值的计算公式 (key-a[low])/(a[high]-a[low])*(high-low)。
    时间复杂度o(logn)但对于表长较大而关键字分布比较均匀的查找表来说，效率较高。
'''
def binary_search(lis,key):
    low=0
    high=len(lis)-1
    time=0
    while low<high:
        time+=1
        mid=low+int((high-low)*(key-lis[low])/(lis[high]-lis[low]))
        print("mid=%s,low=%s,high=%s" % (mid,low,high))
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印查找的次数
            print("!times: %s" % time)
            return mid
    print("*times: %s" % time)
    return False
if __name__ == '__main__':
  LIST = [1, 5, 7, 8, 22, 33,44 ,54,77, 99, 123, 200, 222, 444]
  result = binary_search(LIST, 54)
  print(result)
