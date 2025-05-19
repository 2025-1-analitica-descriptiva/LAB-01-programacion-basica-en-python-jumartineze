"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from .pregunta_01 import read_file
from .pregunta_03 import shuffle_and_sort
from .pregunta_11 import reducer


def mapper(lines):
    sequence = [(col[0], col[4].split(",")) for col in lines]
    sequence = [(col1, item.split(":")) for col1, col5 in sequence for item in col5]
    sequence = [(col1, int(item[1])) for col1, item in sequence]
    return sequence


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    path_file = "files/input/data.csv"
    lines = read_file(path_file)
    sequence = mapper(lines)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence