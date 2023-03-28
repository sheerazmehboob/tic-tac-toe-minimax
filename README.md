<h1>Tic Tac Toe</h1>
<hr>
<p>This code implements the game of Tic Tac Toe. The game is played between a player and a computer, where the player plays with 'X' and the computer plays with 'O'. The computer uses the Minimax algorithm to determine its moves. The Minimax algorithm is implemented in the MinMax() function, which recursively evaluates the board and returns 1 if the computer wins, -1 if the player wins, and 0 if there is no winner.</p>


<h2>How to Play</h2>
<hr>
<p>The game is played on a 3x3 board. The players take turns marking spaces on the board with their respective symbols ('X' or 'O'). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game. If all spaces on the board are filled and no player has won, the game is considered a draw.<p>


<h2>To play Game</h2>
<hr>
<li>Download the code from the GitHub repository.</li>
<li>Open a terminal and navigate to the directory where the code is saved.</li>
<li>Run the command python tic_tac_toe.py.</li>
<li>Follow the on-screen instructions to play the game.</li>


<h2>How the Game Works</h2>
<hr>
<p>The game starts with the computer making the first move. The computer chooses a random empty space on the board to place its symbol ('O'). The player then makes their move by entering the row and column indices of the space they want to mark with their symbol ('X').</p>
<p>After the player makes their move, the computer generates its move by analyzing the board and choosing the most optimal move. The computer's move is then displayed on the board. This process of the player and computer taking turns continues until one player wins or the game ends in a draw.</p>



<h2>Code Explanation</h2>
<hr>
<p>The code is written in Python and consists of several functions that perform different tasks:</p>
<ol>
<li>InitializeBoard() - Initializes the game board to an empty state.</li>
<li>DisplayBoard() - Displays the current state of the game board.</li>
<li>ComputerFirstMove() - Generates the first move for the computer.</li>
<li>PlayerMove() - Gets the player's move by prompting them to enter the row and column indices of the space they want to mark with their symbol.</li>
<li>CheckWin(tempBoard) - Checks if the game has been won by either player by analyzing the board.</li>
<li>ComputerMove() - Generates the computer's move by analyzing the board and choosing the most optimal move.</li>
<li>CheckDraw() - Checks if the game has ended in a draw.</li>
<li>CheckState() - Checks the current state of the game (win, lose, draw).</li>
<li>PlayGame() - The main function that initializes the game and runs the game loop.</li>
</ol>


<h2>Conclusion</h2>
<hr>
<p>Tic Tac Toe is a simple yet classic game that can be enjoyed by players of all ages. This Python implementation of the game provides an entertaining way to pass the time and challenge your strategic thinking.</p>
