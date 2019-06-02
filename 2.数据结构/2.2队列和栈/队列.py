from collections import deque
queue=deque([1,2,3])
tt=queue.popleft()
queue.append(tt)
print(queue)
