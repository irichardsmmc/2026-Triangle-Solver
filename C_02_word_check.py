# functions
def word_check(question):

    """Checks user input is only letters or is blank"""

    error = "Please only enter letters or leave blank"

    while True:

        response = input(question)

        if response.isalpha() or response == "":
            return response
            
        else:
            print(error)

# main routine

while True:

    word_check("Enter a string: ")
