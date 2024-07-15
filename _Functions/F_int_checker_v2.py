# checks integers
def int_check(question):

    while True:
        response = input(question)

        try:
            response = int(response)
            return response


        except ValueError:
            print("Please enter an integer")

