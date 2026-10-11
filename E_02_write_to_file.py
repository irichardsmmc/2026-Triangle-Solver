from pathvalidate import is_valid_filename

# Functions
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


def validate_file_name():

    while True:

        file_name = input("File Name: ")

        if is_valid_filename(file_name):

            return file_name
        
        else:

            print("Invalid Filename")


# Main Routine

while True:
    save_data = string_check("Would you like to save your data to a file? ", ['yes', 'no'], 1)

    if save_data == 'yes':

        # Create file to hold data
        file_name = validate_file_name()
        write_to = "{}.txt".format(file_name)

        text_file = open(write_to, "w+")

        # Strings to write to file
        heading = "=== Triangle Solver ==="
        stuff = "Stuff"
        other_stuff = "Other stuff"

        # List of strings
        to_write = [heading, stuff, other_stuff]

        # Print output
        for item in to_write:
            print(item + '\n')

        # Write item to file
        for item in to_write:
            text_file.write(item)
            text_file.write("\n")
