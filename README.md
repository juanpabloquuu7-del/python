🛠️ SISTEMA DE GESTIÓN COMUNITARIA
Buenas tardes Este es el proyecto para manejar todo el tema de los vecinos, las herramientas y los préstamos del barrio. El programa está dividido para que no se mezcle lo que hace el Admin con lo que hace el Residente.

📂 ¿Qué hay en las carpetas?
proyecto.py: Es el archivo principal. Este es el que tienes que abrir para que arranque todo el sistema.

resi.py: Aquí está todo lo que puede ver y hacer un vecino (ver su perfil, pedir cosas, etc.).

gestiones/: Acá metí la lógica pesada, como el manejo de los JSON y los mensajes de error (logs).

json/: Es nuestra "base de datos". Ahí se guarda la info de los vecinos, qué herramientas tenemos y quién debe qué.

🚀 Cómo ponerlo a andar
Abre tu terminal o consola en la carpeta del proyecto.

Escribe esto y dale Enter:

Bash
python proyecto.py
El sistema te va a pedir tu Id de usuario:

Si usas el 001, entras como Administrador (el que manda).

Si usas el 002, entras como Residente (ejemplo: Miguel Acevedo).

👥 ¿Qué se puede hacer?
Si eres Administrador: Puedes meter vecinos nuevos, ver quién está registrado, agregar herramientas al inventario y ver los reportes de qué es lo que más se presta.

Si eres Residente: Puedes checar qué herramientas hay libres, pedir una prestada, devolverla cuando termines y ver tu perfil con todos tus movimientos.

⚠️ Ojo con esto
Presiona Enter: No te aceleres. Después de que el programa te muestre una lista o un mensaje, siempre te va a pedir que des Enter para continuar. Si no le das, no sigue.

Los Logs: Si algo falla o alguien hace un movimiento, el programa lo anota solito en el archivo logs.txt. Es como nuestra bitácora para saber qué pasó.

Link del video
https://drive.google.com/file/d/1QZUXrLG-boBbW0eDdzHzgZB-mrkMgakH/view?usp=sharing