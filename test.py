def mystery_word(word):
    stack = []
    for letter in word.split(' '):
        if letter == "+":
            if len(stack) < 2:
                return "Invalid Case 1!"
            letr2 = stack.pop()
            letr1 = stack.pop()
            if letter == "+":
                res = letr1 + letr2
            stack.append(res)
        elif letter is not float:
            stack.append(letter)
        else:
            if letter == "":
                pass
    if len(stack) != 1:
        return "Invalid Case 2!"
    return stack[0][::-1]


############### Test Cases ###############
print("===================================")
print(mystery_word(word = "y s + a e + +")) # easy 
print(mystery_word(word = "d c + b a + +")) # abcd
print(mystery_word(word = "a +")) # Invalid Case 1!
print(mystery_word(word = "t a c +")) # Invalid Case 2!
print("===================================")