'''
Complete soltion of Book 
"Python For Software Design by Allen B. Downey"
by Harsh Bhatia ( www.harshbhatia.net )
'''
'''Exercise 6.1
Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.'''
def compare(x,y):
  if x>y:
    return 1
  elif x==y:
    return 0
  else:
    return -1

print compare(2,1)
print compare(1,1)
print compare(1,3)