def find_second_largest():
    try:
        # Read space-separated numbers from user input
        user_input = input("Enter student marks separated by spaces: ")

        # Convert input string into a list of integers
        marks = [int(x) for x in user_input.split()]

        # Remove duplicates using a set
        unique_marks = list(set(marks))

        # If less than 2 unique elements exist, print -1
        if len(unique_marks) < 2:
            print("-1")
            return

        # Sort the unique marks in descending order
        unique_marks.sort(reverse=True)

        # Print the second largest element
        print(unique_marks[2])

    except ValueError:
        print("Please enter valid integers only.")


# Run the function
find_second_largest()
