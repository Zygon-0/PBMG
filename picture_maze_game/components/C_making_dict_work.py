# Comment
# Testing stuff * test
# | Head Comment |


# | Import |
import random
import time
import pandas
# From
from _Functions.F_statement_generator_v3 import statement_generator
from _Functions.F_choice_checker_v3 import choice_checker
from _Functions.F_int_checker import int_check
from _Functions.F_num_st_nd_rd_th import num_st_nd_rd_th
from picture_maze_game.functions.F_room_select_v2 import room_select
from picture_maze_game.functions.F_chosen_direction_v2 import choose_direction_output









# | Main Routine Setup |


# Variable setup
rooms_list = []
when_visited_num = 1
keep_playing = True


# Starting text
statement_generator("Picture Based Maze Game", "*8", 3)
print()
print()


# Small bit of lore
statement_generator("Story Setup", "#", 1)
print()
print("you have joined the crew at\nworld leading maze making\ncompany. and as punishment\nfor making a mistake you"
      "\nhave been tasked with\ntesting the mazes the\ncompany makes ")
print()
print()


# Setup questions

while keep_playing:

    # Setup questions

    # view type with preview
    while True:
        view_chosen =  choice_checker("what view type would you like; above or in (enter <?> for preview): ", ["above", "in", "?"], "please enter above, in, or ?, for your response")

        # print the preview if requested
        if view_chosen == "?":
            print("")
            print("above is:\n"
                  "-----------------------------------------------------------------------------------------------------\n"
                  "|⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛|\n"
                  "|⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜|\n"
                  "|⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜|\n"
                  "|⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜|\n"
                  "|⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜|\n"
                  "|⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛|\n"
                  "|⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛|\n"
                  "|⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛|\n"
                  "|⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨⬛⬛⬛⬛⬛⬛|\n"
                  "|⬛⬛⬛⬛⬛🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛|\n"
                  "|⬛⬛⬛⬛🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛|\n"
                  "|⬛⬛⬛🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛|\n"
                  "|⬛⬛🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛|\n"
                  "|⬛🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛|\n"
                  "|🟨🟨🟨🟨🟨🟨⬜⬜⬜🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨|\n"
                  "|🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨|\n"
                  "|🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨|\n"
                  "-----------------------------------------------------------------------------------------------------\n"
                  "\n"
                  "in is:\n"
                  "------------------------------------------------------------------------------------------------\n"
                  "|🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨|\n"
                  "|🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨|\n"
                  "|🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨⬜⬜⬜🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨🟨|\n"
                  "|🟨🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨🟨|\n"
                  "|🟨🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨🟨|\n"
                  "|🟨🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟨|\n"
                  "------------------------------------------------------------------------------------------------")
            print("")

        elif view_chosen == "above":
            break

        elif view_chosen == "in":
            break

    print(f"chosen view: {view_chosen}")
    print("")

    # Chose mase size
    print("How many crossroads/corners(non dead ends)")
    rooms_num = int_check("would you like your maze to have: ", 1, 9999)

    # prints loading if player chooses a big enough maze size
    if rooms_num >= 5000:
        print("Loading...")





    # | Pandas Setup |

    # dict lists
    dict_rooms_num_list = []
    when_visited_list = []
    times_visited_list = []
    rooms_points_list = []

    # end dict
    end_results_dict = {
        "Room Visited": dict_rooms_num_list,
        "When": when_visited_list,
        "Times": times_visited_list,
        "Points": rooms_points_list
    }





    # | Build Maze |

    # variable setup
    cur_num_rooms = 1
    room_back_setup = 0

    # make rooms list
    while len(rooms_list) != rooms_num:

        # Room ver Setup
        room_here_setup = len(rooms_list) + 1
        room_print_setup = (random.randint(1, 15))
        if rooms_list:
            for i in range(0, len(rooms_list)):
                if int(room_here_setup) in rooms_list[i][:3]:
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

        # .append dict lists
        dict_rooms_num_list.append(room_here_setup)
        times_visited_list.append(0)
        when_visited_list.append(0)
        rooms_points_list.append(0)


    exit_room_subtract = len(rooms_list)
    # Add Dead ends
    while len(rooms_list) != cur_num_rooms:
        room_here_setup = len(rooms_list) + 1
        room_print_setup = 0
        for item in range(0, len(rooms_list)):
            if int(room_here_setup) in rooms_list[item][2:4]:
                grab_back_vel = rooms_list[item]
                room_back_setup = grab_back_vel[0]
        room_left_setup = -1
        room_right_setup = -1
        rooms_list_list = [room_here_setup, room_back_setup, room_left_setup, room_right_setup, room_print_setup]
        rooms_list.append(rooms_list_list)

        # .append dict lists
        dict_rooms_num_list.append(room_here_setup)
        times_visited_list.append(0)
        when_visited_list.append(0)
        rooms_points_list.append(0)


    # Add exit room randomly

    # chose the room to replace
    exit_can_replace = cur_num_rooms - exit_room_subtract
    chosen_room_replace = random.randint(exit_can_replace, cur_num_rooms)
    rooms_list[chosen_room_replace - 1][4] = 16

    for it in range(0, len(rooms_list)):
        if rooms_list[it][4] == 16:
            rooms_list[0][1] = rooms_list[it][0]



    #  print all room lists * test
    for i in range(len(rooms_list)):
        print(rooms_list[i])





    # | Main routine |

    # Main routine ver setup
    current_room = 1
    directions_list = ["left", "right", "back"]

    # Navigating maze
    while True:

        # Set next room to print
        room_to_print = room_select(rooms_list[current_room - 1][4], view_chosen)


        # dict stuff
        # update current rooms times_visited
        times_visited_list[current_room - 1] += 1

        # if first time in room set rooms when_visited
        if times_visited_list[current_room - 1] == 1:
            when_visited_list[current_room - 1] = num_st_nd_rd_th(when_visited_num)
            when_visited_num += 1


        # print current room
        print(room_to_print)
        # current room number * test
        print(f"current room = {current_room}")

        # win if in exit room
        if rooms_list[current_room - 1][4] == 16:
            break

        # setup to chose which direction to go
        has_next_direction = False

        # get the direction the player wants to go
        while not has_next_direction:

            # ask what direction out of left right back
            chosen_direction = choice_checker("Which direction would you like to go: ", directions_list,
                                              "please pick an available direction out of left(l) right(r) or back(b)")

            # get the actual next room (list)
            chosen_direction_output = choose_direction_output(current_room, chosen_direction, rooms_list)

            # re-asks the question if there is no path in the direction of the players choice
            if chosen_direction_output == -1:
                print("There is no path this way")

            # continue if the player has chosen a valid room
            else:
                has_next_direction = True
                current_room = chosen_direction_output





    # | give player results |

    # set 0 in when_visited to Never
    for i in range(len(when_visited_list)):
        if when_visited_list[i] == 0:
            when_visited_list[i] = "Never"

    # get each rooms points
    for i in range(len(when_visited_list)):

        if times_visited_list[i] != 0:
            rooms_points_list[i] = -10

        if i == rooms_list[current_room - 1][0] - 1:
            rooms_points_list[i] = 10 * len(rooms_list)

    # make data frame
    end_results_frame = pandas.DataFrame(end_results_dict)

    # print results
    time.sleep(2)
    print()
    print("Congratulations You Escaped The Maze!!!")
    print()
    print()
    print("----- End Results -----")
    print()
    print("Getting through the maze without visiting all the rooms is down to luck!")
    print("If you got a score of more than 10, you are officially lucky.")
    print()
    print("Here is your route and your final points...")
    print()
    print(end_results_frame)
    print()
    print(f"You went to {when_visited_num - 1} of the {len(rooms_list)} rooms and visited those rooms a total of {sum(times_visited_list)} times")
    print()
    print(f"==== Total Points: {sum(rooms_points_list)} ====")
    print()
    print()
    print()
    time.sleep(5)

    continue_game = choice_checker("Would you like another maze?: ", ["yes", "no"], "please enter yes or no")
    print("")
    if continue_game == "no":
        break


print("thanks for playing")
print()
time.sleep(2)

