# Tic-Tac-Toe AI Agent (Minimax)

This project implements a simple AI agent that plays Tic-Tac-Toe using the Minimax algorithm.  
The agent always chooses the optimal move and cannot lose.

## Features
- Fully working Tic-Tac-Toe AI
- Minimax search algorithm
- Deterministic and optimal decision-making
- Clean and minimal Python code

## How it works
The agent simulates all possible future game states and evaluates them using:
- +1 for AI win
- -1 for human win
- 0 for draw

Then it chooses the move that maximizes its score.

## Run the project
Make sure you have Python 3 installed.

```
python3 game_agent.py
```

You will see the AI’s chosen move for a given board state.

## Project Structure
```
game_agent.py   # Main Tic-Tac-Toe AI logic (Minimax)
README.md       # Project description
```

## Future Improvements
- Add a simple Gradio web interface  
- Implement Connect-4 AI  
- Add Reinforcement Learning agent (Q-learning)  
- Add self-play training mode  
