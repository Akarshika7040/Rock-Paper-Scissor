## 1. Problem Statement
- Game with logic, input handling, and state management are tangled together. This design pattern leads to frequent program crashes when users enter invalid characters and makes debugging or extending the codebase difficult. Additionally, many basic command-line applications lack runtime state tracking, resetting match progress without giving users a summary of their session performance.

## 2. Project Scope
The goal of this project is to build a Rock-Paper-Scissors game in Python. The system separates responsibilities across dedicated modules:
- Input handling and sanitization (basic_error.py)
- Randomized opponent decision-making (computer.py)
- Rule evaluation and outcome resolution(rules.py)
- Session history tracking(stats.py)
- Core application execution and menu routing(main.py)

## 3. Target Users
- **Students and Beginners:** Learning Python control flow, modular architecture, and basic python practices.
- **Casual Terminal Users:** Looking for a quick, interactive game playable directly inside any standard terminal environment.
  
 ## 4. High-Level Features
- **Tournament Mode:** A Best-of-3 match system that determines an overall winner.
- **Input Sanitization:** Dictionary-based validation that handles accidental whitespace and case differences, preventing runtime crashes.
- **Computer as Opponent:** Pure random move selection simulating an impartial opponent.
- **Session Data Tracking:** An in-memory list tracking match results and final scores across the active session.
- **Session Control:** Clear navigation options to play, review match records, reset history, or exit cleanly.
