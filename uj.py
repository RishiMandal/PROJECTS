import random
def repeat_code():
    while True:
        y = input("Enter username: ")
        z = input("Enter your choice [stone/paper/scissor]: ").strip().lower()
        print(f"{y} chose {z}")
        if z == "stone":
            a = 1
        elif z == "paper":
            a = 2
        elif z == "scissor":
            a = 3
        else:
            print("Invalid choice, please choose stone, paper, or scissor.")
            continue
        x = random.randint(1, 3)
        if x == 1:
            computer_choice = "stone"
        elif x == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissor"
        print(f"Computer chose {computer_choice}")
        if a == x:
            print("It's a tie!")
        elif (a == 1 and x == 3) or (a == 2 and x == 1) or (a == 3 and x == 2):
            print(f"{y} wins!")
        else:
            print("Computer wins!")
        repeat = input("Do you want to run the game again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break
repeat_code()
