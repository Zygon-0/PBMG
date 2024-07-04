# generates a statement with text and symbols
def statement_generator(statement, decoration, lines=None):
    fix = decoration[::-1]

    if len(decoration) > 1:
        middle = f'{decoration * 5} {statement} {fix * 5}'
    else:
        middle = f'{decoration * 5} {statement} {decoration * 5}'

    if len(decoration) == 1:
        top_bottom = f'{decoration * len(middle)}'
    else:
        top_bottom = decoration * int(len(middle) / len(decoration) + 1)
        while len(middle) != len(top_bottom):
            top_bottom = top_bottom.rstrip(top_bottom[-1])

    # if len(decoration) > 1:
    #     top_bottom = top_bottom.rstrip(top_bottom[-1])
    #     middle = middle.rstrip(middle[-1])

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    elif lines == 3:
        print(top_bottom)
        print(middle)
        print(top_bottom)
