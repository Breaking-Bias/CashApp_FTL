import pandas as pd

PATH = 'data/'
file_names = ['customers_data', 'synthetic_data', 'transaction_data']

for file_name in file_names:
    dataframe = pd.read_parquet(PATH + file_name + '.pq')
    dataframe.to_csv(PATH + file_name + '.csv')