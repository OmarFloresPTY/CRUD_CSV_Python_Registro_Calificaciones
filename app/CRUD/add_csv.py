import csv
from functools import reduce
def add_csv(path,cip,name,lastname,p1,p2,p3):
    try:
        with open(path,mode='a',newline='',encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            data = [cip,name,lastname,p1,p2,p3]
            prom = reduce(lambda a,b:a+b,data[3:])//len(data[3:])
            data.append(prom)
            writer.writerow(data)
    except FileExistsError as ErrorFile:
        print(str(ErrorFile)+" == El archivo ya existe")
    except FileNotFoundError as ErrorFile2:
        print(str(ErrorFile2)+" == El archivo no se encuentra")
if __name__ == "__main__":
    path = './app/CSV/Notas_Universitarias.csv'
    add_csv(path,"9-922-1233","Abdiel","Ocaña",100,100,100)