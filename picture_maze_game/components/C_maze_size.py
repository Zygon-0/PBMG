# Comment
# Testing stuff * test
# | Head Comment |


# | Import |
# From
from _Functions.F_statement_generator_v3 import statement_generator
from _Functions.F_int_checker import int_check

# | Main Routine Setup |


# Variable setup
maze_size_list = ["s", "m", "l"]
rooms_list = []


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


# Setup questions
while True:
    # Chose mase size
    print("How many crossroads/corners(non dead ends)")
    rooms_num = int_check("would you like your maze to have: ", 1, 9999)

    # prints loading if player chooses a big enough maze size
    if rooms_num >= 5000:
        print("Loading...")

    print("continues")