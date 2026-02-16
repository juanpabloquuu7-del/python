from menu_ini import menu_consultas_y_reportes, menu_usuarios, menu_herramientas, menu_prestamos
from gestiones.gestion_dats import cargar_datos
from gestiones.gestion_datos_herramientas import cargar_datos_herramienta
from gestiones.gestion_dats_prestamos import cargar_datos_prestamo
from gestiones.logs import ver_logs
from resi import panel_residente 

# Colores y estilos
RESET = "\033[0m"
BOLD = "\033[1m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AZUL = "\033[34m"
CYAN = "\033[36m"
AMARILLO = "\033[33m"

def limpiar_pantalla_visual():
    print("\n" * 20)

def menu():
    # Carga inicial de datos
    datos_v = cargar_datos("json/vecinos.json")
    datos_h = cargar_datos_herramienta("json/herramientas.json")
    datos_p = cargar_datos_prestamo("json/prestamos.json")

    while True:
        limpiar_pantalla_visual()
        print(f"{AZUL}╔{'═'*45}╗")
        print(f"║{BOLD}{' 🏢 SISTEMA DE GESTIÓN COMUNITARIA ' :^45}{RESET}{AZUL}║")
        print(f"╚{'═'*45}╝{RESET}")
        
        id_usuario = input(f"{BOLD}🔹 Ingrese su Id de usuario:{RESET} ").strip()
        
        # 1. VALIDACIÓN DE EXISTENCIA
        if id_usuario in datos_v:
            usuario_info = datos_v[id_usuario]
            tipo = usuario_info.get('tipo_de_usuario', 'Residente')
            
            nombre = usuario_info.get('nombre', 'Admin')
            apellido = usuario_info.get('apellidos', 'Sistema')
            nombre_completo = f"{nombre} {apellido}"

            print(f"\n{VERDE}✅ Bienvenid@, {BOLD}{nombre_completo}{RESET} ({tipo})")
            input("Presione Enter para ingresar...")

            # 2. FILTRO: DIRECCIONAMIENTO POR TIPO DE USUARIO
            if tipo == "Administrador":
                while True:
                    limpiar_pantalla_visual()
                    print(f"{AMARILLO}╔{'═'*45}╗")
                    print(f"║{BOLD}{' 🛠️  MENÚ ADMINISTRADOR ' :^45}{RESET}{AMARILLO}║")
                    print(f"╠{'═'*45}╣{RESET}")
                    print(f"  {AMARILLO}1.{RESET} Menú de Usuarios")
                    print(f"  {AMARILLO}2.{RESET} Menú de Herramientas")
                    print(f"  {AMARILLO}3.{RESET} Menú de Préstamos")
                    print(f"  {AMARILLO}4.{RESET} Consultas y Reportes")
                    print(f"  {AMARILLO}5.{RESET} Ver Registro (Logs)")
                    print(f"  {ROJO}6. Salir (Cerrar sesión){RESET}")
                    print(f"{AMARILLO}╚{'═'*45}╝{RESET}")
                    
                    opcion = input(f"\n{BOLD}➤ Seleccione una opción:{RESET} ").strip()
                    
                    if opcion == "1": 
                        menu_usuarios()
                    elif opcion == "2": 
                        menu_herramientas()
                    elif opcion == "3":
                        menu_prestamos()
                    elif opcion == "4": 
                        menu_consultas_y_reportes(datos_v, datos_h, datos_p)
                    elif opcion == "5": 
                        ver_logs()
                    elif opcion == "6": 
                        print(f"\n{CYAN}Cerrando sesión de administrador...{RESET}")
                        break 
                    else: 
                        print(f"{ROJO}❌ Opción inválida.{RESET}")
                        input("Enter para continuar...")
            
            elif tipo == "Residente":
                # Llamamos al panel de residente (asegúrate que esté importado arriba)
                panel_residente(id_usuario, nombre_completo, datos_v, datos_h, datos_p)
        
        else:
            print(f"\n{ROJO}❌ El usuario no está agregado o el ID es incorrecto.{RESET}")
            input("Presione Enter para intentar de nuevo...")

if __name__ == "__main__":
    menu()