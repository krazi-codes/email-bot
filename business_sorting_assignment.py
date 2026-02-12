def print_menu():
    """Displays the main menu options."""
    print("1. Sort List")
    print("2. Exit")


def get_choice():
    """Prompts the user for a choice and validates input."""
    choice = input("Enter your choice: ")
    while choice not in ['1', '2']:
        print("Invalid choice, please try again.")
        choice = input("Enter your choice: ")
    return choice


def sort_2d_list(data):
    """Sorts a 2D list based on the first column."""
    return sorted(data, key=lambda x: x[0])


def interactive_sorting():
    """Main interaction function for 2D list sorting."""
    data = [
        ["Alice", 30],
        ["Bob", 25],
        ["Charlie", 35]
    ]
    print("Original Data:")
    for row in data:
        print(row)

    while True:
        print_menu()
        choice = get_choice()
        if choice == '1':
            sorted_data = sort_2d_list(data)
            print("Sorted Data:")
            for row in sorted_data:
                print(row)
        elif choice == '2':
            print("Exiting...")
            break


if __name__ == '__main__':
    interactive_sorting()