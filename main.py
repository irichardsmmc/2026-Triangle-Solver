from pathvalidate import is_valid_filename
import math

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


def instructions():

    print('''
    
--- Instructions ---

1. Choose to either solve a triangle or exit the program.

2. Enter a unit of measurement, or leave blank.
          
3. Choose either radians or degrees.
          
4. Enter the value of the interior angle, leave blank if unknown.
          
5. Give the length of the sides, leave blank if unknown.
          
6. The result is then printed, and step 1 will be repeated.
          
7. Once the program has been exited, you will be asked if you want to save data to a file.

8. If you have chosen yes, you must enter a valid filename.
         
9. The file will then be saved, and the program will exit.
    ''')


def word_check(question):

    """Checks user input is only letters or is blank"""

    error = "Please only enter letters or leave blank"

    while True:

        response = input(question)

        if response.isalpha() or response == "":
            return response
            
        else:
            print(error)


def angle_check(question, angle_type, exit_code=None):
    """Checks users enter an integer between two values or unknown"""

    if angle_type == 'radians':
        high = math.radians(90)
    else:
        high = 90

    error = f"Oops - please enter a number greater than 0 and less than {high}, or leave blank if unknown."

    while True:
        response = input(question).lower()

        if response == exit_code:
            response = None
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = float(response)
            if 0 <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


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


def validate_right_triangle(a=None, b=None, c=None, theta=None):

    sides = []

    for side in [a, b, c]:
        if side is not None:
            sides.append(side)

    for item in sides:
        if item <= 0:
            return False

    num_sides = len(sides)

    # Less than 2 sides, check for angle

    if num_sides == 0:
        return False

    elif num_sides == 1:
        
        if theta is not None:
            return True
        else:
            return False
    
    # Hypotenuse must be bigger than the other side
    elif num_sides == 2:
        if c is not None:
            if a is not None:
                known_side = a
            else:
                known_side = b
        
            if c <= known_side:
                return False
        
        return True
    
    else:

        if a + b <= c:
            return False
        
        if math.isclose(a ** 2 + b ** 2, c ** 2):
            return True
        
        else:
            return False


def calculations(opp, adj, hyp, theta):

    if theta is not None:

        theta = math.radians(theta)

    while any(item is None for item in [opp, adj, hyp, theta]):

        num_known_sides = sum(side is not None for side in [opp, adj, hyp])

        if num_known_sides >= 2:
            if hyp is None:
                hyp = math.sqrt(opp ** 2 + adj ** 2)
            if opp is None:
                opp = math.sqrt(hyp ** 2 - adj ** 2)
            if adj is None:
                adj = math.sqrt(hyp ** 2 - opp ** 2)

        if theta is None:
            if hyp is not None:
                if opp is not None:
                    theta = math.asin(opp / hyp)
                elif adj is not None:
                    theta = math.acos(adj / hyp)
            elif opp is not None and adj is not None:
                theta = math.atan(opp / adj)

        else:
            if opp is None:
                if adj is not None:
                    opp = adj * math.tan(theta)
                if hyp is not None:
                    opp = hyp * math.sin(theta)

            if adj is None:
                if hyp is not None:
                    adj = hyp * math.cos(theta)
                if opp is not None:
                    adj = opp / math.tan(theta)

            if hyp is None:
                if opp is not None:
                    hyp = opp / math.sin(theta)
                if adj is not None:
                    hyp = adj / math.cos(theta)

    return opp, adj, hyp, theta
        

def validate_file_name():

    while True:

        file_name = input("File Name: ")

        if is_valid_filename(file_name):

            return file_name
        
        else:

            print("Invalid Filename")


# Main Routine

# Initialise variables
side_list = ['opposite', 'adjacent', 'hypotenuse']
data = []
triangle = 0

print("\n=== Right angle triangle solver ===\n")

if string_check("Would you like to see the instructions? ", ['yes', 'no'], 1) == "yes":
    instructions()

while True:

    # Check if users want to solve a triangle or exit program
    start = string_check("Solve a triangle? ", ['yes', 'no'], 1)

    if start == 'no':

        break

    side_values = []
    num_known_sides = 0
    triangle += 1

    # Get unit for side lengths
    unit = word_check("What unit are the lengths of the sides in? ")

    if unit == '':

        unit = ' units'

    else:

        unit = ' ' + unit

    # Check if angle is in radians or degrees
    angle_type = string_check("Radians or Degrees? ", ['radians', 'degrees'], 1)

    # Get angle
    theta = angle_check("What is the value of the interior angle? ", angle_type, '')

    # Get sides if avaliable
    for item in side_list:

        side = num_check(f"What is the length of the {item}? ", '')

        if side == "":

            side = None
            
        side_values.append(side)
        
    # Validate triangle
    if not validate_right_triangle(a=side_values[0], b=side_values[1], c=side_values[2], theta=theta):

        print("Triangle cannot be solved.")

        is_solved = 'Not Solved'

    else:
        
        # calculations
        side_values[0], side_values[1], side_values[2], theta = calculations(side_values[0], side_values[1], side_values[2], theta)

        is_solved = 'Solved'

    for index, item in enumerate(side_values):

        if item is None:

            side_values[index] = "Unknown"

        else:

            if item.is_integer():

                item = int(item)

            side_values[index] = str(item) + unit

    if angle_type == 'degrees':

        angle_unit = '°'
        theta = math.degrees(theta)

    else:

        angle_unit = ' radians'

    if theta is None:

        theta = "Unknown"

    else:

        theta = f'{theta:g}{angle_unit}'

    output = f'Opposite: {side_values[0]}, Adjacent: {side_values[1]}, Hypotenuse: {side_values[2]}, Angle: {theta}'

    print('\n' + output)

    data.append(f"Triangle {triangle} ({is_solved}): {output}")

if data != []:

    print("\n--- History ---\n")

    for item in data:

        print(item)
    
    save_data = string_check("Would you like to save your data to a file? ", ['yes', 'no'], 1)

    if save_data == 'yes':

        # Create file to hold data
        file_name = validate_file_name()
        write_to = "{}.txt".format(file_name)

        text_file = open(write_to, "w+")

        # Strings to write to file
        heading = "=== Triangle Solver ===\n"

        # List of strings
        to_write = [heading, data]

        # Print output
        for item in to_write:
            print(item)

        # Write item to file
        for item in to_write:
            text_file.write(item)
            text_file.write("\n")
