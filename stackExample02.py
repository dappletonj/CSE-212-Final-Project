"""
Author: Daryl Appleton
Date: November 27th, 2021

In this code we are going to undo the order of text. If you follow
the code closely you will see that we are popping characters off of
one text and placing them in the order in which the text is popped off,
the text should look like it is backwards.
"""
# This is the text that will be undoing.
text = "Undo me please!"
print(text)

# In order to accomplish this we must turn this into a list.
stack = list(text)

# This will be where we are storing the characters from the text
# we are undoing.
newStack = []

index = 0

for index in range(len(stack)):
    item = stack.pop() # Remember the pop() method will remove an element from the top of the stack.
    """
    Because we stored the characters in a variable, we will just take 
    the popped element and apprend it to the new list.
    """
    newStack.append(item)
    index+=1

print("".join(newStack)) # Putting the characters back in text format.