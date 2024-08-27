# lists >> items in square Brackets
# items are ordered to use index 
# lists are mutable >> add, delete , edit
# items not unique
# can have different data types
l1 = ['one','two', 10, 50.2, True]
print(l1)
print(l1[3])
print(l1[1:-1])
print(l1.index(True))
print(len(l1))
# lists methods
# append() >>> take one arg
l1.append('alaa')
l1.append("bolbol")
print(l1)
myFriend = ['osama', 'ahmed', 'ali']
l1.append(myFriend) #append list at l1 as one element in list 
print(l1)
print(len(l1))
print(l1[7][1])

# extend() 
a = [1 , 2 , 3 , 4]
b = ['a', 'b' , 'c' , 'd']
a.extend(b)  #extend b in a as elements not list
print(a)

# remove() 
l1.remove(50.2)
print(l1)
l1.remove(myFriend)
print(l1)
print(len(l1))

# sort() by defalt  from small to large
x = [1 ,-10 , 50 , 15 , -5 , 30]
x.sort()
print(x)
# to reverse the sorted list >>> sort(reverse=true)
x.sort(reverse=True)
print(x) 

# reverse() reverse list and start by last element to first
x.reverse()
print(x)
l1.reverse()
print(l1)

# clear()
a.clear()
print(a)

# copy()
a = b.copy()
print(a)
b.append(5)
print(b) # main list
print(a) # copied list (shallow copy)

# count() number of items in list 
c = [1, 2, 3  , 5 ,4 ,3, 1 ,3 ,6]
print(c.count(1)) 
print(c.count(3))

# insert( index , object)
a.insert(3 , 10)
print(a)
a.insert(0 , 500)
print(a)
a.insert(6 , 20)
print(a)

# pop() remove and return element in the index
print(a.pop(6))
print(a.pop(1))
print(a.pop(5)) # error last index is 4 >> d
