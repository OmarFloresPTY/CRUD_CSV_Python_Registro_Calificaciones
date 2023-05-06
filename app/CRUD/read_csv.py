import csv

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
    path = './app/CSV/Notas_Universitarias.csv'
    data = read_csv(path)
    print(data)