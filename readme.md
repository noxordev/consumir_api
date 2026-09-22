# Consumir API - Chuck Norris

Ejercicio de KeepCoding Programación 101: consumir una API con `requests`.

El programa pide las categorías de chistes a [chucknorris.io](https://api.chucknorris.io), las muestra como un menú numerado, y al elegir un número imprime un chiste aleatorio de esa categoría.

## Estructura

El código está separado en capas (MVC):

- `model.py` - llamadas a la API y transformación de datos.
- `view.py` - todo lo que imprime o pide input.
- `controller.py` - une las dos anteriores y valida la selección.
- `main.py` - punto de entrada.

## Uso

```powershell
.\entorno\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```
