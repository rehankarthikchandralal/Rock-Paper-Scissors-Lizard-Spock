# Rock-Paper-Scissors-Lizard-Spock (RPSLS) Game

This Python program is an extension of the classic "Rock, Paper, Scissors" game, introducing two additional options—**Lizard** and **Spock**—to create a fun and strategic twist.

In Rock-Paper-Scissors-Lizard-Spock, each option beats two other options and loses to two, providing more variety and complexity. This README provides instructions on the game rules, how the program works, and how to run it.

---

## How It Works

The program has three main components:

1. **name_to_number** - Converts a player’s choice (e.g., "rock") into a unique number (0-4).
2. **number_to_name** - Converts a randomly generated computer number (0-4) back into a choice.
3. **rpsls** - Plays a round of RPSLS by comparing player and computer choices and determining the winner.

## Game Rules

In this version:
- **Rock** crushes **Scissors** and **Lizard**.
- **Paper** covers **Rock** and disproves **Spock**.
- **Scissors** cuts **Paper** and decapitates **Lizard**.
- **Lizard** eats **Paper** and poisons **Spock**.
- **Spock** smashes **Scissors** and vaporizes **Rock**.

## Functions

### `name_to_number(name)`

- **Input**: A string representing the player’s choice (`"rock"`, `"paper"`, `"scissors"`, `"lizard"`, or `"Spock"`).
- **Output**: An integer (0-4) corresponding to the choice.
- **Error Handling**: If an invalid choice is entered, an error message is printed.

### `number_to_name(number)`

- **Input**: An integer (0-4).
- **Output**: A string corresponding to the computer’s choice.
- **Error Handling**: If an invalid number is provided, an error message is printed.

### `rpsls(player_choice)`

- **Input**: A string representing the player's choice.
- **Process**:
  - Converts player choice to a number.
  - Randomly generates the computer’s choice.
  - Determines and displays the winner based on the difference between player and computer choices.
- **Output**: The game result (win, lose, or tie) is printed to the console.

## Example Output

Running the code might produce output similar to this:

```plaintext
The player's choice is rock
The player's number is 0
The computer's number is 1
The computer's choice is Spock
The difference is 4
Computer wins!

