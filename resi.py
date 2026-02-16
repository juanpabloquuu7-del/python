from herramientas import mostrar_herramientas
from prestamos import solicitar_prestamo, registrar_devo, mis_prestamos
from gestion_vecinos import mi_cuenta

# Paleta de colores consistente
RESET = "\033[0m"
BOLD = "\033[1m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AZUL = "\033[34m"
CYAN = "\033[36m"
AMARILLO = "\033[33m"

def limpiar_pantalla_visual():
    """Genera espacio en la consola para simular limpieza de pantalla"""
    print("\n" * 20)

def panel_residente(id_usuario, nombre_completo, datos_v, datos_h, datos_p):
    while True:
        limpiar_pantalla_visual()
        
        # Encabezado con el estilo de caja definido
        print(f"{VERDE}╔{'═'*50}╗")
        print(f"║{BOLD}{' 👤 PANEL DE CONTROL: RESIDENTE ' :^50}{RESET}{VERDE}║")
        print(f"╠{'═'*50}╣{RESET}")
        print(f"  {BOLD}Usuario:{RESET} {nombre_completo}")
        print(f"  {BOLD}ID:{RESET}      {id_usuario}")
        print(f"{VERDE}╠{'═'*50}╣{RESET}")
        
        # Opciones numeradas
        print(f"  {VERDE}1.{RESET} 🛠️  Ver herramientas disponibles")
        print(f"  {VERDE}2.{RESET} 📝 Solicitar préstamo de herramienta")
        print(f"  {VERDE}3.{RESET} 📋 Ver mis préstamos activos")
        print(f"  {VERDE}4.{RESET} ✅ Devolver herramienta")
        print(f"  {VERDE}5.{RESET} 👤 Ver mi perfil / Mi cuenta")
        print(f"  {ROJO}6. ↩️  Cerrar sesión{RESET}")
        print(f"{VERDE}╚{'═'*50}╝{RESET}")
        
        opcion = input(f"\n{BOLD}➤ Seleccione una opción:{RESET} ").strip()

        if opcion == "1":
            limpiar_pantalla_visual()
            print(f"{AZUL}╔{'═'*50}╗")
            print(f"║{BOLD}{' 🛠️  INVENTARIO DISPONIBLE ' :^50}{RESET}{AZUL}║")
            print(f"╚{'═'*50}╝{RESET}")
            mostrar_herramientas(datos_h)
            input(f"\n{CYAN}Presione Enter para volver...{RESET}")

        elif opcion == "2":
            # Llamamos a solicitar_prestamo (ya actualizado sin datetime)
            solicitar_prestamo(datos_v, datos_h, datos_p)
            
        elif opcion == "3":
            # Muestra los préstamos del usuario logueado
            mis_prestamos(datos_p, nombre_completo)
            
        elif opcion == "4":
            # Proceso de devolución con entrada de fecha manual
            registrar_devo(datos_p, datos_h)
            
        elif opcion == "5":
            limpiar_pantalla_visual()
            # Muestra datos del JSON y el historial
            mi_cuenta(datos_v, id_usuario, datos_p, nombre_completo)
            input(f"\n{CYAN}Presione Enter para volver...{RESET}")
            
        elif opcion == "6":
            print(f"\n{AMARILLO}👋 Saliendo del panel... ¡Hasta luego, {nombre_completo}!{RESET}")
            print("\n" * 2)
            break
            
        else:
            print(f"{ROJO}❌ Opción inválida. Intente de nuevo.{RESET}")
            input(f"{CYAN}Presione Enter para continuar...{RESET}")