import csv
from functools import reduce
from read_csv import read_csv
#Es importante poner un try-cast evaluando que la llave no existe en el diccionario. Un keyerror!
def modify_csv(path,key='Nombre',value='Omar'):
    data = read_csv(path)
    for dicc in data:
        if dicc['CIP'] == '6-722-2106':
            dicc[key] = value
    labels = [columns for columns in data[0].keys()]
    data = list(map(lambda dicc:list(dicc.values()),data))
    for lista in data:
        prom = reduce(lambda a,b:int(a)+int(b),lista[3:6])//len(lista[3:6])
        lista.append(prom) 
    data.insert(0,labels)
    with open(path,"w",newline='') as csvfile:   
        writer = csv.writer(csvfile)
        for lista in data:
            writer.writerow(lista)

if __name__ == '__main__':
    path = './app/CSV/Notas_Universitarias.csv'
    modify_csv(path)