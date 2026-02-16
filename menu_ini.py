

from gestiones.gestion_dats import cargar_datos, guardar_datos
from gestion_vecinos import actualizar_vecino, agregar_vecinos, buscar_vecinos, eliminar_vecino, mostrar_vecinos
from gestiones.gestion_datos_herramientas import cargar_datos_herramienta, guardar_datos_herramienta
from herramientas import actualizar_herramienta, agregar_herramientas, eliminar_herramienta, mostrar_herramientas, buscar_herramientas, inavilitar_herramienta

from prestamos import  autorizar_prestamo, mostrar_prestamos, registrar_devo, solicitar_prestamo




herra = cargar_datos_herramienta("json/herramientas.json")

# Colores y estilos globales
RESET = "\033[0m"
BOLD = "\033[1m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AZUL = "\033[34m"
CYAN = "\033[36m"
AMARILLO = "\033[33m"

def menu_usuarios():
    datos = cargar_datos()
    while True:
        print(f"\n{AZUL}╔{'═'*45}╗")
        print(f"║{BOLD}{' 👤 GESTIÓN DE VECINOS ' :^45}{RESET}{AZUL}║")
        print(f"╠{'═'*45}╣{RESET}")
        print(f"  {VERDE}1.{RESET} Mostrar lista de vecinos")
        print(f"  {VERDE}2.{RESET} Agregar nuevo vecino")
        print(f"  {VERDE}3.{RESET} Buscar vecino (ID/Tipo)")
        print(f"  {VERDE}4.{RESET} Actualizar información")
        print(f"  {VERDE}5.{RESET} Eliminar vecino del sistema")
        print(f"  {AMARILLO}6.{RESET} Guardar y regresar al menú principal")
        print(f"{AZUL}╚{'═'*45}╝{RESET}")

        opcion = input(f"{BOLD}➤ Seleccione una opción:{RESET} ")

        if opcion == "1":
            mostrar_vecinos(datos)   
        elif opcion == "2":
            agregar_vecinos(datos)
        elif opcion == "3":
            buscar_vecinos(datos)
        elif opcion == "4":
            actualizar_vecino(datos)
        elif opcion == "5":
            eliminar_vecino(datos)
        elif opcion == "6":
            guardar_datos(datos)
            print(f"{VERDE}✅ Datos de vecinos sincronizados.{RESET}")
            break
        else:
            print(f"{ROJO}❌ Opción inválida. Intente de nuevo.{RESET}")
        
        input(f"\n{CYAN}Presione Enter para continuar...{RESET}")

def menu_herramientas():
    datos = cargar_datos_herramienta("json/herramientas.json")
    while True:
        print(f"\n{AZUL}╔{'═'*45}╗")
        print(f"║{BOLD}{' ⚒️  GESTIÓN DE HERRAMIENTAS ' :^45}{RESET}{AZUL}║")
        print(f"╠{'═'*45}╣{RESET}")
        print(f"  {VERDE}1.{RESET} Mostrar inventario completo")
        print(f"  {VERDE}2.{RESET} Registrar nueva herramienta")
        print(f"  {VERDE}3.{RESET} Buscar herramienta")
        print(f"  {VERDE}4.{RESET} Actualizar stock/detalles")
        print(f"  {VERDE}5.{RESET} Eliminar del sistema")
        print(f"  {ROJO}6.{RESET} Inhabilitar (FDS)")
        print(f"  {AMARILLO}7.{RESET} Guardar y regresar")
        print(f"{AZUL}╚{'═'*45}╝{RESET}")

        opcion = input(f"{BOLD}➤ Seleccione una opción:{RESET} ")

        if opcion == "1":
            mostrar_herramientas(datos)
        elif opcion == "2":
            agregar_herramientas(datos)
        elif opcion == "3":
            buscar_herramientas(datos)
        elif opcion == "4":
            actualizar_herramienta(datos)
        elif opcion == "5":
            eliminar_herramienta(datos)
        elif opcion == "6":
            inavilitar_herramienta(datos)
        elif opcion == "7":
            guardar_datos_herramienta(datos)
            print(f"{VERDE}✅ Inventario guardado correctamente.{RESET}")
            break
        else:
            print(f"{ROJO}❌ Opción inválida.{RESET}")
        
        input(f"\n{CYAN}Presione Enter para continuar...{RESET}")

def menu_prestamos():
    from gestiones.gestion_datos_herramientas import cargar_datos_herramienta, guardar_datos_herramienta
    from gestiones.gestion_dats import cargar_datos
    from gestiones.gestion_dats_prestamos import cargar_datos_prestamo, guardar_datos_prestamo
    
    datos_prestamos = cargar_datos_prestamo("json/prestamos.json")
    datos_vecinos = cargar_datos("json/vecinos.json")
    datos_herramientas = cargar_datos_herramienta("json/herramientas.json")

    while True:
        print(f"\n{AZUL}╔{'═'*45}╗")
        print(f"║{BOLD}{' 📋 MÓDULO DE PRÉSTAMOS ' :^45}{RESET}{AZUL}║")
        print(f"╠{'═'*45}╣{RESET}")
        print(f"  {VERDE}1.{RESET} Listar todas las solicitudes")
        print(f"  {VERDE}2.{RESET} Registrar nueva solicitud")
        print(f"  {VERDE}3.{RESET} Gestionar aprobaciones")
        print(f"  {VERDE}4.{RESET} Registrar devoluciones")
        print(f"  {AMARILLO}5.{RESET} Guardar y regresar")
        print(f"{AZUL}╚{'═'*45}╝{RESET}")

        opcion = input(f"{BOLD}➤ Seleccione una opción:{RESET} ")

        if opcion == "1":
            mostrar_prestamos(datos_prestamos, datos_vecinos, datos_herramientas)
        elif opcion == "2":
            datos_prestamos, datos_herramientas = solicitar_prestamo(datos_vecinos, datos_herramientas, datos_prestamos)
        elif opcion == "3":
            datos_prestamos, datos_herramientas = autorizar_prestamo(datos_vecinos, datos_herramientas, datos_prestamos)
        elif opcion == "4":
            datos_prestamos, datos_herramientas = registrar_devo(datos_prestamos, datos_herramientas)
        elif opcion == "5":
            guardar_datos_prestamo(datos_prestamos, "json/prestamos.json") 
            guardar_datos_herramienta(datos_herramientas, "json/herramientas.json")
            print(f"{VERDE}✅ Registros de préstamos actualizados.{RESET}")
            break
        else:
            print(f"{ROJO}❌ Opción inválida.{RESET}")
            
        input(f"\n{CYAN}Presione Enter para continuar...{RESET}")

def menu_consultas_y_reportes(datos_vecinos, datos_herramientas, datos_prestamos):
    import reportes as rpt
    while True:
        print(f"\n{AZUL}╔{'═'*45}╗")
        print(f"║{BOLD}{' 📊 CONSULTAS Y REPORTES ' :^45}{RESET}{AZUL}║")
        print(f"╠{'═'*45}╣{RESET}")
        print(f"  {CYAN}1.{RESET} Herramientas con stock bajo")
        print(f"  {CYAN}2.{RESET} Préstamos filtrados por estado")
        print(f"  {CYAN}3.{RESET} Historial detallado por vecino")
        print(f"  {CYAN}4.{RESET} Ranking de herramientas top")
        print(f"  {CYAN}5.{RESET} Ranking de vecinos más activos")
        print(f"  {BOLD}6.{RESET} Reporte ejecutivo general")
        print(f"  {AMARILLO}7.{RESET} Volver")
        print(f"{AZUL}╚{'═'*45}╝{RESET}")
        
        op = input(f"{BOLD}➤ Seleccione un reporte:{RESET} ")

        if op == "1":
            rpt.herramientas_stock_bajo(datos_herramientas)
        elif op == "2":
            rpt.reporte_prestamos(datos_prestamos)
        elif op == "3": 
            rpt.historial_vecino(datos_vecinos, datos_prestamos)
        elif op == "4": 
            rpt.herramientas_mas_solicitadas(datos_prestamos)
        elif op == "5":
            rpt.vecinos_mas_activos(datos_prestamos)
        elif op == "6": 
            rpt.reporte_general(datos_vecinos, datos_herramientas, datos_prestamos)
        elif op == "7": 
            break
        else: 
            print(f"{ROJO}❌ Opción inválida.{RESET}")
        
        input(f"\n{CYAN}Presione Enter para continuar...{RESET}")