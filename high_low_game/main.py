import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Keep track of the player's score
    your_score = 0

    # Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        
        # Generate random numbers for the player and the computer
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        # Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        # Ensure the player inputs a valid choice (higher or lower)
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either 'higher' or 'lower': ")

        # Determine if the guess is correct
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            your_score += 1  # Increment score for a correct guess
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # Display the current score
        print("Your score is now", your_score)
        print()

    # Game over, print final score and performance message
    print("Thanks for playing!")
    print("Your final score is", your_score)

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()