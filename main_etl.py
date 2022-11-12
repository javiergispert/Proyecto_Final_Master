import pandas as pd
import plotly.express as px
import numpy as np
import re

import matplotlib.pyplot as plt

from modules import macquisition as mac
from modules import mpreprocessing as mpr


if __name__ == '__main__':
# preprocessing:
    df_pre = mac.connec_csv()
    df_pre = mpr.column_todate(df_pre)
    df_pre = mpr.drop_colums(df_pre)
    df_pre = mpr.sort_colum(df_pre)
    df_pre = mpr.drop_duplicates(df_pre)
    print(df_pre)