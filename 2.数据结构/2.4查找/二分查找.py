import time
def binSearch(lst, item):
  mid = len(lst) //2
  found = False
  if lst[mid] ==item:
      found = True
      return found
  if mid == 0:#mid等于0就是找到最后一个元素了。
      found = False
      return found
  else:
       if item > lst[mid]: #找后半部分
       #print(lst[mid:])
            return binSearch(lst[mid:], item)
       else:
            return binSearch(lst[:mid], item) #找前半部分


def sequential_search(lis, key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
        else:
            return False

start=time.time()
list_d = ['a','b','c','d','e','f','d','t']
value_d = 't'
aa=binSearch(list_d,value_d)#时间复杂度为 O(logn)
end=time.time()
start1=time.time()
bb=sequential_search(list_d,value_d) ## 时间复杂度O(n)
end1=time.time()
print(str(end))