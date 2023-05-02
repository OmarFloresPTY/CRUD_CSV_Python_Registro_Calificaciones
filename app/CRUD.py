import csv
import os

def create_csv(path):
    if os.path.exists(path):
        print("El archivo ya existe!")
    else:
        try:
            with open(path,mode='w',newline='')as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['CIP','Nombre','Apellido','P1','P2','P3','PF'])
        except FileExistsError as ErrorFile:
            print(str(ErrorFile)+" == El archivo ya existe")
        except FileNotFoundError as ErrorFile2:
            print(str(ErrorFile2)+" == El archivo no se encuentra")

def add_csv(path):
    try:
        with open(path,mode='a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['1-323-2130','Arelis','Reyes','100','100','100','100'])
    except FileExistsError as ErrorFile:
        print(str(ErrorFile)+" == El archivo ya existe")
    except FileNotFoundError as ErrorFile2:
        print(str(ErrorFile2)+" == El archivo no se encuentra")


def read_csv(path):
    """
        Funcion READ para leer el csv y almacenarlo en una superlista donde
        cada elemento es un diccionario.
    """
    try:
        with open(path,'r',encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile,delimiter=",") #Se genera un iterador.
            column = next(reader)
            data = []
            for row in reader:
                iterable = zip(column,row)
                dict_data = {key:value for key,value in iterable}
                data.append(dict_data)
        return data
    except FileNotFoundError as fnfe:
        print(str(fnfe)+" <==> "+"No se encuentra el archivo .csv")

if __name__ == "__main__":
    data = read_csv('./CSV/Notas_Universitarias.csv')