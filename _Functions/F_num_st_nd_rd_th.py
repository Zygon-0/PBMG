def num_st_nd_rd_th(num):

    last_digit_check = [1, 2, 3]
    last_digit = int(repr(num)[-1])

    if len(repr(num)) > 1:
        if int(repr(int(repr(num)[:-1]))[-1]) == 1:
            if last_digit in last_digit_check:
                return f"{num}th"


    if last_digit == 1:
        return f"{num}st"

    elif last_digit == 2:
        return f"{num}nd"

    elif last_digit == 3:
        return f"{num}rd"

    else:
        return f"{num}th"
