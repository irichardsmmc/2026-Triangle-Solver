from pathvalidate import is_valid_filename

def validate_file_name():

    while True:

        file_name = input("File Name: ")

        if is_valid_filename(file_name):

            return file_name
        
        else:

            print("Invalid Filename")

validate_file_name()
