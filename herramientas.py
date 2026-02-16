from gestiones.logs import registrar_evento

# Colores para que se vea nítido
RESET = "\033[0m"
BOLD = "\033[1m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AZUL = "\033[34m"
CYAN = "\033[36m"
AMARILLO = "\033[33m"

def agregar_herramientas(datos):
    print(f"\n{AZUL}{'='*50}{RESET}")
    print(f"{BOLD}⚒️  REGISTRAR NUEVA HERRAMIENTA{RESET}")
    print(f"{AZUL}{'='*50}{RESET}")
    
    cod = input("➤ Ingrese CÓDIGO único (ej: mart002): ").strip()

    if not cod:
        registrar_evento("INTENTO FALLIDO: Código vacío.", es_error=True)
        print(f"{ROJO}❌ Error: El código no puede estar vacío.{RESET}")
        return datos
    
    if cod in datos:
        registrar_evento(f"CONFLICTO: Código duplicado '{cod}'", es_error=True)
        print(f"{ROJO}❌ Error: El código '{cod}' ya existe (Pertenece a: {datos[cod]['nombre']}).{RESET}")
        return datos

    nombre = input("➤ Nombre: ").strip().capitalize()
    cat = input("➤ Categoría: ").strip().capitalize()
    
    try:
        stock = int(input("➤ Stock inicial: "))
        precio = int(input("➤ Precio/Valor: "))
    except ValueError:
        registrar_evento(f"ERROR DATOS: No numéricos en '{nombre}'", es_error=True)
        print(f"{ROJO}❌ Error: Stock y Precio deben ser números.{RESET}")
        return datos

    datos[cod] = {
        "nombre": nombre, "precio": precio, "stock": stock,
        "categoria": cat, "estado": "Activa"
    }
    
    registrar_evento(f"HERRAMIENTA NUEVA: {nombre} (ID: {cod})")
    print(f"\n{VERDE}✅ Éxito: Herramienta '{nombre}' registrada.{RESET}")
    input("\nPresione Enter para continuar...")
    return datos

def actualizar_herramienta(datos):
    print(f"\n{AZUL}{'='*50}{RESET}")
    print(f"{BOLD}🔄 ACTUALIZAR HERRAMIENTA{RESET}")
    print(f"{AZUL}{'='*50}{RESET}")

    cod_actual = input("➤ ID de la herramienta a modificar: ").strip()

    if cod_actual not in datos:
        registrar_evento(f"FALLO ACTUALIZACIÓN: ID '{cod_actual}' no existe.", es_error=True)
        print(f"{ROJO}❌ La herramienta no está registrada.{RESET}")
        return datos

    h = datos[cod_actual]
    print(f"\n{CYAN}Modificando: {BOLD}{h['nombre']}{RESET} (Deje en blanco para no cambiar)")

    try:
        nuevo_id = input(f"➤ Nuevo ID [Actual: {cod_actual}]: ").strip()
        nombre = input(f"➤ Nuevo nombre [Actual: {h['nombre']}]: ").strip().capitalize() or h['nombre']
        precio_input = input(f"➤ Nuevo precio [Actual: {h['precio']}]: ").strip()
        precio = int(precio_input) if precio_input else h['precio']
        stock_input = input(f"➤ Nuevo stock [Actual: {h['stock']}]: ").strip()
        stock = int(stock_input) if stock_input else h['stock']
        categoria = input(f"➤ Nueva categoría [Actual: {h['categoria']}]: ").strip().capitalize() or h['categoria']
        
        while True:
            est = input(f"➤ Nuevo estado (Activa/Reparacion/Fds) [Actual: {h['estado']}]: ").strip().capitalize()
            if not est: 
                estado = h['estado']
                break
            if est in ["Activa", "Reparacion", "Fds"]:
                estado = est
                break
            print(f"{ROJO}Estado no válido.{RESET}")

        # Si cambia el ID (la llave)
        final_id = nuevo_id if (nuevo_id and nuevo_id != cod_actual) else cod_actual
        
        info_nueva = {
            "nombre": nombre, "precio": precio, "stock": stock,
            "categoria": categoria, "estado": estado
        }

        if final_id != cod_actual:
            datos[final_id] = info_nueva
            del datos[cod_actual]
            registrar_evento(f"CAMBIO ID: {cod_actual} -> {final_id}")
        else:
            datos[cod_actual] = info_nueva

        registrar_evento(f"HERRAMIENTA ACTUALIZADA: {final_id}")
        print(f"\n{VERDE}✅ Actualización exitosa.{RESET}")

    except ValueError:
        registrar_evento(f"ERROR DATOS: Actualizando '{cod_actual}'", es_error=True)
        print(f"{ROJO}❌ Error: Precio y stock deben ser números.{RESET}")

    input("\nPresione Enter para continuar...")
    return datos

def buscar_herramientas(datos):
    while True:
        print(f"\n{AZUL}{'='*60}{RESET}")
        print(f"{BOLD}🔍 BUSCADOR DE INVENTARIO{RESET}")
        print(f"{AZUL}{'='*60}{RESET}")
        
        prd = input("➤ Ingrese categoría o nombre a buscar: ").strip().lower()
        print(f"\n{BOLD}{'ID':<12} | {'NOMBRE':<18} | {'CATEGORÍA':<15} | {'STOCK'}{RESET}")
        print("-" * 60)

        encontrado = False
        for k, v in datos.items():
            if prd in v['categoria'].lower() or prd in v['nombre'].lower() or prd == k.lower():
                # Color según stock
                color_stk = VERDE if v['stock'] > 0 else ROJO
                print(f"{k:<12} | {v['nombre'][:18]:<18} | {v['categoria'][:15]:<15} | {color_stk}{v['stock']}{RESET}")
                encontrado = True

        if not encontrado:
            print(f"{ROJO}No hay coincidencias.{RESET}")
        
        rta = input("\n¿Seguir buscando? (Si/No): ").strip().capitalize()
        if rta != "Si":
            break

def mostrar_herramientas(datos):
    print(f"\n{AZUL}{'='*65}{RESET}")
    print(f"{BOLD}📦 INVENTARIO COMPLETO DE HERRAMIENTAS{RESET}")
    print(f"{AZUL}{'='*65}{RESET}")

    if not datos:
        print(f"{ROJO}Inventario vacío.{RESET}")
        return

    # Encabezado tipo tabla
    print(f"{BOLD}{'ID':<12} | {'NOMBRE':<15} | {'CATEGORÍA':<12} | {'STOCK':<6} | {'ESTADO'}{RESET}")
    print("-" * 65)

    for id_h, v in datos.items():
        color_estado = VERDE if v['estado'] == "Activa" else AMARILLO if v['estado'] == "Reparacion" else ROJO
        print(f"{id_h:<12} | {v['nombre'][:15]:<15} | {v['categoria'][:12]:<12} | {v['stock']:<6} | {color_estado}{v['estado']}{RESET}")
    
    print(f"{AZUL}{'='*65}{RESET}")
    input("\nPresione Enter para volver...")

def eliminar_herramienta(datos):
    print(f"\n{ROJO}{'='*50}{RESET}")
    print(f"{BOLD}🗑️  ELIMINAR HERRAMIENTA{RESET}")
    print(f"{ROJO}{'='*50}{RESET}")

    id_elim = input("➤ ID de la herramienta a borrar: ").strip()

    if id_elim not in datos:
        registrar_evento(f"FALLO ELIMINAR: ID '{id_elim}' no existe", es_error=True)
        print(f"{ROJO}❌ ID no encontrado.{RESET}")
        return

    h = datos[id_elim]
    print(f"\n⚠️  ATENCIÓN: Vas a eliminar '{BOLD}{h['nombre']}{RESET}'")
    confirm = input("¿Confirmar eliminación? (s/n): ").lower()

    if confirm == 's':
        registrar_evento(f"HERRAMIENTA ELIMINADA: {h['nombre']} (ID: {id_elim})", es_error=True)
        datos.pop(id_elim)
        print(f"{VERDE}✅ Eliminada correctamente.{RESET}")
    else:
        print(f"{CYAN}Acción cancelada.{RESET}")
    input("\nPresione Enter...")

def inavilitar_herramienta(datos):
    print(f"\n{AMARILLO}{'='*50}{RESET}")
    print(f"{BOLD}⚠️  INHABILITAR POR FUERA DE SERVICIO{RESET}")
    print(f"{AMARILLO}{'='*50}{RESET}")

    id_h = input("➤ ID de la Herramienta: ").strip()
    
    if id_h not in datos:
        registrar_evento(f"FALLO FDS: ID '{id_h}' inexistente", es_error=True)
        print(f"{ROJO}❌ No existe.{RESET}")
        return datos

    h = datos[id_h]
    print(f"➤ Herramienta: {BOLD}{h['nombre']}{RESET}")
    confirmar = input("¿Marcar como Fuera de Servicio (FDS)? (Si/No): ").strip().capitalize()

    if confirmar == "Si":
        stock_ant = h['stock']
        h['estado'] = "Fds"
        h['stock'] = 0
        registrar_evento(f"FDS: {h['nombre']} (ID: {id_h}). Stock {stock_ant} -> 0", es_error=True)
        print(f"{VERDE}✅ Herramienta inhabilitada y stock puesto en 0.{RESET}")
    else:
        print(f"{CYAN}Acción cancelada.{RESET}")
    
    input("\nPresione Enter...")
    return datos