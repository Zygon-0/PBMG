def choose_direction_output(current_room, chosen_direction, rooms_list):

    dead_end = 1
    global room_back
    if rooms_list:
        for i in range(0, len(rooms_list)):
            if int(current_room) in rooms_list[i][:3]:
                room_back = rooms_list[i][0]

    if chosen_direction == "back":
        check_number = 1

    elif chosen_direction == "left":
        check_number = 2

    else:
        check_number = 3

    for i in range(0, len(rooms_list)):
        if current_room in rooms_list[i][:1]:
            dead_end += 1

    if dead_end == len(rooms_list):
        return -1


    try:
        if rooms_list[current_room - 1][check_number] == -1:
            return -1
    except IndexError:
        if current_room == -1:
            return -1
        else:
            print(current_room)
            print(check_number)
            print(current_room - check_number)
            return room_back

    else:
        return rooms_list[current_room - 1][check_number]
