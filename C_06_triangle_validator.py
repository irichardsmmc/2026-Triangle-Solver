import math

# Functions

def num_check(question, exit_code=None):
    """Checks users enter a float that is more than
    zero"""

    error = "Oops - please enter a number more than zero, leave blank if unknown."

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return None

        try:
            # Change the response to a float and check that it's more than zero
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def angle_check(question, angle_type, exit_code):
    """Checks users enter an integer between two values or unknown"""

    if angle_type == 'radians':
        high = math.radians(90)
    else:
        high = 90

    error = f"Oops - please enter a number greater than 0 and less than {high}, or leave blank."

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
            # Find known side, make sure theta is correct
            if a is not None:
                known_side = a
                if theta is not None:
                    opp = c * math.sin(theta)
                    if opp != a:
                        return False
            else:
                known_side = b
                if theta is not None:
                    adj = c * math.cos(theta)
                    if adj != b:
                        return False
        
            if c <= known_side:
                return False
        
        else:
            if theta is not None:
                opp = b * math.tan(theta)
                if opp != a:
                    return False
        
        return True
    
    else:

        if a + b <= c:
            return False
        
        if math.isclose(a ** 2 + b ** 2, c ** 2):
            if theta is None:
                return True
            else:
                hyp = a / math.sin(theta)

                if hyp == c:
                    return True
                else:
                    return False
        
        else:
            return False


# Main routine

print(validate_right_triangle(a=3, b=4, c=5, theta=None))
print(validate_right_triangle(a=3, b=4, c=5, theta=70))
print(validate_right_triangle(a=3, b=4, c=2, theta=None))
print(validate_right_triangle(a=5, b=8, c=3, theta=33))
print(validate_right_triangle(a=None, b=None, c=None, theta=None))
print(validate_right_triangle(a=8, b=None, c=None, theta=None))
print(validate_right_triangle(a=9, b=5, c=None, theta=None))
print(validate_right_triangle(a=7, b=None, c=None, theta=45))
print(validate_right_triangle(a=None, b=2, c=None, theta=30))
print(validate_right_triangle(a=None, b=None, c=5, theta=12))
print(validate_right_triangle(a=None, b=None, c=None, theta=10))
