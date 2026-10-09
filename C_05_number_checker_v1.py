# Functions go here

def num_check(question, exit_code=None):
    """Checks users enter a float that is more than
    zero"""

    error = "Oops - please enter a number more than zero, leave blank if unknown."

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to a float and check that it's more than zero
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine

# loop for testing
while True:
    print()

    my_num = num_check("Please enter a number more than 0: ", "")
    print(f"Thanks.  You chose {my_num}")

