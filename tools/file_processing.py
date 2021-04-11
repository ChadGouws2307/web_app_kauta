import pandas as pd

from .analysis import prepare_price_data, group_corr


def process_corr_file(file):
    df = pd.read_csv(file, sep=',')
    df = prepare_price_data(df)
    stocks, corr = group_corr(df)
    return stocks, corr
