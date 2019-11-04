def text_analyzer(str):
    upper, lower, punctuation, spaces = 0, 0, 0, 0
    for char in str:
        if char.isupper() == True:
            upper += 1
        elif char.islower() == True:
            lower += 1
        elif char->punctuation:
            punctuation += 1
        elif char->space:
            spaces += 1
        else:
            pass
    print("The text contains " + len + "characters")
    print(upper + "upper letters")
    print(lower + "lower letters")
    print(punctuation + "punctuation marks")
    print(spaces + "spaces")
            

text_analyzer("Wass")
