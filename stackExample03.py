word = "a b c + +"

def letter_calculator(word):
    stack = []
    for letter in word.split(' '):
        if letter == "+" or letter == "-" or letter == "*" or letter == "/":
            if len(stack) < 2:
                print("This is not a word!")
                return None
            char1 = stack.pop()
            char2 = stack.pop()
            if letter == "+":
                res = char1 + char2