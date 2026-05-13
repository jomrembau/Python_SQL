from database import create_database_and_tables

def main_menu():
    print("\nWelcome to Freight Manager")

    print("""
            1. Add a box type
            2. Show box types
            3. Load box to container
            4. Show container
            5. Summary Report
            x. Close
            """)

    n = 0

    while n != "x":
        n = input("\nYour Choice: ").lower()

        match n:
            case "1":
                print("Choice 1 Selected")

            case "2":
                print("Choice 2 Selected")

            case "3":
                print("Choice 3 Selected")

            case "4":
                print("Choice 4 Selected")

            case "5":
                print("Choice 5 Selected")

            case "x":
                print("Goodbye!")

            case _:
                print("Invalid input")

if __name__ == "__main__":
    create_database_and_tables(filename="freight_prod.db")
    main_menu()


