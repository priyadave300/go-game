# go-game
In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces. A function is named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:
0: empty square
1: player 1 game piece
2: player 2 game piece

The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.
