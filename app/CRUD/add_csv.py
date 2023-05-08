import csv
from functools import reduce
def add_csv(path):
    try:
        with open(path,mode='a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            data = ['7-889-788','Susan','Carrera',100,100,95]
            prom = reduce(lambda a,b:a+b,data[3:])//len(data[3:])
            data.append(prom)
            writer.writerow(data)
    except FileExistsError as ErrorFile:
        print(str(ErrorFile)+" == El archivo ya existe")
    except FileNotFoundError as ErrorFile2:
        print(str(ErrorFile2)+" == El archivo no se encuentra")
if __name__ == "__main__":
    path = './app/CSV/Notas_Universitarias.csv'
    add_csv(path)