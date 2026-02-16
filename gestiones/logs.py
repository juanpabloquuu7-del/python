def registrar_evento(mensaje, es_error=False):
    """Escribe acciones en un archivo .txt para auditoría."""
    tipo = "[ERROR]" if es_error else "[EVENTO]"
    
    log_linea = f"{tipo}: {mensaje}\n"
    
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(log_linea)
    except:
        pass

def ver_logs():
    """Muestra el contenido de la bitácora en pantalla."""
    print("\n--- REGISTRO DE ACTIVIDADES ---")
    try:
        with open("logs.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No hay eventos registrados.")
    input("\nPresione Enter para continuar...")