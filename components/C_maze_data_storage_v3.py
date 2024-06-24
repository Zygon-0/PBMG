# dead ends were going back to the wrong room





# Comment
# Testing stuff * test
# | Head Comment |


# | Import |
import random
# From
from _Functions.F_statement_generator_v3 import statement_generator
from _Functions.F_choice_checker_v3 import choice_checker
from _Functions.F_int_checker import int_check
from picture_maze_game.functions.F_room_select import room_select
from picture_maze_game.functions.F_chosen_direction_v2 import choose_direction_output






# | Main Routine Setup |


# Variable setup
maze_size_list = ["s", "m", "l"]
rooms_list = []


# Starting text
statement_generator("Picture Based Maze Game", "*8", 3)
print("")
print("")








# | build maze |

# variable setup
cur_num_rooms = 1
room_back_setup = 0
rooms_num = 20


# make rooms list
while len(rooms_list) != rooms_num:

    # Room ver Setup
    room_here_setup = len(rooms_list) + 1
    room_print_setup = (random.randint(1, 15))
    if rooms_list:
        for i in range(0, len(rooms_list)):
            if int(room_here_setup) in rooms_list[i][2:4]:
                grab_back_vel = rooms_list[i]
                room_back_setup = grab_back_vel[0]

    # room left
    if room_print_setup <= 3:
        cur_num_rooms += 1
        room_left_setup = cur_num_rooms
        room_right_setup = -1

    # room right
    elif 3 < room_print_setup < 7:
        cur_num_rooms += 1
        room_left_setup = -1
        room_right_setup = cur_num_rooms

    # room left and right
    elif 7 <= room_print_setup:
        # room left
        cur_num_rooms += 1
        room_left_setup = cur_num_rooms
        # room right
        cur_num_rooms += 1
        room_right_setup = cur_num_rooms

    # Append room
    rooms_list_list = [room_here_setup, room_back_setup, room_left_setup, room_right_setup, room_print_setup]
    rooms_list.append(rooms_list_list)

    exit_room_subtract = len(rooms_list)
    # Add Dead ends
    while len(rooms_list) != cur_num_rooms:
        room_here_setup = len(rooms_list) + 1
        room_print_setup = 0
        for item in range(0, len(rooms_list)):
            if int(room_here_setup) in rooms_list[item][:3]:
                grab_back_vel = rooms_list[item]
                room_back_setup = grab_back_vel[0]
        room_left_setup = -1
        room_right_setup = -1
        rooms_list_list = [room_here_setup, room_back_setup, room_left_setup, room_right_setup, room_print_setup]
        rooms_list.append(rooms_list_list)

    # Add exit room randomly

    # chose the room to replace
    exit_can_replace = cur_num_rooms - exit_room_subtract
    print(exit_can_replace)
    print(cur_num_rooms)
    chosen_room_replace = random.randint(exit_can_replace, cur_num_rooms)
    print(chosen_room_replace)
    rooms_list[chosen_room_replace - 1][4] = 16

    for it in range(0, len(rooms_list)):
        if rooms_list[it][4] == 16:
            rooms_list[0][1] = rooms_list[it][0]



    #  print all room lists * test
    for i in range(len(rooms_list)):
        print(rooms_list[i])
