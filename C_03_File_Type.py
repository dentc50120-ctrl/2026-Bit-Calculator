# asks users for file type (integer / image / text / xxx)

def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for text...
        elif response in ["text", 'txt', 't']:
            return "text"

        # check for image...
        elif response in ["image", 'picture', 'p', 'img']:
            return "image"

        # if the response is invalid output and error
        else:
            print("Please enter a valid file type")




# Main routine goes here
while True:
    file_type = get_filetype()
    print(f"You chose {file_type}")

    if file_type == "xxx":
        break

