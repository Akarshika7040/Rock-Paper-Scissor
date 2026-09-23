# Rock-Paper-Scissors Match Arena

A Rock-Paper-Scissors game built using basic Python.

## Features
- Best-of-3 tournament rounds
- In-memory score tracking using lists
- input handling with dictionaries
- Clean separation of modules

## Overview
This project demonstrates modular programming because instead of combining all routines into a single script, the application separates user input handling, computer decision logic, game rules, and session history management across discrete modules coordinated by a central orchestrator (`main.py`).

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

## How to Run
Run the main script using Python:
```bash
python main.py

