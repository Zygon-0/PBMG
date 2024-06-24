# rethought the way it worked and massively simplified it


def choose_direction_output(current_room, chosen_direction, rooms_list):

    if chosen_direction == "back":
        check_number = 1

    elif chosen_direction == "left":
        check_number = 2

    else:
        check_number = 3

    if rooms_list[current_room - 1][check_number] == -1:
        print(current_room)
        return -1

    else:
        return rooms_list[current_room - 1][check_number]
