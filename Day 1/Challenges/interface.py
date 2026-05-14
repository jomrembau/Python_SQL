from database import create_database_and_tables, add_box, get_all_boxes, get_box
from tabulate import tabulate

def retrieve_numeric_input(called):
    input_ok = False
    n = None

    while not input_ok:
        n = input(f"\nEnter {called} ")

        try:
            n = float(n)
            input_ok = True

        except ValueError:
            print("Please provide a numeric input")

    return n


def add_box_menu():
    box_name = input("\nEnter a name for the box: ")
    box_height = retrieve_numeric_input(called="The box's height in meters: ")
    box_width = retrieve_numeric_input(called="The box's width in meters: ")
    box_length = retrieve_numeric_input(called="The box's length in meters: ")

    add_box(connection, (box_name, box_height,box_width, box_length))

def display_box_types():
    boxes = get_all_boxes(connection)

    print("\n" + tabulate(boxes,
        headers=["box_id", "box_name", "height", "width", "length"],
        tablefmt="psql" + "\n"
                            ))

def load_box_menu():
    n = input("Enter the name of the box: ")

    box = get_box(connection, by_name=n)

    if not box:
        print("A box by that name could not be found.")
    else:
        container_id = input("Enter the id of the container to load the box to: ")

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
                add_box_menu()

            case "2":
                display_box_types()

            case "3":
                load_box_menu()

            case "4":
                print("Choice 4 Selected")

            case "5":
                print("Choice 5 Selected")

            case "x":
                print("Goodbye!")

            case _:
                print("Invalid input")

if __name__ == "__main__":
    connection = create_database_and_tables(filename="freight_prod.db")
    main_menu()


