"""
Daryl Appleton
November 26th, 2021

This program will demonstrate the use of each metod on 
a list. Using the Python programming language syntax.
"""

list = []

# Using the append() function 
# to push element in the stack
list.append('a')
list.append('b')
list.append('c')

print('Initial stack: ')
print(list)

# Using the pop() function 
# to push element in the stack
# LIFO order

print('\nElements popped from stack:')
print(list.pop())
print(list.pop())
print(list.pop())

list.append('d')
list.append('e')
list.append('f')

print('\nNew stack: ')
print(list)

# Using the clear() function 
# to empty the stack
list.clear()

# Checking to see if the stack is empty
if list:
    print("\nList is not empty.")
else:
    print("\nList is empty.")

list.append('g')
list.append('h')
list.append('i')

print('\nNew stack: ')
print(list)

print(f"\nThe size of the list is: {len(list)} ")