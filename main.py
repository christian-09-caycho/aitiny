import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess

# Función para verificar las credenciales de inicio de sesión
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Conectar a la base de datos MySQL
    try:
        # Establecer la conexión
        connection = mysql.connector.connect(
            host='localhost',
            database='bd_certus',
            user='root',
            password='123456'
        )
        cursor = connection.cursor()

        # Consulta para verificar las credenciales
        sql_select_Query = f"SELECT * FROM t_estudiantes WHERE cod_estudiante='{usuario}' AND con_estudiante='{contrasena}'"
        cursor.execute(sql_select_Query)
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Login exitoso", "Inicio de sesión exitoso")

            # Abrir la ventana GTP y cerrar la ventana principal
            abrir_ventana_gtp()

        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

        # Cerrar la conexión
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error de conexión", f"Error: {error}")

# Función para abrir la ventana GTP y cerrar la ventana principal
def abrir_ventana_gtp():
    subprocess.run(["python", "bard.py"])
    ventana.destroy()  # Cerrar la ventana principal

def abrir_register(event):
    subprocess.run(["python", "register.py"])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("420x450")
ventana.configure(bg='#08094a')  # Establecer color de fondo

# Logo con tamaño de 50x50
logo_image = tk.PhotoImage(file="images/logo1.png") 
logo_image = logo_image.subsample(2)  # Reducir tamaño a 50x50
logo_label = tk.Label(ventana, image=logo_image, bg='#08094a')
  # Ajusta la separación de arriba según sea necesario
logo_label.pack(pady=(50, 40))

# Crear un marco para el formulario y centrarlo
formulario_marco = tk.Frame(ventana, bg='#08094a')
formulario_marco.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Fuente
font_style = ("Arial", 16, "bold")

# Crear etiquetas y entradas para usuario y contraseña dentro del marco
tk.Label(formulario_marco, text="Usuario:", font=font_style, fg="white", bg='#08094a').grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")
entry_usuario = tk.Entry(formulario_marco, font=("Arial", 14), bd=1, relief="solid")
entry_usuario.grid(row=0, column=1, padx=10, pady=(5, 0), sticky="ew")

tk.Label(formulario_marco, text="Contraseña:", font=font_style, fg="white", bg='#08094a').grid(row=1, column=0, padx=10, pady=(5, 0), sticky="w")
entry_contrasena = tk.Entry(formulario_marco, show="*", font=("Arial", 14), bd=1, relief="solid")
entry_contrasena.grid(row=1, column=1, padx=10,  pady=(5, 0), sticky="ew")

label_nuevo_registro = tk.Label(formulario_marco, text="Nuevo Registro", font=("Arial", 10), fg="white", bg='#08094a')
label_nuevo_registro.grid(row=2, column=0, columnspan=2, pady=(10,0))

# Asociar un evento de clic al Label
label_nuevo_registro.bind("<Button-1>", abrir_register)


# Botón de inicio de sesión
btn_login = tk.Button(formulario_marco, text="Iniciar sesión", font=font_style, command=verificar_credenciales, bg='#f5f5f5')
btn_login.grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal de tkinter
ventana.mainloop()
