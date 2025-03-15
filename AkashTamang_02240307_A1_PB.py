import random

def guess_game():
    print("Guess Number Game (1-10)")
    num = random.randint(1, 10)
    tries = 0
    while True:
        try:
            guess = int(input("Guess: "))
            tries += 1
            if guess < 1 or guess > 10:
                print("Use 1-10 only")
            elif guess < num:
                print("Too low")
            elif guess > num:
                print("Too high")
            else:
                print(f"Correct! It took {tries} tries")
                break
        except:
            print("Enter a number")

def rps_game():
    print("Rock Paper Scissors")
    choices = ["rock", "paper", "scissors"]
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    while True:
        choice = input("rock/paper/scissors/quit: ").lower()
        if choice == "quit":
            break
        if choice not in choices:
            print("Invalid choice")
            continue
        comp = random.choice(choices)
        print(f"Computer: {comp}")
        if choice == comp:
            print("Tie")
        elif wins[choice] == comp:
            print("You win")
        else:
            print("Computer wins")

while True:
    print("\nMini Games Menu:")
    print("1. Guess Number")
    print("2. Rock Paper Scissors")
    print("3. Exit")
    choice = input("Choose (1-3): ")
    if choice == "1":
        guess_game()
    elif choice == "2":
        rps_game()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Enter 1, 2 or 3")