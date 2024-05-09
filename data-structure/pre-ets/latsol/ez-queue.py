# Find the missing numbers from the following list then USE INSERT LIST PYTHON to insert into the list

q = [1,2,3,4,6,7,8]
q.insert(4,5)
print(q)

q = [1,2,3,4,5,6,7,9,11]
q.insert(7,8)
q.insert(9,10)
print(q)

q = [2,4,10]
q.insert(2,6)
q.insert(3,8)

q = [1,3,7,11,15]
q.insert(2,5)
q.insert(4,9)
q.insert(6,13)
print(q)

# Delete numbers that shouldn't be on the list!
q = [1,2,5,3,4,6,7]
q.pop(2)
q.pop(4)
q.pop(4)
print(q)

q = [2,4,8,6,10]
q.pop(2)
q.pop(3)
print(q)

q = [3,5,11,7,9]
q.pop(2)
print(q)


q = [1,4,9,10,13]
q.pop()
q.pop()
print(q)