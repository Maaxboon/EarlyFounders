"""
Simulate rolling two dice, and prints results of each
"""

import random

# Number of sides on each dice to roll
NUM_SIDES = 6

def main():
    # setting seed is useful for debugging
    # random seed(1): when uncommented ensures the same output is generated each time
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")
main()