import csv
import os

def create_csv(path):
    if not os.path.exists(path):
        try:
            os.makedirs('./CSV')
            with open(path,mode='w',newline='')as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['CIP','Nombre','Apellido','P1','P2','P3','PF'])
        except FileExistsError as ErrorFile:
            print(str(ErrorFile)+" == El archivo ya existe")
        except FileNotFoundError as ErrorFile2:
            print(str(ErrorFile2)+" == El archivo no se encuentra")
    else:
        print(f'El archivo ya existe! en: {path}')
        

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
    path = './CSV/Notas_Universitarias.csv'
    create_csv(path)
    #data = read_csv(path)
    #print(data)