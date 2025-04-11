def write_to_file():
    try:
        user_input = input("Enter some text to write to the file: ")
        with open("output.txt", "w") as file:
            file.write(user_input + "\n")

        additional_input = input("Enter some additional text to append to the file: ")
        with open("output.txt", "a") as file:
            file.write(additional_input + "\n") 

        with open("output.txt", "r") as file:
            print("\n--- Final content of the file ---")
            print(file.read())

    except Exception as e:
        print(f"An error occurred: {e}")

write_to_file()
