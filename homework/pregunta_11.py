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
    sequence = [(col[3].split(","), int(col[1])) for col in lines]
    sequence = [(item, sublist[1]) for sublist in sequence for item in sublist[0]]
    return sequence


def reducer(sequence):
    """Reducer"""
    result = {}
    for key, group in groupby(sequence, lambda x: x[0]):
        result[key] = sum(value for _, value in group)
    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    path_file = "files/input/data.csv"
    lines = read_file(path_file)
    sequence = mapper(lines)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence