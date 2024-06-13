# import
import random
# from
from _Functions.F_statement_generator_v3 import statement_generator
from _Functions.F_choice_checker_v3 import choice_checker
from _Functions.F_int_checker import int_check
from picture_maze_game.functions.F_room_select import room_select
from picture_maze_game.functions.F_chosen_direction import choose_direction_output

# variable setup
maze_size_list = ["s", "m", "l"]
rooms_list = []

# Main routine setup

# Starting text
statement_generator("Picture Based Maze Game", "*8", 3)
print("")
print("")

# Small bit of lore
statement_generator("Story Setup", "#", 1)
print("")
print("you have joined the crew at\nworld leading maze making\ncompany. and as punishment\nfor making a mistake you"
      "\nhave been tasked with\ntesting the mazes the\ncompany makes ")
print("")
print("")

# setup questions

# Chose mase size
print("How many crossroads/corners(non dead ends)")
rooms_num = int_check("would you like your maze to have: ", 1, 9999)

if rooms_num >= 5000:
    print("Loading...")

# build maze
cur_num_rooms = 1
room_back_setup = 0
# room list
while len(rooms_list) != rooms_num:

    room_here_setup = len(rooms_list) + 1
    room_print_setup = (random.randint(1, 15))
    if rooms_list:
        for i in range(0, len(rooms_list)):
            if int(room_here_setup) in rooms_list[i][:3]:
                grab_back_vel = rooms_list[i]
                room_back_setup = grab_back_vel[0]

    # room back and left
    if room_print_setup <= 3:
        cur_num_rooms += 1
        room_left_setup = cur_num_rooms
        room_right_setup = -1

    # room back and right
    elif 3 < room_print_setup < 7:
        cur_num_rooms += 1
        room_left_setup = -1
        room_right_setup = cur_num_rooms

    # room back, left and right
    elif 7 <= room_print_setup:
        # room left
        cur_num_rooms += 1
        room_left_setup = cur_num_rooms
        # room right
        cur_num_rooms += 1
        room_right_setup = cur_num_rooms

    rooms_list_list = [room_here_setup, room_back_setup, room_left_setup, room_right_setup, room_print_setup]
    rooms_list.append(rooms_list_list)

for i in range(len(rooms_list)):
    print(rooms_list[i])

current_room = 1
directions_list = ["left", "right", "back"]

# Main routine
while True:

    try:
        room_to_print = room_select(rooms_list[current_room - 1][4])

    except IndexError:
        room_to_print = room_select(0)

    print(room_to_print)
    print(f"current room = {current_room}")

    next_room_printed = False

    while not next_room_printed:
        chosen_direction = choice_checker("Which direction would you like to go: ", directions_list,
                                          "please pick an available direction out of left(l) right(r) or back(b)")

        current_room = choose_direction_output(current_room, chosen_direction, rooms_list)

        if current_room == -1:
            print("There is no path this way")

        else:
            next_room_printed = True


print("")
print("")
print("1. Know what room to print\n"
      "2. know what rooms are next to that room\n"
      "3. make sure you can actually get to the end\n"
      "4. keep track of how many rooms there are")

