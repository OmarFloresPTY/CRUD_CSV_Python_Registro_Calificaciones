import csv

def deleter_element_csv(path,cip):
    """
        Funcion para eliminar una fila del csv utilizando un elemento
        de esa fila.
        deleter_element_csv(path="directorio donde está ubicado el csv",key="palabra clave")
    """
    with open(path,'r',encoding='utf-8-sig') as csvfile:
        reader = list(csv.reader(csvfile,delimiter=','))
        reader = list(filter(lambda list_in_reader: cip not in list_in_reader,reader))
    
    with open(path,"w",newline='') as csvfile:   
        writer = csv.writer(csvfile)
        for lista in reader:  
            writer.writerow(lista)

if __name__ == "__main__":
    path = './app/CSV/Notas_Universitarias.csv'
    data = deleter_element_csv(path,"6-722-2106")