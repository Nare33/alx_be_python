def main():
    """Prompts user for a number and prints its multiplication table."""

    number = int(input("Enter a number to see its multiplication table: "))

    print(f"Multiplication table for {number}:")

    for i in range(1,11):
        product = number * i
        print(f"{number} * {i} = {product}")

        if __name == "__main__":
            main()
