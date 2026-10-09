import math

# functions


def string_check(question, valid_ans_list, num_letters):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")



def angle_check(question, angle_type, exit_code):
    """Checks users enter an integer between two values or unknown"""

    if angle_type == 'radians':
        high = math.radians(90)
    else:
        high = 90

    error = f"Oops - please enter a number greater than 0 and less than {high}, or 'unknown'."

    while True:
        response = input(question).lower()

        if response == exit_code:
            response = None
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = float(response)
            if 0 < response < high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


angle_type = string_check("Radians or Degrees? ", ['radians', 'degrees'], 1)
angle = angle_check("What is the value of the interior angle? ", angle_type, "unknown")

print(angle)
