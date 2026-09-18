import requests as consulta

def crear_diccionario(lista):
    lista_diccionarios = []
    num = 1
    for i in lista:
        lista_diccionarios.append({
            "clave": num,
            "valor": i
        }) #agrega el diccionario a la lista
        num += 1
    return lista_diccionarios

def imprimir_diccionario(lista_diccionarios): #muestra el menu de opciones
    for elemento in lista_diccionarios:
        print(f"{elemento['clave']} - {elemento['valor']}")

def seleccionar_diccionario(lista): #selecciona el diccionario de la lista
    lista_diccionarios = crear_diccionario(lista)
    imprimir_diccionario(lista_diccionarios)
    seleccion = input("Seleccione un numero de la lista: ")
    if not seleccion.isdigit():
        print("Tienes que escribir un numero")
        return None
    for elemento in lista_diccionarios:
        if int(seleccion) == elemento["clave"]:
            print(f"Seleccionaste {elemento['valor']}")
            return elemento["valor"]
    print("El numero no es valido")
    return None

def mostrar_joke(categoria):
    respuesta = consulta.get(f"https://api.chucknorris.io/jokes/random?category={categoria}")
    print("chiste:", respuesta.json()["value"])

categorias = consulta.get("https://api.chucknorris.io/jokes/categories")
lista_categorias = categorias.json()

categoria_elegida = seleccionar_diccionario(lista_categorias)
if categoria_elegida:
    mostrar_joke(categoria_elegida)

#print("codigo de respuesta:", response.status_code)
#print("headers de respuesta:", response.headers["Content-Type"])
#print("encoding de respuesta:", response.encoding)
#print("respuesta en json de value:", response.json()["value"])
#print("respuesta en texto:", response.text)
