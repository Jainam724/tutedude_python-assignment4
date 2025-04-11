def read_file():
    try:
        with open("sample.txt", "r") as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_file()
