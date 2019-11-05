import string

def text_analyzer(str):
    upper, lower, punctuation, spaces = 0, 0, 0, 0
    for char in str:
        if char.isupper() == True:
            upper += 1
        elif char.islower() == True:
            lower += 1
        elif char.punctuation() == True:
            punctuation += 1
        elif char.whitespace() == True:
            spaces += 1
        else:
            pass
   # print("The text contains " + str(len) + "characters")
    print(str(upper) + "upper letters")
    print(str(lower) + "lower letters")
    print(str(punctuation) + "punctuation marks")
    print(str(spaces) + "spaces")
            

text_analyzer("Wass")
