# fixed numbers ending in 11, 12, or 13 returning as 11st, 12nd, and 13rd



def num_st_nd_rd_th(num):

    # list to tell program to only correct 1,2,3
    last_digit_check = [1, 2, 3]

    # gets last digit
    last_digit = int(repr(num)[-1])

    # if the number isn't single digit get the second to last digit then... (comment below)
    if len(repr(num)) > 1:
        # if second to last digit is 1 then... (comment below)
        if int(repr(int(repr(num)[:-1]))[-1]) == 1:
            # if last digit is 1,2,or 3 return <{num}th>
            if last_digit in last_digit_check:
                return f"{num}th"

    # applies correct place letters
    if last_digit == 1:
        return f"{num}st"

    elif last_digit == 2:
        return f"{num}nd"

    elif last_digit == 3:
        return f"{num}rd"

    else:
        return f"{num}th"

# copied to _Functions