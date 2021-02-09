import sys
from src import utility


def start_app():
    while True:
        print("Select one of the options from below: ")
        print("1. Input File")
        print("2. Exit")
        try:
            user_input = int(input())
            if user_input == 1:
                utility.get_file_input()
            else:
                raise KeyboardInterrupt

        except KeyboardInterrupt:
            sys.exit("Exited..")
        except:
            print("Please select valid input")
            continue


if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        sys.exit("Exiting the application..")
