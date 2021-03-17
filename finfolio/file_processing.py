import pandas as pd

from .models import Trade


def process_trade_file(file, user):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df.date)
    df['ticker'] = df['ticker'].str.upper()
    for index, row in df.iterrows():
        instance = Trade(user=user, ticker=row['ticker'], date=row['date'],
                         price=row['price'], no_of_shares=row['shares'])
        instance.save()
