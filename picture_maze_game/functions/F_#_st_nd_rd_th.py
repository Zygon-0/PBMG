def num_st_nd_rd_th(num):

    # gets last digit
    last_digit = int(repr(num)[-1])

    # applies correct place letters
    if last_digit == 1:
        return f"{num}st"

    elif last_digit == 2:
        return f"{num}nd"

    elif last_digit == 3:
        return f"{num}rd"

    else:
        return f"{num}th"
