import pandas as pd
import numpy as np
import re
import string


def column_todate(df):   
    df["Date"] =  pd.to_datetime(df["insert_date"], format="%Y/%m/%d")
    return df

def drop_colums(df):   
    df.drop('insert_date', axis=1, inplace=True)
    return df

def sort_colum(df):
    df = df.sort_values(by='Date')
    return df

def drop_duplicates(df):
    df.drop_duplicates(subset='product_id', keep="last", inplace=True)
    return df
