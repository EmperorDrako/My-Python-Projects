# Dice Roller Game
import keyboard
import time
import random
print("Welcome to the Dice Roller Game!")
running = True
while running:
    time.sleep(0.2)
    dicetwo = input("Do you want to roll two dice? (yes/no): ").lower()
    if dicetwo == "yes":
        min_roll1 = int(input("What is the minimum roll you want? "))
        time.sleep(0.4)
        max_roll1 = int(input("What is the maximum roll you want? "))
        min_roll2 = int(input("What is the minimum roll you want for the second die? "))
        time.sleep(0.4)
        max_roll2 = int(input("What is the maximum roll you want for the second die? "))
        def roll_dice():
            return random.randint(min_roll1, max_roll1), random.randint(min_roll2, max_roll2)
    else:
        min_roll = int(input("What is the minimum roll you want? "))
        time.sleep(0.4)
        max_roll = int(input("What is the maximum roll you want? "))
        def roll_dice():
            return random.randint(min_roll, max_roll)
    print("Press d to roll the dice or escape to exit...")
    while True:
        if keyboard.is_pressed('d'):
            time.sleep(0.1)
            print("You rolled a", roll_dice())
            time.sleep(0.1)
            break
        elif keyboard.is_pressed('escape'):
            print("Exiting the game...")
            running = False
            break
