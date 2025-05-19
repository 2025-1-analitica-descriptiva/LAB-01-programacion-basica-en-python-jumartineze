"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from .pregunta_01 import read_file
from .pregunta_03 import shuffle_and_sort
from itertools import groupby


def reducer(sequence):
    """Reducer"""
    result = []
    for key, group in groupby(sequence, lambda x: x[0]):
        group_list = list(group) 
        result.append(
            (key, max(value for _, value in group_list), 
                  min(value for _, value in group_list))
        )
    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    path_file = "files/input/data.csv"
    lines = read_file(path_file)
    sequence = [(col[0], int(col[1])) for col in lines]
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence