import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wait_for_continue(custom_msg=None):
    if custom_msg:
        input(f"\n{custom_msg} Pulse Enter para continuar...")
    else:
        input("\nPulse Enter para continuar...")
    clear()


def validate_day(day):
    valid_days = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]
    if day != None and day.lower() not in valid_days:
        raise ValueError(f"El día \"{day}\" no es válido. Por favor, ingrese un día de la semana.")
    return day
    
def validate_age(age):
    if age is None:
        raise ValueError("Error: La edad no puede estar vacía.")
    if not str(age).isdigit():
        raise ValueError("Error: La edad debe ser un número entero.")
    return int(age)
    
def is_pensioneer(age):
    return age > 65
