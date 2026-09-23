# Rock-Paper-Scissors Match Arena

A Rock-Paper-Scissors game built using basic Python.

## Overview
This project demonstrates modular programming because instead of combining all routines into a single script, the application separates user input handling, computer decision logic, game rules, and session history management across discrete modules coordinated by a central orchestrator (`main.py`).

## Features
- Best-of-3 tournament rounds
- In-memory score tracking using lists
- input handling with dictionaries
- Clean separation of modules


## Technologies & Tools Used
* **Programming Language:** Python 3
* **Built-in Modules:** `random`
* **Version Control:** Git & GitHub
* **Development Environment:** Visual Studio Code / Terminal

## Project Structure
- `main.py` - Runs the game menu and match loop
- `rules.py` - Evaluates round winners based on game rules
- `computer.py` - Generates random computer moves
- `stats.py` - Stores and displays session match records
- `basic_error.py` - Validates user inputs

## Steps to Install & Run the Project

### Option A: Run via GitHub Codespaces (Browser-Based, No Install)
1. On this repository page, click the green **Code** button.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. In the terminal at the bottom of the window, run:
   ```bash
   python main.py

### Option B: Run Locally on Your Machine
**Prerequisites:**
* Python 3.x installed on your operating system.
**Steps:**
1. Clone the repository:
   ```bash
   git clone [https://github.com/Akarshika7040/Rock-Paper-Scissor.git](https://github.com/Akarshika7040/Rock-Paper-Scissor.git)
2. Navigate to the folder:
   cd Rock-Paper-Scissor
3. Run:
      ```bash
   python main.py

## Instructions for Testing

Verify the application's stability and logic through the following terminal test procedures:

* **Menu Input Validation:** At the main menu, enter an out-of-range option such as `9` or `xyz`. Verify that the program outputs `"Invalid option! Please enter 1, 2, 3, or 4."` and re-prompts for input without crashing.
* **Move Shorthand & Casing:** Choose Option 1 to start a match, then input lowercase `r` or uppercase `P`. Verify that the system normalizes the input as `"Rock"` or `"Paper"`.
* **Invalid Move Handling:** During a match round, enter an unsupported character like `x` or `123`. Verify that the game prints `"Invalid input! Please type only r, p, or s."` and waits for a valid choice.
* **Tournament Termination:** Play consecutive rounds until either you or the computer reaches 2 wins. Verify that the match loop stops immediately, declares the overall winner, and saves the score.
* **History State & Reset:** From the main menu, select Option 2 to confirm your completed match appears in the log. Select Option 3 to clear history, then check Option 2 again to verify it displays `"No matches played yet."`


