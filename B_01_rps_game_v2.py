import random

# checks for an integer more than 0 (allows <enter>)
def int_checker(question):
    while True:
        error = " Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinte mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

#compares user / computer choice and returns
# results ( win / lose / tie)


# Ask user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# Game loop starts here
while rounds_player <= num_rounds:
    if mode == "infinite":
        rounds_heading = "\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_player + 1} of {num_rounds}💿💿💿"

        print(rounds_heading)

        # randomly choose from the rps list(excluding the exit code)
    comp_choice = random. choice(rps_list[:-1])
    print(" Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

def rps_compare(user, comp):
   
   # If the user and thye computer choice is the same, it's a tie
   if user == comp:
        round_result = "tie"
        
    # There are three ways to win 
    elif user == " paper" and comp == "rock":
            round_result = "win"
    elif user == "scissors" and comp == "paper":
            round_result = "win"
    elif user == "rock" and comp == "scissors":
            round_result = " win"

    # if it's not a win/ tie, then it's a loss
        
result = rps_compare(user_choice, comp_choice)
print(f"{user_choice} vs {comp_choice}{result}")

# Main routine start here

# Intialise game variables
mode = "regular"

rounds_player = 0
rounds_tie = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("💎📰✂ Rock / Paper / Scissors Game 💎📰✂")
print()


# ask user if they want to see the instruction and display
# them if requested
want_instruction = string_checker("Do you want to read the instruction? ")

# checks user enter yes (y) or no(n)
if want_instruction == "yes":
    instruction()

    # Ask user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop ends here
while rounds_player < num_rounds:

        # Rounds headings (based on mode)
        if mode == "infinite":
            rounds_heading = "\n Round {rounds_played + 1} (Infinite Mode) "
        else:
            rounds_heading = f"\n💿💿💿 Round {rounds_player + 1} of {num_rounds}💿💿💿"

        print(rounds_heading)

# randomly choose from the rps list(excluding the exit code)
comp_choice = random. choice(rps_list[:-1])
print(" Computer choice", comp_choice)

# get user choice
user_choice = string_checker("Do you want to read the instruction?")
# print("you chose", user_choice)

# If user choice is the exit code , break the loop
if user_choice == "xxx":
    break

result = rps_compare(user_choice, comp_choice)
print(f"{user_choice} vs{comp_choice}, {result}")

rounds_player += 1

# if users are in infinite mode, increase number of rounds!
if mode == "infinite":
        num_rounds += 1

        # Game loop ends here




        
