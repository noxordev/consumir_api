import model
import view

def seleccionar_categoria():
    lista_diccionarios = model.crear_diccionario(model.obtener_categorias())
    view.imprimir_diccionario(lista_diccionarios)
    seleccion = view.pedir_seleccion()
    if not seleccion.isdigit():
        view.mostrar_error("Tienes que escribir un numero")
        return None
    valor = model.buscar_por_clave(lista_diccionarios, int(seleccion))
    if valor is None:
        view.mostrar_error("El numero no es valido")
        return None
    view.mostrar_seleccion(valor)
    return valor

def ejecutar():
    categoria = seleccionar_categoria()
    if categoria:
        view.mostrar_joke(model.obtener_joke(categoria))
