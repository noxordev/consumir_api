def imprimir_diccionario(lista_diccionarios): #muestra el menu de opciones
    for elemento in lista_diccionarios:
        print(f"{elemento['clave']} - {elemento['valor']}")

def pedir_seleccion():
    return input("Seleccione un numero de la lista: ")

def mostrar_seleccion(valor):
    print(f"Seleccionaste {valor}")

def mostrar_joke(joke):
    print("chiste:", joke)

def mostrar_error(mensaje):
    print(mensaje)
