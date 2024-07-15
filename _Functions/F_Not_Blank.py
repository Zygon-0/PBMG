# checks if a string is valid
def not_blank(question):

    while True:

        response = input(question).strip()

        if response == "":
            print("sorry, response cant be blank")
        else:
            return response









