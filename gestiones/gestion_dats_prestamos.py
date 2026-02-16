import json

def cargar_datos_prestamo(ruta="json/prestamos.json"):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def guardar_datos_prestamo(datos, ruta="json/prestamos.json"):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)