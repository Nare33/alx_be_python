def main():
    """Prompts user for size and draws a square pattern of asterisks."""

    while True:
        try:
            size = int(input("Enter the size of the pattern (positive interger): "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print ("Invalid input. Please enter a number.")

            for row in range(size):
                for col in range(size):
                    print("*", end="")
                    print()

                    if __name == "__main__":
                        main()
