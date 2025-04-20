#created a go game function in which input will be 2 D array where will have 1s for player 1 stones and 2s for
#player 2 stones and 0 for empty square. will create 3 variables which will have count of stones for player1
#player 2 and empty square. wil use 2 for loops and trasverse across 1st through all the rows and then in 
#each row all elements and thenc ount 1s and 2s and 0 for empty square. Then atlast count of 1s higher than
#return 1 or 2s higher than 2 or 0

def who_won(game_board):
    player_1_count = 0
    player_2_count = 0
    empty_square_count = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1 :
                player_1_count +=1
            elif game_board[i][j] == 2:
                player_2_count +=1
            else:
                empty_square_count +=1
    if player_1_count > player_2_count:
        return 1
    elif player_2_count > player_1_count:
        return 2
    else:
        return 0

if __name__ == "__main__":
    game_board = [[1, 2, 2, 0], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(who_won(game_board))
