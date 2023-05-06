import csv
import os

def create_csv(path):
    if not os.path.exists(path):
        try:
            os.makedirs('./app/CSV')
            with open(path,mode='w',newline='')as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['CIP','Nombre','Apellido','P1','P2','P3','PF'])
        except FileExistsError as ErrorFile:
            print(str(ErrorFile)+" == El archivo ya existe")
        except FileNotFoundError as ErrorFile2:
            print(str(ErrorFile2)+" == El archivo no se encuentra")
    else:
        print(f'El archivo ya existe! en: {path}')

if __name__ == "__main__":
    path = './app/CSV/Notas_Universitarias.csv'
    create_csv(path)
    
