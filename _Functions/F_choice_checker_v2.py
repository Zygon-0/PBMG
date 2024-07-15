# check if input is in valid list
def choice_checker(question, valid_list, error):
    while True:

        # max_len = int(len(max(valid_list, key=len)))
        response = input(question).lower()
        len_plus = 0
        check = 0

        # excepts response if it is one of the items in list or the first letter of said item
        for item in valid_list:
            while check == 0:

                print(len(item))
                print(len_plus)
                print(item[:len(item) - len_plus])

                if response == item[:len(item) - len_plus]:
                    return item
                elif int(len(item)) == len_plus+1:
                    check = 1
                else:
                    len_plus += 1

        # output an error if item not in valid list
        print(error)
        print()


# choice checker lists
yes_no_list = ["yes", "no"]
