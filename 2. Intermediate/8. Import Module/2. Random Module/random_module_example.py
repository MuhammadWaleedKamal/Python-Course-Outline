"""
Random module example.
Selects a raffle winner from a participant list.
"""

import random

participants = ["Ali", "Sara", "Tariq", "Nida"]
winner = random.choice(participants)
print(f"Today's raffle winner is: {winner}")

# Exercises:
# 1. Shuffle the participant list and print the result.
# 2. Select three unique winners using random.sample().
# 3. Simulate a dice roll with random.randint(1, 6).
