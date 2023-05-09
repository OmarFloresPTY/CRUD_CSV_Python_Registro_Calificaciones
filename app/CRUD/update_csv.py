import csv
from functools import reduce
from CRUD.read_csv import read_csv_dict
#Es importante poner un try-cast evaluando que la llave no existe en el diccionario. Un keyerror!
def modify_csv(path,cip,nombre,apellido,p1,p2,p3):
    data = read_csv_dict(path)
    for dicc in data:
        if dicc['CIP'] == cip:
            dicc['Nombre'] = nombre
            dicc['Apellido'] = apellido
            dicc['P1'] = p1
            dicc['P2'] = p2
            dicc['P2'] = p3
    labels = [columns for columns in data[0].keys()]
    data = list(map(lambda dicc:list(dicc.values()),data))
    for lista in data:
        prom = reduce(lambda a,b:int(a)+int(b),lista[3:6])//len(lista[3:6])
        lista[6] = prom 
    data.insert(0,labels)
    with open(path,"w",newline='') as csvfile:   
        writer = csv.writer(csvfile)
        for lista in data:
            writer.writerow(lista)

if __name__ == '__main__':
    path = './app/CSV/Notas_Universitarias.csv'
    modify_csv(path,'6-722-2106','Lizbeth','Flores','100','98','90')