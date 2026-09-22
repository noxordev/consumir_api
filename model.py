import requests as consulta

URL_CATEGORIAS = "https://api.chucknorris.io/jokes/categories"
URL_JOKE = "https://api.chucknorris.io/jokes/random"

def obtener_categorias():
    respuesta = consulta.get(URL_CATEGORIAS)
    return respuesta.json()

def obtener_joke(categoria):
    respuesta = consulta.get(f"{URL_JOKE}?category={categoria}")
    return respuesta.json()["value"]

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

def buscar_por_clave(lista_diccionarios, clave):
    for elemento in lista_diccionarios:
        if elemento["clave"] == clave:
            return elemento["valor"]
    return None
