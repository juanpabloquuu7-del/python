# reportes.py
RESET = "\033[0m"
BOLD = "\033[1m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AZUL = "\033[34m"
CYAN = "\033[36m"
AMARILLO = "\033[33m"

def limpiar_pantalla_visual():
    # Simulamos limpieza de pantalla sin usar la librería os
    print("\n" * 25)
    print(f"{AZUL}{'='*60}{RESET}")

# 1. Herramientas con stock bajo
def herramientas_stock_bajo(datos_h):
    limpiar_pantalla_visual()
    print(f"{BOLD}⚠️  REPORTE: HERRAMIENTAS CON STOCK BAJO (Menos de 3 unidades){RESET}")
    print(f"{AZUL}{'─'*60}{RESET}")
    encontrado = False
    for cod, info in datos_h.items():
        if info['stock'] < 3:
            print(f"ID: {cod:10} | {info['nombre']:15} | Stock: {ROJO}{info['stock']}{RESET}")
            encontrado = True
    if not encontrado:
        print(f"{VERDE}✅ Todo el inventario tiene stock suficiente.{RESET}")
    input(f"\n{CYAN}Presione Enter para volver...{RESET}")

# 2. Préstamos filtrados por estado
def reporte_prestamos(datos_p):
    limpiar_pantalla_visual()
    print(f"{BOLD}📋 FILTRAR PRÉSTAMOS POR ESTADO{RESET}")
    estado = input("Ingrese estado (Activo / Devuelto / En trámite): ").strip().capitalize()
    print(f"\n{BOLD}Resultados para: {estado}{RESET}")
    print(f"{AZUL}{'─'*60}{RESET}")
    encontrado = False
    for id_p, p in datos_p.items():
        if p['estado'] == estado:
            print(f"ID: {id_p} | Vecino: {p['solicitante']:20} | Herramienta: {p['herramienta']}")
            encontrado = True
    if not encontrado:
        print(f"{ROJO}No se encontraron registros con ese estado.{RESET}")
    input(f"\n{CYAN}Presione Enter para volver...{RESET}")

# 3. Historial detallado por vecino
def historial_vecino(datos_v, datos_p):
    limpiar_pantalla_visual()
    id_v = input("➤ Ingrese ID del vecino para consultar historial: ").strip()
    if id_v in datos_v:
        nombre_c = f"{datos_v[id_v]['nombre']} {datos_v[id_v]['apellidos']}"
        print(f"\n{BOLD}👤 HISTORIAL COMPLETO DE: {nombre_c}{RESET}")
        print(f"{AZUL}{'─'*60}{RESET}")
        encontrado = False
        for id_p, p in datos_p.items():
            if p['solicitante'] == nombre_c:
                color = VERDE if p['estado'] == "Activo" else RESET
                print(f" • {id_p}: {p['herramienta']:15} | Estado: {color}{p['estado']}{RESET}")
                encontrado = True
        if not encontrado:
            print("Este vecino no ha realizado préstamos aún.")
    else:
        print(f"{ROJO}❌ El ID {id_v} no existe en la base de datos.{RESET}")
    input(f"\n{CYAN}Presione Enter para volver...{RESET}")

# 4. Ranking de herramientas top (Nombre corregido para tu if)
def herramientas_mas_solicitadas(datos_p):
    limpiar_pantalla_visual()
    print(f"{BOLD}🏆 RANKING: HERRAMIENTAS MÁS SOLICITADAS{RESET}")
    print(f"{AZUL}{'─'*60}{RESET}")
    conteo = {}
    for p in datos_p.values():
        h = p['herramienta']
        conteo[h] = conteo.get(h, 0) + 1
    
    # Ordenar por cantidad de mayor a menor
    ranking = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    for i, (nombre, total) in enumerate(ranking[:5], 1):
        print(f" {i}. {nombre:20} ─ Usada {total} veces")
    
    if not ranking:
        print("No hay datos de préstamos suficientes.")
    input(f"\n{CYAN}Presione Enter para volver...{RESET}")

# 5. Ranking de vecinos más activos (Nombre corregido para tu if)
def vecinos_mas_activos(datos_p):
    limpiar_pantalla_visual()
    print(f"{BOLD}🥇 RANKING: VECINOS CON MÁS MOVIMIENTOS{RESET}")
    print(f"{AZUL}{'─'*60}{RESET}")
    conteo = {}
    for p in datos_p.values():
        v = p['solicitante']
        conteo[v] = conteo.get(v, 0) + 1
    
    ranking = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    for i, (nombre, total) in enumerate(ranking[:5], 1):
        print(f" {i}. {nombre:25} ─ {total} préstamos")
        
    if not ranking:
        print("No hay movimientos registrados.")
    input(f"\n{CYAN}Presione Enter para volver...{RESET}")

# 6. Reporte ejecutivo general (Nombre corregido para tu if)
def reporte_general(datos_v, datos_h, datos_p):
    limpiar_pantalla_visual()
    print(f"{BOLD}📊 REPORTE GENERAL DEL SISTEMA{RESET}")
    print(f"{AZUL}{'═'*60}{RESET}")
    
    total_v = len(datos_v)
    total_h = len(datos_h)
    total_p = len(datos_p)
    activos = sum(1 for p in datos_p.values() if p['estado'] == "Activo")
    
    print(f" 📁 Usuarios registrados:      {CYAN}{total_v}{RESET}")
    print(f" 🔧 Herramientas en catálogo:  {CYAN}{total_h}{RESET}")
    print(f" 📝 Total histórico préstamos: {CYAN}{total_p}{RESET}")
    print(f" 🟢 Préstamos activos ahora:   {VERDE}{activos}{RESET}")
    print(f"{AZUL}{'─'*60}{RESET}")
    
    input(f"\n{CYAN}Presione Enter para volver...{RESET}")