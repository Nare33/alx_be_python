def main():
    """Prompts user for size and draws a square pattern."""

    while True:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
            except ValuueErroe:
                print("Invalid input. please enter a number.")

                for row in range(size):
                    for col in range(size):
                        print ("*", end="")
                        print()

                        if __name__ == "__main__":
                            main()
