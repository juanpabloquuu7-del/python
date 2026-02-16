
from gestiones.logs import registrar_evento




# Colores y estilos
RESET = "\033[0m"
BOLD = "\033[1m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AZUL = "\033[34m"
CYAN = "\033[36m"
AMARILLO = "\033[33m"

def solicitar_prestamo(datos_vecinos, datos_herramientas, datos_prestamos):
    print(f"\n{AZUL}╔{'═'*45}╗")
    print(f"║{BOLD}{' 📝 NUEVA SOLICITUD DE PRÉSTAMO ' :^45}{RESET}{AZUL}║")
    print(f"╚{'═'*45}╝{RESET}")
    
    # 1. Validar Vecino
    id_V = input("➤ ID del Vecino que solicita: ").strip()
    if id_V not in datos_vecinos:
        registrar_evento(f"FALLO SOLICITUD: ID vecino inexistente {id_V}", es_error=True)
        print(f"{ROJO}❌ Error: El vecino ID {id_V} no está registrado.{RESET}")
        return datos_prestamos, datos_herramientas

    # 2. Validar Herramienta
    cod_H = input("➤ ID de la Herramienta: ").strip()
    if cod_H not in datos_herramientas:
        registrar_evento(f"FALLO SOLICITUD: ID herramienta inexistente {cod_H}", es_error=True)
        print(f"{ROJO}❌ Error: La herramienta {cod_H} no existe.{RESET}")
        return datos_prestamos, datos_herramientas

    # 3. Verificar Disponibilidad
    h = datos_herramientas[cod_H]
    if h['stock'] <= 0 or h['estado'] != "Activa":
        registrar_evento(f"SOLICITUD RECHAZADA: {h['nombre']} sin stock.", es_error=True)
        print(f"\n{ROJO}🚫 NO DISPONIBLE PARA PRÉSTAMO{RESET}")
        return datos_prestamos, datos_herramientas

    # 4. ID Único de Préstamo
    id_P = input("➤ Cree un ID para este préstamo (ej: P101): ").strip().upper()
    if not id_P or id_P in datos_prestamos:
        print(f"{ROJO}❌ ID inválido o ya existente.{RESET}")
        return datos_prestamos, datos_herramientas

    # 5. Fechas (Manejadas como texto simple)
    print(f"{CYAN}Use formato DD/MM/AAAA (ej: 24/12/2024){RESET}")
    f_ini = input("➤ Fecha de inicio: ").strip()
    f_dev = input("➤ Fecha estimada de entrega: ").strip()
    
    if not f_ini or not f_dev:
        print(f"{ROJO}❌ Las fechas son obligatorias.{RESET}")
        return datos_prestamos, datos_herramientas
    
    obs = input("➤ Observaciones: ").strip().capitalize() or "Sin observaciones"

    # 6. Guardar en el diccionario
    v = datos_vecinos[id_V]
    datos_prestamos[id_P] = {
        "id_prestamo": id_P,
        "solicitante": f"{v['nombre']} {v['apellidos']}",
        "tipo_usuario": v['tipo_de_usuario'],
        "id_herramienta": cod_H,
        "herramienta": h['nombre'],
        "cantidad": 1,
        "fecha_inicio": f_ini,
        "fecha_entrega": f_dev,
        "estado": "En trámite",
        "observaciones": obs
    }

    registrar_evento(f"SOLICITUD CREADA: {id_P} por {v['nombre']} {v['apellidos']}")
    print(f"\n{VERDE}✅ Solicitud registrada exitosamente.{RESET}")
    input("\nPresione Enter para continuar...")
    return datos_prestamos, datos_herramientas

def mostrar_prestamos(datos_prestamos, datos_vecinos, datos_herramientas):
    print(f"\n{AZUL}{'='*95}")
    print(f"{BOLD}{'ID PREST':<10} | {'SOLICITANTE':<25} | {'HERRAMIENTA':<20} | {'ESTADO':<15}{RESET}")
    print(f"{AZUL}{'='*95}{RESET}")
    
    if not datos_prestamos:
        print(f"{AMARILLO}No hay registros de préstamos.{RESET}")
    else:
        for id_p, info in datos_prestamos.items():
            st = info.get('estado', 'Pendiente')
            # Color dinámico por estado
            color = VERDE if st == "Activo" else AMARILLO if st == "En trámite" else CYAN if st == "Finalizado" else ROJO
            print(f"{id_p:<10} | {info['solicitante'][:25]:<25} | {info['herramienta'][:20]:<20} | {color}{st:<15}{RESET}")
    
    print(f"{AZUL}{'='*95}{RESET}")

def autorizar_prestamo(datos_vecinos, datos_herramientas, datos_prestamos):
    print(f"\n{AMARILLO}╔{'═'*45}╗")
    print(f"║{BOLD}{' ⚖️  GESTIÓN DE SOLICITUDES ' :^45}{RESET}{AMARILLO}║")
    print(f"╚{'═'*45}╝{RESET}")

    pendientes = {k: v for k, v in datos_prestamos.items() if v['estado'] == "En trámite"}

    if not pendientes:
        print(f"{VERDE}✅ No hay solicitudes pendientes.{RESET}")
        return datos_prestamos, datos_herramientas

    print(f"{'ID':<10} | {'SOLICITANTE':<20} | {'HERRAMIENTA'}")
    print("-" * 50)
    for id_p, info in pendientes.items():
        print(f"{id_p:<10} | {info['solicitante']:<20} | {info['herramienta']}")

    id_gest = input(f"\n{BOLD}➤ ID a procesar:{RESET} ").strip().upper()

    if id_gest not in pendientes:
        print(f"{ROJO}❌ ID no válido o no está pendiente.{RESET}")
        return datos_prestamos, datos_herramientas

    op = input(f"¿Desea {VERDE}(A)utorizar{RESET} o {ROJO}(D)enegar{RESET}? (A/D): ").upper()

    if op == 'A':
        id_h = pendientes[id_gest]['id_herramienta']
        if datos_herramientas[id_h]['stock'] > 0:
            datos_prestamos[id_gest]['estado'] = "Activo"
            datos_herramientas[id_h]['stock'] -= 1
            registrar_evento(f"AUTORIZADO: {id_gest}. Herramienta {id_h}")
            print(f"{VERDE}✅ Préstamo autorizado. Stock actualizado.{RESET}")
        else:
            print(f"{ROJO}❌ Sin stock para aprobar.{RESET}")
            
    elif op == 'D':
        motivo = input("➤ Motivo de rechazo: ").strip()
        datos_prestamos[id_gest]['estado'] = "Denegado"
        datos_prestamos[id_gest]['observaciones'] += f" | Rechazo: {motivo}"
        registrar_evento(f"DENEGADO: {id_gest}. Motivo: {motivo}")
        print(f"{ROJO}🚫 Solicitud denegada.{RESET}")

    input("\nPresione Enter...")
    return datos_prestamos, datos_herramientas




def registrar_devo(datos_prestamos, datos_herramientas):
    print(f"\n{VERDE}╔{'═'*45}╗")
    print(f"║{BOLD}{' 🔙 REGISTRAR DEVOLUCIÓN ' :^45}{RESET}{VERDE}║")
    print(f"╚{'═'*45}╝{RESET}")
    
    id_P = input("➤ ID del préstamo a finalizar: ").strip().upper()
    
    # Verificamos si existe el préstamo
    if id_P not in datos_prestamos:
        print(f"{ROJO}❌ El préstamo ID {id_P} no existe.{RESET}")
        input("Presione Enter...")
        return datos_prestamos, datos_herramientas

    # Verificamos que esté activo
    if datos_prestamos[id_P]['estado'] != "Activo":
        print(f"{ROJO}❌ Este préstamo no está 'Activo' (Estado actual: {datos_prestamos[id_P]['estado']}).{RESET}")
        input("Presione Enter...")
        return datos_prestamos, datos_herramientas

    p = datos_prestamos[id_P]
    cod_H = p['id_herramienta']
    
    if cod_H in datos_herramientas:
        # 1. Devolvemos el stock
        datos_herramientas[cod_H]['stock'] += 1
        
        # 2. Cambiamos estado
        p['estado'] = "Finalizado"
        
        # 3. Fecha manual (para no usar datetime)
        f_real = input("➤ Ingrese fecha de hoy (DD/MM/AAAA): ").strip()
        if not f_real:
            f_real = "Fecha no registrada"
        
        p['observaciones'] += f" | Devuelto el: {f_real}"
        
        # 4. Registrar en el LOG
        registrar_evento(f"DEVOLUCIÓN: {id_P}. Herramienta {cod_H} regresó.")
        
        print(f"\n{VERDE}✅ Devolución procesada correctamente.{RESET}")
        print(f"{CYAN}📈 Stock de {datos_herramientas[cod_H]['nombre']} actualizado.{RESET}")
    else:
        print(f"{ROJO}❌ Error: La herramienta {cod_H} ya no existe en el sistema.{RESET}")

    input("\nPresione Enter para continuar...")
    return datos_prestamos, datos_herramientas

def mis_prestamos(datos_p, nombre_completo):
    print(f"\n{CYAN}╔{'═'*45}╗")
    print(f"║{BOLD}{' 📋 MIS PRÉSTAMOS ' :^45}{RESET}{CYAN}║")
    print(f"╚{'═'*45}╝{RESET}")
    
    encontrados = False
    for id_p, info in datos_p.items():
        if info.get('solicitante') == nombre_completo:
            encontrados = True
            st = info.get('estado')
            color = VERDE if st == "Activo" else AMARILLO if st == "En trámite" else RESET
            print(f"{BOLD}ID: {id_p}{RESET}")
            print(f"   🛠️  Herramienta: {info.get('herramienta')}")
            print(f"   📌 Estado: {color}{st}{RESET}")
            print(f"   📅 Fecha entrega: {info.get('fecha_entrega')}")
            print("-" * 40)

    if not encontrados:
        print(f"{AMARILLO}No tienes préstamos registrados.{RESET}")
    
    input(f"\n{CYAN}Presione Enter para volver...{RESET}")