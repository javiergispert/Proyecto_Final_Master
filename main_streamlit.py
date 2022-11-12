import pandas as pd
import numpy as np
import re
import string

import json


import matplotlib.pyplot as plt

import streamlit as st
from PIL import Image

header = st.container()
dataset = st.container()
features = st.container()

st.markdown(
    """
    <style>
    .main {
    background-color: #F5F5F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

route = 'datasets/'

# Importing CSV Recipes with prices Dataset
df = pd.read_csv(route + 'df_recetas_con_precios.csv', index_col=0)

image = Image.open(route + 'test_imagen.jpg')
image_got = Image.open(route + 'juego_de_tronos.jpg')
image_24 = Image.open(route + 'imagen_24.jpg')
image_sense8 = Image.open(route + 'imagen_sense8.jpg')


# -------------------------------------------------


def select_recipe(recipe):
        receta = df[(df["nombre_receta"] == recipe)]
        receta_filtro= receta[['nombre_receta', 'px_receta_mercadona', 'px_receta_dia', 'px_receta_carrefour']]
        return(receta_filtro)

def select_recipe_raciones(recipe):
        receta = df[(df["nombre_receta"] == recipe)]
        receta_filtro= receta[['nombre_receta', 'px_ración_mercadona', 'px_ración_dia', 'px_ración_carrefour']]
        return(receta_filtro)

def select_ingredients(data):
        df["ingredientes"] = df["ingredientes"].apply(eval)
        receta = df[(df["nombre_receta"] == data)]
        receta_filtro= receta['ingredientes']
        return(receta_filtro)

# Streamlit:
st.sidebar.header("Selecciona la receta a calcular su coste de alimentos: ")

filtro_raciones = df['numero_raciones'].unique()
caja_raciones = st.sidebar.selectbox('Paso 1: ¿Cuántas raciones tienes pensado necesitar?', options = filtro_raciones, index = 0)

filtro_precios_raciones = df[df['numero_raciones'] == caja_raciones]
caja_precios = st.sidebar.slider('Paso 2: ¿Cuál es el coste máximo por receta que te quieres gastar?', 
                                  min_value=int(np.ceil(df[df['numero_raciones'] == caja_raciones][['px_receta_mercadona', 'px_receta_dia', 'px_receta_carrefour']].min(axis=1).min(axis=0))), 
                                  max_value=int(np.ceil(df[df['numero_raciones'] == caja_raciones][['px_receta_mercadona', 'px_receta_dia', 'px_receta_carrefour']].max(axis=1).max(axis=0))), 
                                  value=int(np.ceil(df[df['numero_raciones'] == caja_raciones][['px_receta_mercadona', 'px_receta_dia', 'px_receta_carrefour']].mean(axis=1).mean(axis=0))), step=1)

filtro_nombres_recetas = filtro_precios_raciones[filtro_precios_raciones['px_receta_mercadona'] <= caja_precios]['nombre_receta'].unique() # es mejorable si se incluyen los precios de los 3 supermercados
caja_recetas = st.sidebar.selectbox('Paso 3: Selecciona una de las recetas disponibles', options = filtro_nombres_recetas, index = 0)



with header:
    #displaying the image on streamlit app
    st.image(image, caption='Enter any caption here')

    st.title('Tapertece: Sé dueño de tu tiempo')
    st.text('Recupera ese tiempo para ti')

    st.markdown('* **Compara** los precios de los ingredientes usados entre varias cadenas de supermercados')
    st.markdown('* **Compara** cesta de la compra entre los supermercados')

with dataset:
    st.header('Tu robot de cocina te acaba de brindar la posibilidad, mientras se encarga de cocinar, de que veas un capítulo de:')

    if caja_recetas == 'lentejas estofadas':
        st.image(image_got, caption='Enter any caption here')
    elif caja_recetas == 'Arroz tres delicias':
        st.image(image_24, caption='Enter any caption here')
    else:
        st.image(image_sense8, caption='Enter any caption here')
    #st.write(df.head())

    st.subheader('Este es el coste de los ingredientes usados para la receta seleccionada')
    st.table(select_recipe(caja_recetas).style.format({'px_receta_carrefour':'{:.2f}', 'px_receta_dia':'{:.2f}', 'px_receta_mercadona':'{:.2f}'}))
    

    prices_recipe = pd.DataFrame(df[(df["nombre_receta"] == caja_recetas)][['px_receta_mercadona', 'px_receta_dia', 'px_receta_carrefour']].T)
    st.bar_chart(prices_recipe)

    st.subheader('Este es el coste de los ingredientes por cada ración:')

    st.table(select_recipe_raciones(caja_recetas).style.format({'px_ración_mercadona':'{:.2f}', 'px_ración_dia':'{:.2f}', 'px_ración_carrefour':'{:.2f}'}))
    
    

with features:
    st.header('Los ingredientes de tu receta')

    #sel_col, dis_col = st.columns(2)

    #st.table(df[(df["nombre_receta"] == caja_recetas)].ingredientes).lst()
    for i in select_ingredients(caja_recetas):
        st.write(i)