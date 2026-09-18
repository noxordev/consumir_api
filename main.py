from multiprocessing import Value
import requests as consulta

categorias = consulta.get("https://api.chucknorris.io/jokes/categories")
print("categorias:", categorias.json())

lista_categorias = categorias.json()
print("ultimo dato de la lista de categorias:", lista_categorias[-1])

response = consulta.get("https://api.chucknorris.io/jokes/random?category=animal")

print("codigo de respuesta:", response.status_code)
print("headers de respuesta:", response.headers["Content-Type"])
print("encoding de respuesta:", response.encoding)
print("respuesta en json de value:", response.json()["value"])
print("respuesta en texto:", response.text)