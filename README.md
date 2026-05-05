# AI Queen Game with Minimax and Alpha-Beta Pruning

A Python strategy game where players move a queen toward the lower-left corner of the board. The project includes both human gameplay and an AI opponent powered by Minimax and Alpha-Beta pruning.

---

## Overview

This project was built to practice artificial intelligence search algorithms through a simple turn-based board game.

The queen starts at a chosen position on a grid. Players take turns moving the queen left, down, or diagonally down-left. The player who moves the queen into the winning corner at `(0, 0)` wins.

The game supports:

- Human vs Human mode
- Human vs AI mode
- Minimax-based AI
- Alpha-Beta pruning
- Move validation
- Board rendering in the terminal
- Replayability after each game

---

## Game Rules

- The board uses zero-based indexing.
- Row `0` is the bottom row.
- Column `0` is the leftmost column.
- The queen can move:
  - left
  - down
  - diagonally down-left
- The queen must move at least one square.
- The first player to move the queen to `(0, 0)` wins.
- The initial queen position cannot be `(0, 0)`.

---

## AI Logic

The AI is implemented using game-tree search.

### Minimax

The Minimax algorithm evaluates possible future moves by assuming that:

- The AI tries to maximize its chance of winning.
- The human player tries to minimize the AI’s chance of winning.

### Alpha-Beta Pruning

Alpha-Beta pruning improves Minimax by reducing the number of game-tree nodes that need to be explored.

The project includes node counters to compare:

- Standard Minimax search
- Alpha-Beta pruning search

This makes it possible to observe the performance improvement from pruning.

---

## Tech Stack

**Language:** Python  
**Concepts:** Artificial Intelligence, Game Search, Minimax, Alpha-Beta Pruning, Recursion, Algorithms  
**Interface:** Terminal-based gameplay  

---

## Main Features

- Dynamic board size input
- Initial queen position selection
- Legal move generation
- Input validation
- Human vs Human gameplay
- Human vs AI gameplay
- Minimax decision-making
- Alpha-Beta pruning optimization
- Node counting for search comparison
- Replay option after each game

---

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
