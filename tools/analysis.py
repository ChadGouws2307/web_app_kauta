import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def transform_data(df):
    tickers = list(df)
    x_tran = StandardScaler().fit_transform(df.values)
    return tickers, x_tran


def pca_decomposition(x, n):
    components = []
    for i in range(n):
        components.append('component ' + str(i+1))
    pca = PCA(n_components=n)
    principal_components = pca.fit_transform(x)
    principal_df = pd.DataFrame(data=principal_components, columns=components)
    return principal_df


def concatenate_data(pc_df, x_tran, tickers):
    df_tran = pd.DataFrame(data=x_tran, columns=tickers)
    df_all = pd.concat([pc_df, df_tran], axis=1)
    return df_all


def calculate_corr(all_df, n):
    df_corr = all_df.corr().iloc[0:n, n:]
    df_groups = df_corr.where(df_corr != df_corr.max(),
                              df_corr.columns.to_series(), axis=1).where(df_corr == df_corr.max(), '', axis=1)
    corr_groups = []
    for comp, stocks in df_groups.iterrows():
        group = [comp] + list(stocks)
        corr_groups.append([g for g in group if g])
    return corr_groups
