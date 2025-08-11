# Wordle Game Project

## Folder Structure

```
yy/
├── task6.py         # Main Python script for Wordle (CLI and GUI)
├── README.md        # Project documentation (this file)
└── words.txt        # List of valid 5-letter words (external file, not included here)
```

- **task6.py**: Contains all the logic for both the command-line and GUI versions of the Wordle game.
- **README.md**: Explains the structure and logic of the project.
- **words.txt**: A plain text file with one 5-letter word per line, used as the dictionary for valid guesses and secret words.

## Logical Structure

### Main Components

- **Word Loading**: Reads valid 5-letter words from `words.txt` for use in the game.
- **Game Logic**: Handles random word selection, guess checking, and feedback generation.
- **CLI Game**: Runs a text-based Wordle game in the terminal.
- **GUI Game**: Uses Tkinter to provide a graphical Wordle experience, including a grid, on-screen keyboard, and colored feedback.

### How It Works

1. **Startup**: The script loads the word list and picks a random secret word.
2. **Mode Selection**: 
   - If run normally, it starts the CLI game.
   - If run with `--gui`, it launches the GUI version.
3. **Gameplay**:
   - Players have 6 attempts to guess the secret word.
   - After each guess, feedback is given for each letter (correct position, wrong position, or not in word).
   - In the GUI, feedback is shown with colored tiles and an on-screen keyboard.
4. **End Condition**: The game ends when the word is guessed or attempts run out.

### Flowchart

```
[Start]
   |
[Load words.txt]
   |
[Pick random word]
   |
[CLI or GUI?]---(if --gui)-->[Start GUI Game]
   |                             |
   |                        [User Inputs Guess]
   |                             |
   |                        [Show Feedback]
   |                             |
   |                        [Win/Lose?]
   |                             |
   |                        [End]
   |
(Start CLI Game)
   |
[User Inputs Guess]
   |
[Show Feedback]
   |
[Win/Lose?]
   |
[End]
```

## Bonus: Problem Analysis & Alternative Solutions

### Problem Analysis

- **Goal**: Implement a playable Wordle game with both CLI and GUI options.
- **Requirements**: 
  - 5-letter word guessing
  - Feedback for each letter
  - 6 attempts
  - Dictionary validation

### Considered Solutions

- **GUI Frameworks**: Considered PyQt and Kivy for the GUI, but chose Tkinter for simplicity and standard library support.
- **Word List Storage**: Considered embedding the word list in the script, but using an external file (`words.txt`) makes updates easier.
- **Feedback Logic**: Explored more complex feedback (e.g., handling duplicate letters exactly as Wordle does), but kept logic simple for clarity.
- **Game Modes**: Considered adding a "hard mode" or statistics tracking, but focused on core gameplay for this version.

---

*This project demonstrates basic Python programming, file I/O, and GUI development with Tkinter, structured for clarity and easy extension.*
