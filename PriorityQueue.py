from queue import PriorityQueue as pq
q = pq()
q.put((10))
q.put((8))
q.put((5))
q.put((4))
while not q.empty():
    item = q.get()
    print(item)

# --------------------------------------------------------------------------

import heapq

li = [5, 7, 9, 1, 3]

heapq.heapify(li)

print ("The created heap is : ",end="")
print (list(li))

heapq.heappush(li,4)

print ("The modified heap after push is : ",end="")
print (list(li))

print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))


print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3,li))

print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3,li))