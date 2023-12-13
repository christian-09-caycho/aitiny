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
    subprocess.run(["python", "gtp.py"])
    ventana.destroy()  # Cerrar la ventana principal

# Función para validar la entrada de cod_estudiante (solo números y longitud máxima de 8)
def validate_cod_estudiante(value):
    return value.isdigit() and len(value) <= 8

# Función para crear un nuevo registro de estudiante
def crear_registro():
    cod_estudiante = entry_cod_estudiante.get()
    nom_estudiante = entry_nom_estudiante.get()
    ape_estudiante = entry_ape_estudiante.get()
    con_estudiante = entry_con_estudiante.get()

    # Validar la longitud de cod_estudiante
    if len(cod_estudiante) != 8:
        messagebox.showerror("Error", "El código de estudiante debe tener 8 dígitos.")
        return

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

        # Insertar el nuevo registro
        sql_insert_Query = f"INSERT INTO t_estudiantes (cod_estudiante, nom_estudiante, ape_estudiante, con_estudiante) " \
                           f"VALUES ('{cod_estudiante}', '{nom_estudiante}', '{ape_estudiante}', '{con_estudiante}')"
        cursor.execute(sql_insert_Query)
        connection.commit()

        messagebox.showinfo("Registro exitoso", "Nuevo estudiante registrado exitosamente.")

        # Limpiar los campos después de un registro exitoso
        entry_cod_estudiante.delete(0, tk.END)
        entry_nom_estudiante.delete(0, tk.END)
        entry_ape_estudiante.delete(0, tk.END)
        entry_con_estudiante.delete(0, tk.END)

        # Después de un registro exitoso, abrir main.py
        subprocess.run(["python", "main.py"])

    except mysql.connector.Error as error:
        messagebox.showerror("Error de conexión", f"Error: {error}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("600x450")
ventana.configure(bg='#08094a')  # Establecer color de fondo

# Logo con tamaño de 50x50
logo_image = tk.PhotoImage(file="images/logo1.png")  # Cambia "logo.png" con la ruta de tu logo
logo_image = logo_image.subsample(2)  # Reducir tamaño a 50x50
logo_label = tk.Label(ventana, image=logo_image, bg='#08094a')
  # Ajusta la separación de arriba según sea necesario
logo_label.pack(pady=(30, 80))

# Crear un marco para el formulario de registro y centrarlo
registro_marco = tk.Frame(ventana, bg='#08094a')
registro_marco.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear etiquetas y entradas para el formulario de registro
tk.Label(registro_marco, text="Código de Estudiante (8 dígitos):", font=("Arial", 16), fg="white", bg='#08094a').grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")
entry_cod_estudiante = tk.Entry(registro_marco, font=("Arial", 16), bd=1, relief="solid", validate="key", validatecommand=(ventana.register(validate_cod_estudiante), '%P'))
entry_cod_estudiante.grid(row=0, column=1, padx=10, pady=(5, 0), sticky="ew")

tk.Label(registro_marco, text="Nombre del Estudiante:", font=("Arial", 16), fg="white", bg='#08094a').grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nom_estudiante = tk.Entry(registro_marco, font=("Arial", 16), bd=1, relief="solid")
entry_nom_estudiante.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(registro_marco, text="Apellido del Estudiante:", font=("Arial", 16), fg="white", bg='#08094a').grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_ape_estudiante = tk.Entry(registro_marco, font=("Arial", 16), bd=1, relief="solid")
entry_ape_estudiante.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(registro_marco, text="Contraseña del Estudiante:", font=("Arial", 16), fg="white", bg='#08094a').grid(row=3, column=0, padx=10, pady=(5, 20), sticky="w")
entry_con_estudiante = tk.Entry(registro_marco, font=("Arial", 16), bd=1, relief="solid")
entry_con_estudiante.grid(row=3, column=1, padx=10, pady=(5, 20), sticky="ew")

# Botón para crear un nuevo registro
btn_registro = tk.Button(registro_marco, text="Crear Registro", font=("Arial", 16), command=crear_registro)
btn_registro.grid(row=4, column=0, columnspan=2, pady=(0, 20))

# ... Código anterior ...

# Ejecutar el bucle principal de tkinter
ventana.mainloop()
