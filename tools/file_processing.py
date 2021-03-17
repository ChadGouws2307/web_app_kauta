import pandas as pd

from .analysis import transform_data, pca_decomposition, concatenate_data, calculate_corr


def process_pca_file(file, n):
    df = pd.read_csv(file)
    tickers, x_tran = transform_data(df)
    pc_df = pca_decomposition(x_tran, n)
    df_all = concatenate_data(pc_df, x_tran, tickers)
    corr = calculate_corr(df_all, n)
    return corr
