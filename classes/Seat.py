from constants import TEST_BASE_PRICE

class Seat:
    def __init__(self, number, row):
        self.number = number
        self.row = row
        self.reserved = False
        self.price = TEST_BASE_PRICE
        
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if number <= 0:
            raise ValueError("El número del asiento debe ser positivo.")
        self._number = int(number)
    
    @property
    def row(self):
        return self._row
    
    @row.setter
    def row(self, row):
        if row <= 0:
            raise ValueError("La fila debe ser positiva.")
        self._row = int(row)
    
    @property
    def reserved(self):
        return self._reserved
    
    @reserved.setter
    def reserved(self, reserved):
        self._reserved = bool(reserved)
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price is not None and price < 0:
            raise ValueError("El precio debe ser positivo.")
        self._price = float(price) if price is not None else None
    
    def __str__(self):
        return f"\
            {"*"*30}\n\
            * Fila: {self.row:>20} *\n\
            * Número: {self.number:>18} *\n\
            * Reservado: {"Sí" if self.reserved else "No":>15} *\n\
            * Precio: {self.price if self.price is not None else "No asignado":>18.2f} *\n\
            {"*"*30}"
