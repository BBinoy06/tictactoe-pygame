# Tic-Tac-Toe Game (Console + GUI)

## Description
A fully-featured Tic-Tac-Toe game implemented in **Python**.  
- Includes **Console Version** and **Pygame GUI Version**.  
- Implements **AI opponents** with **Easy, Medium, and Hard (Minimax)** difficulty levels.  
- Demonstrates **Object-Oriented Programming (OOP)**, **game logic design**, and **AI decision-making**.

---

## Features
- **Console Version:**    
  - Player vs Computer with Easy, Medium, and Hard AI  
  - Medium AI uses win/block logic  
  - Hard AI uses Minimax algorithm for optimal moves  

- **Pygame GUI Version:**  
  - Visual interface with clickable grid   
  - Same difficulty levels and logic as console version  
  - Visual indicators for wins, draws, and losses
  - Has home and restart button

---

## Tech Stack / Tools Used
Languages:
- Python
Libraries / frameworks:
- Pygame for GUI
- unittest for unit testing
Concepts:
- Object-Oriented Programming (classes for Board, Game, Computer etc.), AI logic (minimax)
Tools:
- Version control: Git via command prompt / GitHub
- Virtual environment: venv (to isolate Python packages)
- Editor / IDE: IDLE (Python’s built-in editor)
- Object-Oriented Programming (OOP)
- Platform: Tested on Windows

---

## Installation / Setup
Open command prompt
- git clone https://github.com/BBinoy06/tictactoe-pygame.git
navigate to the project folder (tictactoe-pygame)
- cd tictactoe-pygame
if using vitual environment on windows:
- venv\Scripts\activate
- pip install -r requirements.txt

(GUI version)
- python main.py

---

## How to use
**GUI:**
- User clicks on their preferred level of difficulty and they land on screen with grid and on the top right, home and restart buttons
- if user had clicked easy then the computer places marks randomly. If they had picked hard the computer looks at wins and also tries to block. In hard level the computer tries to win or force a draw by using **Minimax algorithm** to choose optimal moves

**Console version:**
- Run the console version by cloning the other reposiory and then run (e.g. `python app.py`).  
- You will be asked to input your move in the format `row,column` (each between 0-2).  
- After your move, the computer will respond based on the difficulty:  
   - Easy → random  
   - Medium → win/block logic  
   - Hard → minimax  
- The console will display the board after each move, and at the end it tells you who wins or if it’s a draw.

---

## How it works and key logic (Detailed and screenshots in TictacToecode.pdf)
- Board Class
- Player Class
- Computer Class
- Game Class
**Win -Block logic (medium)**
- first check if the computer can win in this move
- if not winning immediately, check if the opponent(player) is about to win in their next move
- if neither condition triggers then choose a random empty spot
**Minimax (Hard)**
- a recursive algorithm which explores all possible future game states.
- each possible state is analysed to see whether it leads to win, loss or draw.
- it uses the concept of maximiser(computer) and minimiser(opponent).
- The computer assumes the opponent plays optimally
- end states are assigned scores
- The recursion works by playing hypothetical moves
then the move that the computer acctually makes in the game uses this to choose the best move from the current board state

---

## Tests (unittest)
**GUI Tests (testcode.py):**
Window Size:
- Verifies that the main window size is set to 600 pixels.
Board Size:
- Ensures the board size is 540 pixels.

Board Position:
- Checks that the board is centered within the window.

**Console Tests (testcode_app.py):**
Board Initialization:
- Confirms that the board initializes with a 3x3 grid of empty spaces.

Player Initialization:
- Validates that players are correctly initialized with their names and marks.

Game Initialization:
- Ensures the game starts with the correct initial player and board state.

Turn Switching:
- Tests that the game correctly alternates turns between players.

Game Over Conditions:
- Win Condition: Verifies that the game detects a win when a player has three marks in a row.
- Draw Condition:Checks that the game recognizes a draw when the board is full with no winner.

AI Behavior:
- Medium Difficulty: Tests that the AI makes optimal moves, such as winning when possible, blocking the player when necessary, or choosing a random move when no immediate action is required.
- Hard Difficulty: Assesses the AI's ability to make the best possible move using the minimax algorithm.

## Future Improvements
- Implement a stopwatch feature which could time the duration of each game
- Expand Unit Test Coverage for the GUI version
- Improve User Interface
- Add mutiplayer feature

## Skills and what I learned 
**Algorithm Design – Minimax Implementation**
- Implemented the Minimax algorithm to create an unbeatable AI for Tic-Tac-Toe.
- Enhanced understanding of decision trees and game theory in AI development.
**Game Development with Pygame**
- Transitioned from console-based logic to a graphical user interface using Pygame.
- Gained experience in handling events, rendering graphics, and managing game loops.
**Unit Testing with unittest**
- Learned to write unit tests to ensure code reliability and catch bugs early.
- Developed tests for both console and GUI components, enhancing code maintainability.
**Object-Oriented Programming (OOP)**
- Designed classes like Board, Player, Computer, and Game to structure code effectively.
- Improved code modularity and reusability through OOP principles.
**Debugging and Problem Solving**
- Enhanced debugging skills by identifying and fixing issues in both logic and UI.
- Developed a systematic approach to problem-solving in software development

