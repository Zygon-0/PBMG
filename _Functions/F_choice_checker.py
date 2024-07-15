# check if input is in valid list
def choice_checker(question, valid_list, error, num_letters):
    while True:

        response = input(question).lower()

        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item

        # output an error if item not in valid list
        print(error)
        print()


# choice checker lists
yes_no_list = ["yes", "no"]
