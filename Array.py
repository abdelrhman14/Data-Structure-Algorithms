import numpy as np

arr = np.array([1,2,3])
print('Array:',arr)

# using append() to insert new value at end
arr =np.append(arr,[4],axis=0)
print('The appended array is:',arr)

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr = np.insert(arr,2,5,axis=0)
# printing array after insertion
print ("The array after insertion is :", arr)

# using delete() to delete value at specific position
# delete 2 at 1nd position
arr = np.delete(arr,2,axis=0)
# printing array after insertion
print ("The array after insertion is :", arr)

arr2 = [1,2,3,4]
# using pop() to remove element at 2nd position
print ("The popped element is : ",arr2.pop(2))
 

arr2 = [1,2,3,4]
# using index() to index element at 1nd position
print ("The index element is : ",arr2.index(1))
