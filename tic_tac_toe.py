# Importing necessary libraries
import random
from copy import deepcopy

# Initializing the game board
Board = [[0 for i in range(3)] for j in range(3)]
EmptySpace='-'  # To represent empty space in the board


# Function to initialize the board
def InitializeBoard():
    for i in range(3):
        for j in range(3):
            Board[i][j]=EmptySpace


# Function to display the current board state
def DisplayBoard():
    print()
    for i in range(3):
        print("-------------")
        for j in range(3):
            print("|", Board[i][j], end=" ")
        print("|")
    print("-------------")
    print()


# Function to generate the first move for the computer
def ComputerFirstMove():
    i=random.randint(0,2)
    j=random.randint(0,2)
    Board[i][j]='O'


# Function to get player's move
def PlayerMove():
    while True:
        try:
            i = int(input("Input Row Index (0-2): "))
            j = int(input("Input Column Index (0-2): "))
            if i not in range(3) or j not in range(3):
                print("Invalid input! Index should be in range of 0-2.")
                continue
            if Board[i][j] == EmptySpace:
                Board[i][j] = 'X'
                break
            else:
                print("Invalid Move!!")
                print("Try Again")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# Function to check for winning condition
def CheckWin(tempBoard):
    # Checking for computer's win condition
    for i in range(3):
        if(tempBoard[i][0]=='O' and tempBoard[i][1]=='O' and tempBoard[i][2]=='O') or (tempBoard[0][i]=='O' and tempBoard[1][i]=='O' and tempBoard[2][i]=='O'):
            return 1
    if((tempBoard[0][0]=='O' and tempBoard[1][1]=='O' and tempBoard[2][2]=='O') or (tempBoard[0][2]=='O' and tempBoard[1][1]=='O' and tempBoard[2][0]=='O')):
        return 1
    
    # Checking for player's win condition
    for i in range(3):
        if(tempBoard[i][0]=='X' and tempBoard[i][1]=='X' and tempBoard[i][2]=='X') or (tempBoard[0][i]=='X' and tempBoard[1][i]=='X' and tempBoard[2][i]=='X'):
            return -1
    if((tempBoard[0][0]=='X' and tempBoard[1][1]=='X' and tempBoard[2][2]=='X') or (tempBoard[0][2]=='X' and tempBoard[1][1]=='X' and tempBoard[2][0]=='X')):
        return -1
    
    return 0


# Function to generate the computer's move
def ComputerMove():
    winningMove = []
    loosingMove = []
    noEffect = []

    # Checking Moves Effect
    for i in range(3):
        for j in range(3):
            tempBoard = deepcopy(Board)
            tempBoard2 = deepcopy(Board)
            
            # Check if empty space available
            if (tempBoard[i][j]==EmptySpace):
                # Check for winning move 
                tempBoard[i][j] = 'O'
                if(CheckWin(tempBoard)==1):
                    winningMove.append((i,j))
                # Check for loosing move and block it 
                tempBoard2[i][j] = 'X'
                if(CheckWin(tempBoard2)==-1):
                    loosingMove.append((i,j))
                # Check for no effect move 
                if(CheckWin(tempBoard)==0):
                    noEffect.append((i,j))

    # Making Suitable Move 
    if(len(winningMove)):
        # Make winning move
        x = winningMove.pop(0)
        Board[x[0]][x[1]] ='O'
    elif(len(loosingMove)):
        # Block loosing move
        x = loosingMove.pop(0)
        Board[x[0]][x[1]] ='O'
    elif((len(noEffect))):
        # Make any available move 
        x = noEffect.pop(0)
        Board[x[0]][x[1]] ='O'


# Draw Game Check
def CheckDraw():
    for i in range(3):
        for j in range(3):
            if(Board[i][j]==EmptySpace):
                return False
    return True    


# Checking Game State
def CheckState():
    if(CheckWin(Board)==1):
        DisplayBoard()
        print("Better Luck Next Time!!")
        print("Computer Won!!")
        return True
    elif(CheckWin(Board)==-1):
        DisplayBoard()
        print("Congartulations!!")
        print("You Won!!")
        return True
    
    if(CheckDraw()):
        DisplayBoard()
        print("Game Draw")
        return True


# Game Play
def PlayGame():
    InitializeBoard()
    ComputerFirstMove()

    while True:
        DisplayBoard()
        PlayerMove()
        if(CheckState()):
            return
        ComputerMove()
        if(CheckState()):
            return

# Game Play Started From Here
PlayGame()