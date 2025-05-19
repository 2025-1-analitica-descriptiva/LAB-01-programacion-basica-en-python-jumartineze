"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from .pregunta_01 import read_file
from .pregunta_03 import shuffle_and_sort
from itertools import groupby


def mapper(lines):
    sequence = [col[4].split(",") for col in lines]
    sequence = [item for sublist in sequence for item in sublist]
    sequence = [item.split(":") for item in sequence]
    sequence = [(item[0], int(item[1])) for item in sequence]
    return sequence


def reducer(sequence):
    """Reducer"""
    result = []
    for key, group in groupby(sequence, lambda x: x[0]):
        group_list = list(group) 
        result.append(
            (key, min(value for _, value in group_list), 
                  max(value for _, value in group_list))
        )
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    path_file = "files/input/data.csv"
    lines = read_file(path_file)
    sequence = mapper(lines)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence