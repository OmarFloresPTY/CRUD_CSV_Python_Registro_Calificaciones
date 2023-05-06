import csv

def add_csv(path):
    try:
        with open(path,mode='a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['9-888-99','Mario','Balotelli','12','45','12','45'])
    except FileExistsError as ErrorFile:
        print(str(ErrorFile)+" == El archivo ya existe")
    except FileNotFoundError as ErrorFile2:
        print(str(ErrorFile2)+" == El archivo no se encuentra")

if __name__ == "__main__":
    path = './app/CSV/Notas_Universitarias.csv'
    add_csv(path)