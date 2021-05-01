import random


def player_move(game_board: list):
    first_field = int(input("Startfield: "))
    second_field = int(input("Endfield: "))

    game_board[first_field] = "x"
    game_board[second_field] = "p"

    return game_board

def pc_move(game_board: list, no_more_moves: bool):
    legal_moves = get_legal_moves(game_board)
    if len(legal_moves) > 0:
        leftover_moves = compare_pc_moves(legal_moves)
        choice = random.randint(0, len(leftover_moves)-1)
        game_board = leftover_moves[choice]
        store_move = list(leftover_moves[choice])
    else:
        no_more_moves = True
        store_move = []
    return game_board, no_more_moves, store_move

def get_legal_moves(game_board: list):
    legal_moves = []
    for i in range(3, 9, 1):
        if game_board[i] == "c":
            if game_board[i-3] == "x":
                check_board = list(game_board)
                check_board[i] = "x"
                check_board[i-3] = "c"
                legal_moves.append(check_board)
    if game_board[7] == "c" and game_board[3] == "p":
        check_board_1 = list(game_board)
        check_board_1[7] = "x"
        check_board_1[3] = "c"
        legal_moves.append(check_board_1)
    if game_board[7] == "c" and game_board[5] == "p":
        check_board_2 = list(game_board)
        check_board_2[7] = "x"
        check_board_2[5] = "c"
        legal_moves.append(check_board_2)
    if game_board[6] == "c" and game_board[4] == "p":
        check_board_3 = list(game_board)
        check_board_3[6] = "x"
        check_board_3[4] = "c"
        legal_moves.append(check_board_3)
    if game_board[8] == "c" and game_board[4] == "p":
        check_board_4 = list(game_board)
        check_board_4[8] = "x"
        check_board_4[4] = "c"
        legal_moves.append(check_board_4)
    if game_board[4] == "c" and game_board[0] == "p":
        check_board_5 = list(game_board)
        check_board_5[4] = "x"
        check_board_5[0] = "c"
        legal_moves.append(check_board_5)
    if game_board[4] == "c" and game_board[2] == "p":
        check_board_6 = list(game_board)
        check_board_6[4] = "x"
        check_board_6[2] = "c"
        legal_moves.append(check_board_6)
    if game_board[3] == "c" and game_board[1] == "p":
        check_board_7 = list(game_board)
        check_board_7[3] = "x"
        check_board_7[1] = "c"
        legal_moves.append(check_board_7)
    if game_board[5] == "c" and game_board[1] == "p":
        check_board_8 = list(game_board)
        check_board_8[5] = "x"
        check_board_8[1] = "c"
        legal_moves.append(check_board_8)
    return legal_moves

def compare_pc_moves(legal_moves):
    leftover_moves = list(legal_moves)
    for i in dead_constellations_main:
        for e in legal_moves:
            found = True
            for y in range(9):
                if i[y] == e[y]:
                    continue
                else:
                    found = False
            if found:
                leftover_moves.remove(e)
    return leftover_moves

def win_check_player(game_board: list, running: bool):
        for i in range(6, 9, 1):
            if game_board[i] == "p":
                running = False
                print("Player Wins")
        return running

def win_check_pc(game_board: list, running: bool):
        for i in range(0, 3, 1):
            if game_board[i] == "c":
                running = False
                print("PC Wins")
        return running

def game(game_board: list, running: bool, bad_move: bool, store_move: list, dead_constellations: list):
    while running:
        no_more_moves = False
        game_board = player_move(game_board)
        print(game_board[0:3])
        print(game_board[3:6])
        print(game_board[6:9])
        print("-------------")
        running = win_check_player(game_board, running)
        if running:
            bad_move = False
        if bad_move:
            dead_constellations.append(store_move)
        if running:
            game_board, no_more_moves, store_move = pc_move(game_board, no_more_moves)
            print(game_board[0:3])
            print(game_board[3:6])
            print(game_board[6:9])
            running = win_check_pc(game_board, running)
            if no_more_moves:
                running = False
                print("No more Moves")
            bad_move = True
    return dead_constellations


dead_constellations_main = []
game_goes_on = True

while game_goes_on:
    game_board_main = ["p", "p", "p", "x", "x", "x", "c", "c", "c"]
    store_move_main = []
    running = True
    bad_move = False
    dead_constellations_main = game(game_board_main, running, bad_move, store_move_main, dead_constellations_main)
    go_on = input("Next Game? [y][n] ")
    if go_on == "n":
        game_goes_on = False