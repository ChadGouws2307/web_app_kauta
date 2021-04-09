import pandas as pd
import numpy as np


def prepare_price_data(df):
    df.columns = df.columns.str.upper()
    if 'DATE' in ' '.join(list(df)):
        df = df.drop(['DATE'], axis=1)
    else:
        df = df.drop(df.columns[0], axis=1)
    df = np.log(df) - np.log(df.shift(1))
    df = df.drop(0)
    return df


def group_corr(df):
    stocks = list(df.columns)
    d_array = _generate_distance_matrix(len(stocks))
    count = 0
    e_tot = -1
    while count < 30:
        df_corr = df[stocks].corr()                                     # Calculate corr of new order
        e = _calculate_energy(df_corr, d_array)                         # Calculate energy of new order = (1 - Cij)*(Di - Dj)
        df_energy = pd.DataFrame(e, columns=df_corr.columns)
        e_new = e.sum()                                                 # Calculate tot energy of new order
        stocks = list(df_energy.sum(axis=0).sort_values().index)        # Sort columns by total column energy
        if e_new == e_tot:
            pass
        else:
            e_tot = e_new
            count += 1
    corr = np.round(df_corr.values, 2).tolist()

    return df_corr.columns.tolist(), np.round(df_corr.values, 2).tolist()


def _calculate_energy(corr, d):
    e_array = np.multiply(1 - corr.values, d)
    return e_array


def _generate_distance_matrix(size):
    n = np.array(range(size))+1
    s = n
    for m in n:
        s = np.vstack([s, n-m])
    s = s[1:]
    s[s <= 0] = 0
    return np.sqrt(s)
