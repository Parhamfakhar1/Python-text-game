def intro():
    print("Welcome to the Adventure!")
    print("You are in a dark forest. You see two paths.")

def game():
    intro()
    while True:
        print("\nChoose a path:")
        print("1. Left path")
        print("2. Right path")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '0':
            print("Exiting the game. Goodbye!")
            break
        elif choice == '1':
            print("You walk along the left path and find a treasure chest!")
        elif choice == '2':
            print("You walk along the right path and encounter a wild animal!")
        else:
            print("Invalid choice!")

def main():
    game()

if __name__ == '__main__':
    main()
