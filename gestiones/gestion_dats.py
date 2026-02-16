import json

def cargar_datos(ruta="json/vecinos.json"):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        
        return {"001": {"nombre": "Admin", "apellidos": "Principal", "tipo_de_usuario": "Administrador"}}

def guardar_datos(datos, ruta="json/vecinos.json"):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)