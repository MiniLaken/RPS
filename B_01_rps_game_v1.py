# checks for an integer more than 0 (allows <enter>)
def int_checker():
    while True:
        error = " Please enter an integer that is 1 or more."

        to_check = input()

        # check for infinte mode
        if to_check == "":
            return "infinite"

        try:
            response = int()

            # checks that the number is more than / equal to 13
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

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5


# Game loop starts here
while rounds_player <= num_rounds:
    input("Choose: ")
    rounds_player += 1

    # if users are in infinite mode, increase number of rounds!
    num_rounds += 1


# Game loop ends here

# Game History / Statistics area
