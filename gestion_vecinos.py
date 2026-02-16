from gestiones.logs import registrar_evento
# Colores básicos para la terminal
RESET = "\033[0m"
BOLD = "\033[1m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AZUL = "\033[34m"
CYAN = "\033[36m"

def agregar_vecinos(datos):
    print(f"\n{AZUL}{'='*50}{RESET}")
    print(f"{BOLD}🆕 REGISTRAR NUEVO VECINO{RESET}")
    print(f"{AZUL}{'='*50}{RESET}")

    id = input("➤ Ingrese el ID del vecino: ").strip()
    if id in datos:
        print(f"\n{ROJO}❌ Error: El vecino con ID {id} ya existe.{RESET}")
        input("Presione Enter para continuar...")
        return datos

    nombre = input("➤ Nombre: ").strip().capitalize()
    apellidos = input("➤ Apellido: ").strip().capitalize()
    
    while True:
        telefono = input("➤ Número de teléfono (10 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 10:
            break
        print(f"{ROJO}⚠ El número debe tener exactamente 10 dígitos.{RESET}")
    
    direccion = input("➤ Dirección: ").strip().capitalize()
    
    while True:
        tipo_de_usuario = input("➤ Tipo (Administrador/Residente): ").strip().capitalize()
        if tipo_de_usuario in ["Administrador", "Residente"]:
            break
        print(f"{ROJO}⚠ Tipo no válido. Elija entre Administrador o Residente.{RESET}")

    datos[id] = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo_de_usuario": tipo_de_usuario
    }
    
    registrar_evento(f"NUEVO VECINO: {nombre} {apellidos} (ID: {id})")
    print(f"\n{VERDE}✅ Vecino '{nombre}' agregado con éxito.{RESET}")
    input("\nPresione Enter para continuar...")
    return datos

def actualizar_vecino(datos):   
    print(f"\n{AZUL}{'='*50}{RESET}")
    print(f"{BOLD}🔄 ACTUALIZAR DATOS DE VECINO{RESET}")
    print(f"{AZUL}{'='*50}{RESET}")

    id = input("➤ ID del Vecino a modificar: ").strip()

    if id not in datos:
        print(f"{ROJO}❌ El vecino no está en el sistema.{RESET}")
        input("Presione Enter para volver...")
        return datos

    print(f"\n{CYAN}Deje en blanco o complete los nuevos datos:{RESET}")
    nombre = input(f"➤ Nuevo nombre [{datos[id]['nombre']}]: ").strip().capitalize() or datos[id]['nombre']
    apellidos = input(f"➤ Nuevo apellido [{datos[id]['apellidos']}]: ").strip().capitalize() or datos[id]['apellidos']
    
    while True:
        telefono = input(f"➤ Nuevo teléfono [{datos[id]['telefono']}]: ").strip() or datos[id]['telefono']
        if telefono.isdigit() and len(telefono) == 10:
            break
        print(f"{ROJO}⚠ Debe tener 10 números.{RESET}")

    direccion = input(f"➤ Nueva dirección [{datos[id]['direccion']}]: ").strip().capitalize() or datos[id]['direccion']
    
    while True:
        tipo = input(f"➤ Nuevo tipo [{datos[id]['tipo_de_usuario']}]: ").strip().capitalize() or datos[id]['tipo_de_usuario']
        if tipo in ["Administrador", "Residente"]:
            tipo_de_usuario = tipo
            break
        print(f"{ROJO}⚠ Tipo no válido.{RESET}")

    datos[id] = {
        "nombre": nombre, "apellidos": apellidos, "telefono": telefono,
        "direccion": direccion, "tipo_de_usuario": tipo_de_usuario
    }

    registrar_evento(f"VECINO ACTUALIZADO: ID {id}")
    print(f"\n{VERDE}✅ Datos actualizados correctamente.{RESET}")
    
    # Resumen visual
    print(f"\n{CYAN}╔{'═'*48}╗")
    print(f"║ {'RESUMEN DE ACTUALIZACIÓN':^46} ║")
    print(f"╠{'═'*48}╣")
    print(f"║ ID: {id:<43} ║")
    print(f"║ Nombre: {nombre + ' ' + apellidos:<38} ║")
    print(f"║ Tel: {telefono:<41} ║")
    print(f"╚{'═'*48}╝{RESET}")
    
    input("\nPresione Enter para continuar...")
    return datos

def buscar_vecinos(datos):
    while True:
        print(f"\n{AZUL}{'='*50}{RESET}")
        print(f"{BOLD}🔍 BUSCADOR DE VECINOS{RESET}")
        print(f"{AZUL}{'='*50}{RESET}")
        
        prd = input("➤ Ingrese ID o Tipo de usuario para buscar: ").strip().lower()
        print(f"\n{BOLD}{'ID':<10} | {'NOMBRE':<25} | {'TIPO':<15}{RESET}")
        print("-" * 55)

        encontrado = False
        for k, v in datos.items():
            if prd in v['tipo_de_usuario'].lower() or prd == k.lower():
                print(f"{k:<10} | {v['nombre'] + ' ' + v['apellidos']:<25} | {v['tipo_de_usuario']:<15}")
                encontrado = True

        if not encontrado:
            print(f"{ROJO}No se encontraron coincidencias.{RESET}")
            
        rta = input("\n¿Desea realizar otra búsqueda? (Si/No): ").strip().capitalize()
        if rta != "Si":
            break

def mostrar_vecinos(datos):
    print(f"\n{AZUL}{'='*60}{RESET}")
    print(f"{BOLD}👥 LISTA GENERAL DE VECINOS{RESET}")
    print(f"{AZUL}{'='*60}{RESET}")

    if not datos:
        print(f"{ROJO}No hay vecinos registrados.{RESET}")
        return

    for id_v, info in datos.items():
        print(f"{BOLD}ID: {id_v}{RESET}")
        if isinstance(info, dict):
            print(f"  ▸ Nombre: {info.get('nombre')} {info.get('apellidos')}")
            print(f"  ▸ Tipo:   {info.get('tipo_de_usuario')}")
            print(f"  ▸ Tel:    {info.get('telefono')}")
        print(f"{CYAN}{'-'*30}{RESET}")
    
    input("\nPresione Enter para volver al menú...")

def eliminar_vecino(datos):
    print(f"\n{ROJO}{'='*50}{RESET}")
    print(f"{BOLD}🗑️ ELIMINAR VECINO DEL SISTEMA{RESET}")
    print(f"{ROJO}{'='*50}{RESET}")

    if not datos:
        print("No hay vecinos registrados.")
        return

    id_eliminar = input("➤ ID del vecino a eliminar: ").strip()

    if id_eliminar not in datos:
        print(f"{ROJO}❌ No existe un vecino con el ID {id_eliminar}{RESET}")
        input("Presione Enter para continuar...")
        return

    v = datos[id_eliminar]
    print(f"\n⚠️ SE ELIMINARÁ A: {BOLD}{v['nombre']} {v['apellidos']}{RESET}")
    
    confirmacion = input("\n¿Está seguro de eliminar este registro permanentemente? (s/n): ").lower()

    if confirmacion == 's':
        datos.pop(id_eliminar)
        registrar_evento(f"VECINO ELIMINADO: ID {id_eliminar}")
        print(f"{VERDE}✅ Vecino eliminado exitosamente.{RESET}")
    else:
        print(f"{CYAN}Operación cancelada.{RESET}")
    
    input("\nPresione Enter para continuar...")



def mi_cuenta(datos_vecinos, id_usuario, datos_prestamos, nombre_completo):
    """Muestra el perfil del usuario logueado y su historial resumido"""
    
    # 1. Limpieza visual
    print("\n" * 15)
    
    # 2. Encabezado de Perfil
    print(f"{CYAN}╔{'═'*55}╗")
    print(f"║{BOLD}{' 👤 MI PERFIL PERSONAL ' :^55}{RESET}{CYAN}║")
    print(f"╚{'═'*55}╝{RESET}")

    if id_usuario not in datos_vecinos:
        print(f"{ROJO}❌ Error: No se pudo cargar la información del perfil.{RESET}")
        return

    v = datos_vecinos[id_usuario]

    # 3. Mostrar Datos Personales
    print(f"{BOLD}ID de Usuario:{RESET}  {id_usuario}")
    print(f"{BOLD}Nombre:{RESET}         {v['nombre']} {v['apellidos']}")
    print(f"{BOLD}Teléfono:{RESET}       {v['telefono']}")
    print(f"{BOLD}Dirección:{RESET}      {v['direccion']}")
    print(f"{BOLD}Rango:{RESET}          {BOLD}{v['tipo_de_usuario']}{RESET}")
    print(f"{CYAN}{'─'*57}{RESET}")

    # 4. Resumen de Actividad (Historial)
    print(f"{BOLD}📊 RESUMEN DE ACTIVIDAD:{RESET}")
    
    total_prestamos = 0
    activos = 0
    
    for p in datos_prestamos.values():
        if p['solicitante'] == nombre_completo:
            total_prestamos += 1
            if p['estado'] == "Activo":
                activos += 1

    print(f"  ▸ Préstamos totales realizados: {total_prestamos}")
    print(f"  ▸ Herramientas en su posesión:  {VERDE}{activos}{RESET}")
    
    # 5. Pequeño listado de las últimas herramientas (Opcional pero útil)
    if total_prestamos > 0:
        print(f"\n{BOLD}Últimos movimientos:{RESET}")
        contador = 0
        # Mostramos los últimos 3
        for p in reversed(list(datos_prestamos.values())):
            if p['solicitante'] == nombre_completo and contador < 3:
                color_st = VERDE if p['estado'] == "Activo" else RESET
                print(f"  • {p['herramienta']} - {color_st}{p['estado']}{RESET}")
                contador += 1
    else:
        print(f"\n{BOLD}Aún no has solicitado herramientas.{RESET}")

    print(f"{CYAN}╚{'═'*55}╝{RESET}")
    input(f"\n{CYAN}Presione Enter para volver al panel...{RESET}")
# Tu función mi_cuenta ya está bastante bien estéticamente, solo asegúrate
# de que llame a los datos en el orden correcto en el archivo principal.