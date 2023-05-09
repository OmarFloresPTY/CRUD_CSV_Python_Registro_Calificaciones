import tkinter as tk
from tkinter import ttk
from CRUD.read_csv import read_csv_list,read_csv_dict
from CRUD.add_csv import add_csv
from CRUD.deleter_csv import deleter_element_csv
from CRUD.update_csv import modify_csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RegistroPrincial:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Bienvenido al Registro de Estudiantes")
        self.window.geometry("1243x722")
        self.window.config(bg='white')
        self.label = tk.Label(self.window,text="Registro de Estudiantes",bg="white",font=("Arial",30,"bold"))
        self.label.pack()
        #Creamos un contenedor que va a tener los labels, los textbox y el datagripview principal 
        self.frame_padre = tk.Frame(self.window)
        self.frame_padre.pack(pady=20)
        #Creando Texbox y labels principales
        self.frame = tk.Frame(self.frame_padre,bg="white")
        self.frame.pack(pady=20)
        self.txt_cip = tk.Label(self.frame,text="CIP",bg="white")
        self.txt_cip.grid(row=1,column=0)
        self.txtbox_cip = tk.Entry(self.frame,relief='solid')
        self.txtbox_cip.grid(row=1,column=1)
        self.txt_nombre = tk.Label(self.frame,text="Nombre",bg="white")
        self.txt_nombre.grid(row=1,column=2)
        self.txtbox_nombre = tk.Entry(self.frame,relief='solid')
        self.txtbox_nombre.grid(row=1,column=3)
        self.txt_apellido = tk.Label(self.frame,text="Apellido",bg="white")
        self.txt_apellido.grid(row=1,column=4)
        self.txtbox_apellido = tk.Entry(self.frame,relief='solid')
        self.txtbox_apellido.grid(row=1,column=5)
        self.txt_p1 = tk.Label(self.frame,text="Nota 1",bg="white")
        self.txt_p1.grid(row=2,column=0)
        self.txtbox_p1 = tk.Entry(self.frame,relief='solid')
        self.txtbox_p1.grid(row=2,column=1)
        self.txt_p2 = tk.Label(self.frame,text="Nota 2",bg="white")
        self.txt_p2.grid(row=2,column=2)
        self.txtbox_p2 = tk.Entry(self.frame,relief='solid')
        self.txtbox_p2.grid(row=2,column=3)
        self.txt_p3 = tk.Label(self.frame,text="Nota 3",bg="white")
        self.txt_p3.grid(row=2,column=4)
        self.txtbox_p3 = tk.Entry(self.frame,relief='solid')
        self.txtbox_p3.grid(row=2,column=5)

        #Botones CRUD
        self.btn_agregar = tk.Button(self.frame, text="Agregar",width=10,command=lambda: add_csv('./app/CSV/Notas_Universitarias.csv',self.txtbox_cip.get(),self.txtbox_nombre.get(),self.txtbox_apellido.get(),int(self.txtbox_p1.get()),int(self.txtbox_p2.get()),int(self.txtbox_p3.get())))
        self.btn_agregar.grid(row=0,column=6,padx=(40,0))
        self.btn_modificar = tk.Button(self.frame, text="Modificar",width=10,command=lambda:modify_csv('./app/CSV/Notas_Universitarias.csv',self.txtbox_cip.get(),self.txtbox_nombre.get(),self.txtbox_apellido.get(),self.txtbox_p1.get(),self.txtbox_p2.get(),self.txtbox_p3.get()))
        self.btn_modificar.grid(row=1,column=6,padx=(40,0))
        self.btn_eliminar = tk.Button(self.frame, text="Eliminar",width=10,command=lambda:deleter_element_csv('./app/CSV/Notas_Universitarias.csv',self.txtbox_cip.get()))
        self.btn_eliminar.grid(row=2,column=6,padx=(40,0))
        self.btn_refrescar = tk.Button(self.frame, text="Refrescar",width=10,command=self.datanew)
        self.btn_refrescar.grid(row=3,column=6,padx=(40,0))
        self.datagripviw_create()

        #Crear gráfico:
        value_x = read_csv_dict('./app/CSV/Notas_Universitarias.csv')
        value_y = read_csv_list('./app/CSV/Notas_Universitarias.csv')
        self.generate_data_asignature(value_y[0][3:],value_x)
        self.window.mainloop()
       

    def datagripviw_create(self):
        self.datagripview = ttk.Treeview(self.frame_padre,columns=("CIP","Nombre","Apellido","N1","N2","N3","PF"),show="headings")
        self.datagripview.heading("CIP",text="CIP",anchor="center")
        self.datagripview.heading("Nombre",text="Nombre",anchor="center")
        self.datagripview.heading("Apellido",text="Apellido",anchor="center")
        self.datagripview.heading("N1",text="N1",anchor="center")
        self.datagripview.heading("N2",text="N2",anchor="center")
        self.datagripview.heading("N3",text="N3",anchor="center")
        self.datagripview.heading("PF",text="PF",anchor="center")
        #Ajustamos el tamaño de las columnas
        self.datagripview.column("CIP",width=100)
        self.datagripview.column("Nombre",width=100)
        self.datagripview.column("Apellido",width=100)
        self.datagripview.column("N1",width=100)
        self.datagripview.column("N2",width=100)
        self.datagripview.column("N3",width=100)
        self.datagripview.column("PF",width=100)
        self.data = read_csv_list('./app/CSV/Notas_Universitarias.csv')
        for lista in self.data[1:]:
            self.datagripview.insert("","end",values=lista)
        self.datagripview.pack(padx=200)
        self.datagripview.bind("<ButtonRelease-1>",self.update_textbox_datagripview_onclic)
    
    def datanew(self):
        if self.datagripview:
            self.datagripview.destroy()
            self.datagripviw_create()
            self.canvas.get_tk_widget().destroy()
            value_x = read_csv_dict('./app/CSV/Notas_Universitarias.csv')
            value_y = read_csv_list('./app/CSV/Notas_Universitarias.csv')
            self.generate_data_asignature(value_y[0][3:],value_x)

    def generate_data_asignature(self,label,data):
        p1 = p2 = p3 = pf = 0
        values = []
        for dicc in data:
            p1 += int(dicc.get('P1'))/len(data)
            p2 += int(dicc.get('P2'))/len(data)
            p3 += int(dicc.get('P3'))/len(data)
            pf += int(dicc.get('PF'))/len(data)
        values.append(p1)
        values.append(p2)
        values.append(p3)
        values.append(pf)

        fig, ax = plt.subplots()
        ax.bar(label,values)
        ax.set_xlabel('Notas y Promedios de la Clase')
        ax.set_ylabel('Calificación Promedio')
        ax.set_title("Gráfico Calificación Promedio del Curso Por Notas")
        self.canvas = FigureCanvasTkAgg(fig,master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        plt.close()
    
    def update_textbox_datagripview_onclic(self,event):
        item = self.datagripview.selection()[0]
        values = self.datagripview.item(item)["values"]
        self.txtbox_cip.delete(0,tk.END)
        self.txtbox_cip.insert(0,values[0])
        self.txtbox_nombre.delete(0,tk.END)
        self.txtbox_nombre.insert(1,values[1])
        self.txtbox_apellido.delete(0,tk.END)
        self.txtbox_apellido.insert(2,values[2])
        self.txtbox_p1.delete(0,tk.END)
        self.txtbox_p1.insert(3,values[3])
        self.txtbox_p2.delete(0,tk.END)
        self.txtbox_p2.insert(4,values[4])
        self.txtbox_p3.delete(0,tk.END)
        self.txtbox_p3.insert(5,values[5])

if __name__ == '__main__':
    ventana = RegistroPrincial()