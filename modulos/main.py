"""
mostrar un menu


tomar input -> validarlo -> mostar/hacer algo

"""
from console_output import mostrar_menu
from validar_datos import validar_numero_entre, validar_edad, validar_nombre_o_apellido
import os

def aplicacion():
    
    ejecutando = True
    nombre = None
    apellido = None
    
    while  ejecutando:
        mostrar_menu()
        numero = input('ingrese una opcion: ')
        opcion_int =validar_numero_entre(numero,1,4)
        
        match opcion_int:
            case 1:
                nombre = input('ingrse su nombre: ')
                nombre = validar_nombre_o_apellido(nombre, 'incorrecto, escriba de nuevo')
                
                apellido = input('ingrse su apellido:')
                apellido = validar_nombre_o_apellido(apellido,'incorrecto, escriba de nuevo')
            case 2:
                if nombre != None and apellido != None:
                 print(f'hola {nombre}{apellido}')
                else:
                    print('primero debe ir la opcion 1. ')
            case 3:
                print('ahi va el genio del mundo mundial!!!gool!!')
            case 4:
                ejecutando = False
                print('saliendo del programa')
        os.system('pause')
        os.system('cls')   
aplicacion()        