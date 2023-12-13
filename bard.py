import mysql.connector
from tkinter import *

def cerrar_ventana_principal():
    wind.destroy()

def clear_message():
    for widget in chat_bg.winfo_children():
        widget.destroy()

def send_message():
    global xi, yi
    u = user_entry.get()
    user = Label(chat_bg, height=1, width=64, bg='#a6a6a6', fg='black', text=u + ' <Tu ', font=12, anchor='e')
    user.grid(row=xi, column=0, sticky='w')
    
    respuesta = obtener_respuesta(u.lower())
    
    bot = Label(chat_bg, height=1, width=64, bg='white', fg='black', text=' AITiny> ' + respuesta, font=12, anchor='w')
    bot.grid(row=xi + 1, column=0, sticky='w')
    
    xi += 2
    user_entry.delete(0, 'end')

def obtener_respuesta(pregunta):
    conn = mysql.connector.connect(host='localhost',
                                        database='bd_certus',
                                        user='root',
                                        password='123456')
    print("Conexión exitosa!")
    cursor = conn.cursor()
    
    cursor.execute("SELECT answer FROM knowledge WHERE question=%s", (pregunta,))
    respuesta = cursor.fetchone()
    
    conn.close()
    
    if respuesta:
        return respuesta[0]
    else:
        return "No tengo información sobre esa pregunta."

def on_enter(e):
    user_entry.delete(0, 'end')
    user_entry.config(fg='black')

def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg='#5c5a5a')
    if n == '' or n == ' ':
        user_entry.insert(0, 'Enter message...')
        user_entry.config(fg='#5c5a5a')

def cerrar_sesion():
    wind.destroy()
    import os
    os.system('python main.py')

wind = Tk()
wind.title('ChatBot')
wind.geometry('600x600')
wind.configure(bg='#08094a')
xi = 0
yi = 0

hcb_text = Label(height=2, width=14, bg='#08094a', text='Aytini', font=('Impact', 20), fg='white')
hcb_text.place(x=200, y=5)

chat_bg = Frame(height=420, width=580, bg='#f5f5f5')
chat_bg.place(x=10, y=80)

entry_bg = Frame(height=60, width=500, bg='white')
entry_bg.place(x=10, y=520)

sendbtn_bg = Frame(height=60, width=65, bg='white')
sendbtn_bg.place(x=525, y=520)

user_entry = Entry(entry_bg, width=32, bg='white', font=('Helvetica', 20), relief=FLAT, border=0)
user_entry.place(x=10, y=13)
user_entry.insert(0, 'Enter message...')
user_entry.config(fg='#5c5a5a')
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

send_button = Button(sendbtn_bg, height=1, width=3, bg='#08094a', text='GO', font=('Helvetica', 20),
                     activeforeground='white', fg='white', relief=FLAT, border=0, activebackground='#08094a', command=send_message)
send_button.place(x=5, y=4)

# Crear un botón de cerrar sesión en forma circular
boton_cerrar_sesion = Button(wind, width=12, height=2, compound=LEFT, bg='red', fg='red', relief=FLAT, command=cerrar_sesion)
boton_cerrar_sesion.place(relx=0.95, rely=0.05, anchor='ne')

# Ajustar el tamaño del botón de cerrar sesión
boton_cerrar_sesion.config(width=30, height=30)

# Agregar un logo de apagado al botón
logo_apagado = PhotoImage(file='images/shutdown.png') 
boton_cerrar_sesion.config(image=logo_apagado, compound=LEFT)

wind.mainloop()

