"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from .pregunta_01 import read_file
from collections import Counter


def mapper(lines):
    sequence = [col[4].split(",") for col in lines]
    sequence = [item for sublist in sequence for item in sublist]
    sequence = [item.split(":") for item in sequence]
    sequence = [item[0] for item in sequence]
    return sequence


def reducer(sequence):
    sequence = sorted(Counter(sequence).items())
    sequence = {key: value for key, value in sequence}
    return sequence


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}
    """
    path_file = "files/input/data.csv"
    lines = read_file(path_file)
    sequence = mapper(lines)
    sequence = reducer(sequence)
    return sequence