'''Comprobador de Conectividad de Sitios Web
La idea de este proyecto es crear un programa que pruebe la conectividad de sitios web.
Puedes usar los modulos urllib y tkinter para crear una interfaz gráfica de usuario (GUI) que
permita a los usuarios ingresar una dirección web. Después de haber recopilado la dirección
web del usuario, puedes pasarla a una función para devolver un código de estado HTTP para
el sitio web actual mediante la función .getcode() del módulo urllib.
En este ejemplo, simplemente determinamos si el código HTTP es 200. Si lo es, sabemos que
el sitio está funcionando; de lo contrario, informamos al usuario de que no está disponible (cg)
'''
'''
Paso 1: Importar los módulos necesarios
Vamos a utilizar los módulos urllib.request para realizar la solicitud HTTP y tkinter para crear la interfaz gráfica de usuario.

Paso 2: Crear la interfaz gráfica
Vamos a diseñar una interfaz simple con un campo de entrada para que el usuario ingrese la URL y un botón para verificar la conectividad. Mostraremos el resultado en una etiqueta.

Paso 3: Implementar la lógica para probar la conectividad
Usaremos urllib.request para hacer la solicitud HTTP y determinar el código de estado.(cg)
'''
import urllib.request
import tkinter as tk
from tkinter import messagebox

def check_connectivity():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una URL.")
        return

    try:
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        if status_code == 200:
            messagebox.showinfo("Resultado", "El sitio web está funcionando.")
        else:
            messagebox.showinfo("Resultado", f"El sitio web retornó el código de estado {status_code}.")
    except urllib.error.HTTPError as e:
        messagebox.showerror("Error", f"Error HTTP: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        messagebox.showerror("Error", f"Error de URL: {e.reason}")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Verificador de Conectividad de Sitios Web")

# Crear y colocar los widgets
label = tk.Label(root, text="Ingrese la URL:")
label.pack(pady=10)

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

button_check = tk.Button(root, text="Verificar Conectividad", command=check_connectivity)
button_check.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()

'''
Desglose del Código
Importaciones:

urllib.request: Para realizar la solicitud HTTP.
tkinter: Para crear la interfaz gráfica.
messagebox: Para mostrar mensajes emergentes.
Función check_connectivity:

Obtiene la URL ingresada por el usuario.
Intenta abrir la URL y verificar el código de estado HTTP.
Muestra mensajes adecuados dependiendo del resultado.
Interfaz gráfica:

Crea una ventana con un campo de entrada, un botón y etiquetas para mostrar mensajes.
Llama a la función check_connectivity cuando se presiona el botón.

Nota: El código urllib.request.urlopen(url) asume que la URL está bien formada y accesible
'''

