import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RegistroPrincial:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Bienvenido al Registro de Estudiantes")
        self.window.geometry("1243x722")
        self.window.config(bg='white')
        self.label = tk.Label(self.window,text="Registro de Estudiantes",bg="white",font=("Arial",30,"bold"))
        self.label.pack()

        self.frame = tk.Frame(self.window,bg="white")
        self.frame.pack(pady=20)
        self.txt_cip = tk.Label(self.frame,text="CIP",bg="white")
        self.txt_cip.grid(row=0,column=0)
        self.txtbox_cip = tk.Entry(self.frame)
        self.txtbox_cip.grid(row=0,column=1)

        self.txt_nombre = tk.Label(self.frame,text="Nombre",bg="white")
        self.txt_nombre.grid(row=0,column=2)
        self.txtbox_nombre = tk.Entry(self.frame)
        self.txtbox_nombre.grid(row=0,column=3)

        self.txt_apellido = tk.Label(self.frame,text="Apellido",bg="white")
        self.txt_apellido.grid(row=0,column=4)
        self.txtbox_apellido = tk.Entry(self.frame)
        self.txtbox_apellido.grid(row=0,column=5)

        self.txt_p1 = tk.Label(self.frame,text="Nota 1",bg="white")
        self.txt_p1.grid(row=1,column=0)
        self.txtbox_p1 = tk.Entry(self.frame)
        self.txtbox_p1.grid(row=1,column=1)

        self.txt_p2 = tk.Label(self.frame,text="Nota 2",bg="white")
        self.txt_p2.grid(row=1,column=2)
        self.txtbox_p2 = tk.Entry(self.frame)
        self.txtbox_p2.grid(row=1,column=3)

        self.txt_p3 = tk.Label(self.frame,text="Nota 3",bg="white")
        self.txt_p3.grid(row=1,column=4)
        self.txtbox_p3 = tk.Entry(self.frame)
        self.txtbox_p3.grid(row=1,column=5)

        self.datagripview = ttk.Treeview(self.window,columns=("CIP","Nombre","Apellido","N1","N2","N3","PF"),show="headings")
        self.datagripview.heading("CIP",text="CIP")
        self.datagripview.heading("Nombre",text="Nombre")
        self.datagripview.heading("Apellido",text="Apellido")
        self.datagripview.heading("N1",text="N1")
        self.datagripview.heading("N2",text="N2")
        self.datagripview.heading("N3",text="N3")
        self.datagripview.heading("PF",text="PF")
        self.datagripview.pack()

        self.window.mainloop()

if __name__ == '__main__':
    ventana = RegistroPrincial()