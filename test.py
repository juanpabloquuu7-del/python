
VERDE = "\033[32m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
from gestiones.gestion_datos_herramientas import cargar_datos_herramienta
from gestiones.gestion_test import guardar_datos_test, cargar_datos_test
datos_h = cargar_datos_herramienta("json/herramientas.json")
datos_t = cargar_datos_test("json/test.json")
def dar_baja(datos_h,guardar_datos_test,datos_t):

    print("Registrar baja de herramientas")

    if not datos_h:
        print("Inventario vacío.")
        return datos_h

    # Encabezado tipo tabla
    print(f"{'ID':<12} | {'NOMBRE':<15} | {'ESTADO'}")
    print("-" * 65)

    for id_baja, v in datos_h.items():
        color_estado = VERDE if v['estado'] == "Activa" else AMARILLO if v['estado'] == "Reparacion" else ROJO
        print(f"{id_baja:<12} | {v['nombre'][:15]:<15}  | {color_estado}{v['estado']}")
    
    print(f"{'='*65}")
    
    id_baja = input("\n➤Seleccione ID de herramienta a dar de baja")
    if not id_baja :
        print("❌ El id es obligatorio.")
        input("presiona enter para continuar")
        return datos_h
    if id_baja not in datos_h:
        print(f"FALLO EN DAR BAJA: ID '{id_baja}' no existe.")
        print(f"{ROJO}❌ La herramienta no está registrada.")
        input("presiona enter para continuar")
        return datos_h
    

    print(f"Use formato DD/MM/AAAA (ej: 24/12/2024)")
    f_ini = input("➤ Fecha en la que se dio de baja: ").strip()
    if not f_ini:
        print(f"❌ La fecha es obligatorio.")
    
        return datos_h
    estado = "dada de baja"
    motivo = input("➤Ingrese el motivo por el cual se da de baja")
    nombre = "martillo"
    datos_t[id_baja] = {
        "id_baja": id_baja, "nombre": nombre, "estado": estado, "fecha_baja": f_ini,
        "motivo": motivo
    }
    print("Herramientas dadas de baja")
    print("=" * 65)
    print(f"{'ID':<12} | {'NOMBRE':<15} | {'FECHA DE BAJA':<20} | {'MOTIVO':<25}")
    print("-" * 65)

    for id_baja, v in datos_t.items():
        
            print(f"{id_baja:<12} | {v['nombre'][:15]:<15}  | {f_ini:<20}| {motivo:<25}")
    opcion =  input("deseas guardar estos datos(si/no)")
    if opcion == "si":
        guardar_datos_test(datos_t)

dar_baja(datos_h,guardar_datos_test,datos_t)

