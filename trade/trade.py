import time

import pandas as pd

from pipeline import prepare_data as prep
from pipeline.luno_api import TradeLuno

from algorithm.NN import NeuralNetwork


tl = TradeLuno()

api_file = 'home/kautuboy/repositories/kauta_web_app/data/test_luno.csv'


def main_nn(currency_pairs):
    nn = NeuralNetwork()                                                        # Initialize Neural Net

    tl.get_balance()                                                            # Get account balance from API
    for pair in currency_pairs:
        df = pd.read_csv(tl.price_files[pair], header=0)                        # Read price data from file
        # Get ticker data from API
        ticker = tl.get_ticker(pair)
        tl.current_price[pair] = prep.get_bid_price(ticker)
        # Check if API failed - if it fails, pause process for 60s then call API again
        if tl.current_price == -1.0:
            time.sleep(60)
            ticker = tl.get_ticker(pair)
            price_bid = prep.get_bid_price(ticker)
            if price_bid == -1.0:
                continue
        df_prices = prep.append_list_to_df(df, [[tl.current_price[pair]]])      # Append current price to previous
        df_perc = prep.calculate_perc_change(df_prices)                         # Prepare data into perc
        output = nn.feedforward(df_perc.values.reshape(1, 30))                  # NN makes market prediction: 0-1
        tl.order_type(output[0][0])                                             # Order type BUY/SELL
        tl.trade_currency_pair(pair)                                            # Post SELL/BUY order to API
        # Write process to file
        df_2 = prep.append_list_to_df(df, [[tl.current_price[pair]]])
        prep.write_df_to_file(df_2, tl.price_files[pair], rows=30)
        ticker['type'] = tl.type
        prep.write_dict_to_file(ticker, api_file)


if __name__ == '__main__':
    currency_pairs = ['XBTZAR']                                                 #, 'ETHZAR'
    main_nn(currency_pairs)
