from utils import validate_day, is_pensioneer
from constants import TEST_BASE_PRICE

class CinemaRoom:

    def __init__(self):
        self._seats = []

    def add_seat(self, seat):
        if self._find_seat_by_number_and_row(seat.number, seat.row):
            raise ValueError(f"El asiento en la fila {seat.row}, número {seat.number} ya está registrado.")
        
        self._seats.append(seat)

    def search_seat(self, number, row):
        seat = self._find_seat_by_number_and_row(number, row)
        if not seat:
            raise ValueError(f"El asiento en la fila {row}, número {number} no está registrado.")
        return seat
    
    def reserve_seat(self, number, row, age, day):
        seat = self._find_seat_by_number_and_row(number, row)
        if not seat:
            raise ValueError(f"El asiento en la fila {row}, número {number} no está registrado.")
        
        if seat.reserved:
            raise ValueError(f"El asiento en la fila {row}, número {number} ya está reservado.")
        
        seat.price = self._apply_discounts(TEST_BASE_PRICE, age, day)
        seat.reserved = True
        print(f"El asiento en la fila {row}, número {number} ha sido reservado con éxito.")

    def cancel_reservation(self, number, row):
            seat = self._find_seat_by_number_and_row(number, row)
            if not seat:
                raise ValueError(f"El asiento en la fila {row}, número {number} no está registrado.")
            
            if not seat.reserved:
                raise ValueError(f"El asiento en la fila {row}, número {number} no está reservado.")
            
            seat.reserved = False
            print(f"La reserva del asiento en la fila {row}, número {number} se ha cancelado correctamente.")


    def show_seats(self):
        print(f"{'Fila':^10}{'Número':^10}{'Estado':^15}{'Precio (€)':^10}")
        print("-" * 45)
        
        for seat in self._seats:
            status = "Reservado" if seat.reserved else "Disponible"
            price = f"{seat.price:.2f} €"
            print(f"{seat.row:^10}{seat.number:^10}{status:^15}{price:^10}")



    def find_seat(self, number, row):
        return self._find_seat_by_number_and_row(number, row)


    def _apply_discounts(self, base_price, age, day):
        validate_day(day)

        if is_pensioneer(age):
            base_price *= 0.7
        elif day.lower() == "miércoles" or day.lower() == "miercoles":
            base_price *= 0.8
        
        return base_price
    
    def _find_seat_by_number_and_row(self, seat_number, seat_row):
        for existing_seat in self._seats:
            if existing_seat.number == seat_number and existing_seat.row == seat_row:
                return existing_seat
        return None
