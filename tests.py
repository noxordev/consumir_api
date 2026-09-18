list = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

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

print(crear_diccionario(list))

def imprimir_diccionario(lista):
    for lista in crear_diccionario(list):
        print(f"{lista['clave']} - {lista['valor']}") #imprime la resta de la clave y el valor

imprimir_diccionario(list)

def seleccionar_diccionario(list): #selecciona el diccionario de la lista
    seleccion = input("Seleccione un numero de la lista: ")
    for list in crear_diccionario(list):
        if int(seleccion) == int(list["clave"]):
            print(f"tu seleccionaste {list['valor']}")
            break
    else:
        print("El numero no es valido")

seleccionar_diccionario(list)