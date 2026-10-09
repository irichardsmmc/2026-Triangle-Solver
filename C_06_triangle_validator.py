import math

# Functions
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

# Main routine

print(validate_right_triangle(a=3, b=4, c=5, theta=None))
print(validate_right_triangle(a=3, b=4, c=None, theta=None))
print(validate_right_triangle(a=5, b=None, c=3, theta=None))
print(validate_right_triangle(a=3, b=4, c=10, theta=None))
