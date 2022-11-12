import pandas as pd
import plotly.express as px
import numpy as np
import re

path_original_file = '../../data/'
name_original_file = 'datamarket_productos_de_supermercados.csv'

def connec_csv():
    # función para únicamente tomar en formato csv la data sin tratar de una conexión a bbdd mysql
    df = pd.read_csv(path_original_file + name_original_file, sep=',')
    return df