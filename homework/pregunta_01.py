"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def read_file(path_file):
    lines = open(path_file, "r").readlines()
    lines = [line.replace("\n", "") for line in lines]
    lines = [line.split("\t") for line in lines]
    return lines


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    path_file = "files/input/data.csv"
    lines = read_file(path_file)
    return sum([int(col[1]) for col in lines])