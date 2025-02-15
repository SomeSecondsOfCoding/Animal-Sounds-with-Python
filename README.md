#Rock, Paper, Scissors AI

#Overview

This is a simple Rock, Paper, Scissors game written in Python. The AI opponent learns from the player's choices and adapts its strategy over time. Unlike a random-choice AI, this implementation predicts the player's most frequent move and selects the optimal counter-move.

#How It Works

1. The player selects rock, paper, or scissors.

2. The AI starts with a random choice in the first round.

3. After each round, the AI tracks the player's choices in a history dictionary.

4. The AI predicts the most frequently chosen move and selects the best counter-move.

5. The game continues until the player decides to quit.
