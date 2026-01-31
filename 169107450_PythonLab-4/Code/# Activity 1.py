# Activity 1: Customizable Dice Simulator
import random

def roll_dice(num_dice, num_sides):
    total = 0
    for _ in range(num_dice):
        total += random.randint(1, num_sides)
    return total
