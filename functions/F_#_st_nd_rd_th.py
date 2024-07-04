def num_st_nd_rd_th(num):

    last_digit = int(repr(num)[-1])

    if last_digit == 1:
        return f"{num}st"

    elif last_digit == 2:
        return f"{num}nd"

    elif last_digit == 3:
        return f"{num}rd"

    else:
        return f"{num}th"

from _Functions.F_int_checker import int_check

while True:
    numb = int_check("num: ", 1)

    output = num_st_nd_rd_th(numb)

    print(output)
