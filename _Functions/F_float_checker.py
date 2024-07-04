# checks integers
def float_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    elif low is None and high is not None:
        error = f"Please enter an integer that is less than {high}"
        situation = "high only"
    else:
        error = f"Please enter an integer that is more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = float(response)

            # check that integer is valid (ie: not too low / too hig etc.)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            elif situation == "high only":
                if response <= high:
                    return response

            print(error)

        except ValueError:
            print(error)
