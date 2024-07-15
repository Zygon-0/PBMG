# check if input is in valid list
def choice_checker(question, valid_list, error):
    while True:

        true_list = []
        response = input(question).lower()

        for item in valid_list:

            true_list.append([item, item[:], item[:]])


            if response == item[0] or response == item:
                return item

        # output an error if item not in valid list
        print(error)
        print()


# choice checker lists
yes_no_list = ["yes", "no"]
