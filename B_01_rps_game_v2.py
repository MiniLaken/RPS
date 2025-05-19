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

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    while True:

        # Get  user response and make sure it's lowercase
        user_response =input(question) . lower()


        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as 
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        print("please enter a valid answer")
        continue

#compares user / computer choice and returns
# results ( win / lose / tie)
def rps_compare(user, comp):
   
    # If the user and thye computer choice is the same, it's a tie
    if user == comp:
        result = "tie"

    # There are three ways to win 
    elif user == " paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
       result = "win"
    elif user == "rock" and comp == "scissors":
        result = " win"
    

    # if it's not a win/ tie, then it's a loss
    else:
        result = "lose"

    return result

# Main routine starts here


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
want_instruction = string_checker("Do you want to read the instruction? ", ('yes', 'no'))

# checks user enter yes (y) or no(n)
if want_instruction == "yes":
    print("instructions go here")

    # Ask user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop ends here
while rounds_player < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_player + 1} (Infinite Mode) "
        num_rounds += 1
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_player + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)

    # randomly choose from the rps list(excluding the exit code)
    comp_choice = random. choice(rps_list[:-1])
    print(" Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose...:", rps_list)
    # print("you chose", user_choice)

    # If user choice is the exit code , break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tie += 1
        feedback = "👔👔 It's a tie! 👔👔"
    elif result == "lose":
        rounds_lost += 1 
        feedback = "😥😥 You lose. 😥😥"
    else:
        feedback = "👍👍 You won. 👍👍"

    # Set up to the game and output it user.
    # Add it to the game history list (include the round number)
    rounds_player += 1
    round_feedback = (f"{user_choice} vs {comp_choice}, {feedback}")
    history_item = f"Round:{rounds_player} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)



# Game loop ends here

# Game History / Statistics

# Calculate Statistics
rounds_won = rounds_player - rounds_tie - rounds_lost
percent_won = rounds_won / rounds_player * 100
percent_lost = rounds_lost / rounds_player * 100
percent_tied = 100 - percent_won - percent_lost

# Output Game statistics 
print("📊📊📊 Game Sattistics 📊📊📊")
print(f"👍 Won: {percent_won:.2f} \t "
      f"😥 Lost: {percent_lost:.2f} \t "
      f"👔 Tied: {percent_tied:.2f}")

# ask the user if they want to see their game history and output it if requested.
see_history = string_checker("\nDo you want to see your game history? ", ('yes', 'no'))
if see_history == "yes":
    for item in game_history:
        print(item)

    print()
    print("Thanks for playing. ")

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")




        
