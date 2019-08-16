import random
import os
# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monseter
# draw player in the grid
# take input for movemenet
#move player, unless invalif move (past edges
# check for win/loss
# clear screen and redraw grid

CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),
        (0,1),(1,1),(2,1),(3,1),(4,1),
        (0,2),(1,2),(2,2),(3,2),(4,2),
        (0,3),(1,3),(2,3),(3,3),(4,4),
        (0,4),(1,4),(2,4),(3,4),(4,4)]

def clear_screen():
    os.system('clear')

def get_locations():
    return random.sample(CELLS,3)

def move_player(player, move):
    #get the player's location
    x, y = player
    if move == 'LEFT':
        player = x-1, y
    if move == 'RIGHT':
        player = x+1, y
    if move == 'DOWN':
        player = x, y+1
    if move == 'UP':
        player = x, y-1
    return player

def get_moves(player):
    moves = ["LEFT","RIGHT","UP","DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")

    return moves

def draw_map(player):
    print(' _'*5)
    tile = "|{}"

    for cell in CELLS:
        x,y = cell
        if x < 4:
            line_end=""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output,end=line_end)


def game_loop():
    monster, door, player = get_locations()
    while True:
        clear_screen()
        valid_moves = get_moves(player)
        draw_map(player)
        print("You're currently in room {}".format(player)) #fill with player position
        print("You can move {}".format(valid_moves)) #fill with available rooms
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()
        move_player(player, move)
        if move == "QUIT":
            break
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n Oh no! The monster got you!")
                play_again()
                
            if player == door:
                print('\n Congrats you won!')
                play_again()
                
        else:
            input("That's not a valid move, you can only move {}".format(valid_moves))

def play_again():
    print("Do you want to play again? y/n")
    playing = input('> ')
    if playing.lower() == 'y':
        game_loop()
    else:
        print("Okay, we'll see you soon!")
        break

print("Welcome to the dungeon")
input("Press return to start!")
clear_screen()
game_loop()



    #On the door? THey win
    #On the monster? they lose
    #Otherwise loop back around
