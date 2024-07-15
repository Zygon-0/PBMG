# checks if a string is valid
def string_checker(question, exit):

    not_allowed = ["a", "b", "c", "d", "e", "f", ]

    while True:

        end = 0
        response = input(question).lower().strip()

        for item in not_allowed:
            if item not in response:
                end = 1
                continue
            elif response == "":
                end = 2

        if end == 0:
            return response
        elif end == 1:
            print("response can only have letters and -")
        elif end == 2:
            print("sorry, response cant be blank")









