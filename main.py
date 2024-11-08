import sys
from utils import clear
from classes.CinemaRoom import CinemaRoom
from classes.Seat import Seat
from utils import wait_for_continue, is_pensioneer, validate_age
from constants import MENU_OPTIONS, LIMIT_ROOM_ROWS, LIMIT_SEATS_PER_ROW

def get_seat_details(multi = False):
    try:
        clear()
        row_input = input(f"Ingrese el número de fila (solo hay {LIMIT_ROOM_ROWS}): ")
        if not row_input.strip():  # Si está vacío o solo tiene espacios
            raise ValueError("El número de fila no puede estar vacío.")
        row = int(row_input)
        if row <= 0 or row > LIMIT_ROOM_ROWS:
            raise ValueError(f"La fila debe estar entre 1 y {LIMIT_ROOM_ROWS}.")
        
        number_input = input(f"Ingrese el número de asiento (solo hay {LIMIT_SEATS_PER_ROW}): ")
        if not number_input.strip():  # Si está vacío o solo tiene espacios
            raise ValueError("El número de asiento no puede estar vacío.")
        number = int(number_input)
        if number <= 0 or number > LIMIT_SEATS_PER_ROW:
            raise ValueError(f"El número del asiento debe estar entre 1 y {LIMIT_SEATS_PER_ROW}.")
        
        return row, number
    except ValueError as e:
        wait_for_continue(f"Error: {e}")
        return None, None


def show_menu():
    print("\n--- Sistema de Gestión de Cine ---\n")
    for index, (key, description) in enumerate(MENU_OPTIONS.items(), start=1):
        print(f"{index}. {description}")

def add_seat(cinema_room):
    row, number = get_seat_details()
    if row is not None and number is not None:
        seat = Seat(number, row)
        try:
            cinema_room.add_seat(seat)
            wait_for_continue("Asiento añadido correctamente.")
        except ValueError as e:
            wait_for_continue(f"Error al añadir el asiento: {e}")

def add_multiple_seats(cinema_room):
    try:
        clear()
        print("Añadir múltiples asientos:")

        num_rows, num_seats = get_seat_details(multi=True)

        if num_rows is not None and num_seats is not None:
            added_seats = 0
            for row in range(1, num_rows + 1):
                for seat_num in range(1, num_seats + 1):
                    if not cinema_room.find_seat(seat_num, row):
                        seat = Seat(seat_num, row)
                        cinema_room.add_seat(seat)
                        added_seats += 1
                    else:
                        print(f"\nYa existe el asiento {seat_num} en la fila {row}")
            
            wait_for_continue(f"Se han añadido correctamente {added_seats} asientos.")
    except ValueError as e:
        wait_for_continue(f"Error: {e}")

def reserve_seat(cinema_room):
    row, number = get_seat_details()
    if row is not None and number is not None:
        try:
            age_input = input("Ingrese la edad del usuario: ")
            age = validate_age(age_input)
            day = None
            if not is_pensioneer(age):
                day = input("Ingrese el día de la semana: ")
            
            cinema_room.reserve_seat(number, row, age, day)
            wait_for_continue("Asiento reservado correctamente.")
        except ValueError as e:
            wait_for_continue(f"Error al reservar el asiento: {e}")


def cancel_reservation(cinema_room):
    row, number = get_seat_details()
    if row is not None and number is not None:
        try:
            cinema_room.cancel_reservation(number, row)
            wait_for_continue("Reserva cancelada correctamente.")
        except ValueError as e:
            wait_for_continue(f"Error al cancelar la reserva: {e}")

def search_seat(cinema_room):
    row, number = get_seat_details()
    if row is not None and number is not None:
        try:
            print(cinema_room.search_seat(number, row))
            wait_for_continue()
        except ValueError as e:
            wait_for_continue(f"Error al buscar el asiento: {e}")

def show_all_seats(cinema_room):
    clear()
    print("Listado de Asientos:")
    cinema_room.show_seats()
    wait_for_continue()

def main():
    cinema_room = CinemaRoom()
    
    actions = {
        "add": lambda: add_seat(cinema_room),
        "add_multiple": lambda: add_multiple_seats(cinema_room),
        "reserve": lambda: reserve_seat(cinema_room),
        "cancel": lambda: cancel_reservation(cinema_room),
        "show": lambda: show_all_seats(cinema_room),
        "search": lambda: search_seat(cinema_room),
    }

    clear()
    while True:
        show_menu()
        
        try:
            option = int(input("\nSeleccione una opción: "))
            index = option - 1
            if 0 <= index < len(MENU_OPTIONS):
                action_key = list(MENU_OPTIONS.keys())[index]
                if action_key == "exit":
                    clear()
                    print("Saliendo del sistema. ¡Gracias por usar el gestor de cine!")
                    sys.exit()
                actions[action_key]()
            else:
                wait_for_continue("Opción no válida. Por favor, intente nuevamente.")
        except ValueError:
            clear()
            wait_for_continue("Error: Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
