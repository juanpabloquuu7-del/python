import json

def cargar_datos_prestamo(nom_archivo="reportes.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
    
def guardar_datos_prestamo(datos, nom_archivo="reportes.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception:
        datos = {}