import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to Ludo Dice Roller!")
    while True:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"You rolled a {dice_roll}")
        
        # Predicting the next roll (though it's still random)
        predicted_roll = roll_dice()
        print(f"Predicted next roll: {predicted_roll}")
        
        continue_rolling = input("Do you want to roll again? (yes/no): ").strip().lower()
        if continue_rolling != 'yes':
            break

    print("Thanks for playing!")


    


