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


# Main routine start here

# Intialise game variables
mode = "regular"
rounds_player = 0


print("💎📰✂ Rock / Paper / Scissors Game 💎📰✂")
print()

# Instruction 

# Ask user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    
    num_rounds = 5


# Game loop starts here
while rounds_player <= num_rounds:
    
    user_choice = input("Choose: ")
    if user_choice == "xxx":
        break
        
    rounds_player += 1
    print("rounds played: ", rounds_player)

        # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

print("We are done")

# Game loop ends here

# Game History / Statistics area
