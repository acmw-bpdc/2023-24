def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 6)
                
def check_winner(board):
 # Check rows
 for row in board:
     if (row[0] == row[1] == row[2]!= " "):
         return row[0]
        
 # Check columns
 for col in range(3):
     if (board[0][col] == board[1][col] == board[2][col]!= " "):
         return board[0][col]
        
 # Check diagonals
     if (board[0][0] == board[1][1] == board[2][2] != " "):
         return board[0][0]
     if (board[0][2] == board[1][1] == board[2][0] != " "):
         return board[0][2]
     return None
        
def playgame():
    board = [[" " for _ in range(3)] for _ in range(3)] #board = [[" " for _ in range(columns)] for _ in range(rows)]
    current_player='X'
    winner = None
    while True:
        print_board(board)
                
        # Get player's move
        while True:
             row = int(input("Enter the row (0-2): "))
             col = int(input("Enter the column (0-2): "))
        
             if (board[row][col]==" "):
                 board[row][col] = current_player
                 break
             else:
                 print("Invalid Position, Try PlayAgain")
         # Check for a winner
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        count=0
        #Check for tie
        tie = True
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    count+=1
        if count==0:
            print("It's a tie!")
            break
        # Switch to the other player
        if current_player == "X":
            current_player = "O"
                 
        else:
            current_player="X"
playgame()

