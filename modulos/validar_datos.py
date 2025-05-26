

def validar_edad(edad: str) -> int:
    """
    Recibe una edad en formato string, valida que esté formada por números y que sea mayor o igual a 18.
    En caso de no cumplir, vuelve a pedir la edad hasta que sea válida.
    Retorna la edad parseada a entero.
    """
    while not edad.isdigit() or int(edad) < 18:
        edad = input('Ingrese su edad [solo mayores de 18 años]: ')
    return int(edad)


def validar_numero_entre(numero, min, max):
    """
    Valida que el usuario ingrese un número dentro del rango determinado (min y max).
    Retorna el número dentro del rango permitido, convertido a entero.
    """
    while not numero.isdigit() or not (min <= int(numero) <= max):
        numero = input(f"Ingrese un número válido entre {min} y {max}: ")

    numero_int = int(numero)
    return numero_int

    
def validar_nombre_o_apellido(nombre_o_apellido: str, mensaje: str) -> str:
    """
    Valida que el nombre o apellido contenga solamente letras.
    Args:
        nombre_o_apellido: La palabra a evaluar.
        mensaje: Mensaje que se muestra si la palabra no es válida.
    Returns:
        La palabra válida en caso de éxito.
    """
    while not nombre_o_apellido.isalpha():
        nombre_o_apellido = input(mensaje)
    return nombre_o_apellido
