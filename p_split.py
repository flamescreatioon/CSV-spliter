import pandas as pd

def split_csv_pandas(filename, chunksize):
    df = pd.read_csv(filename, chunksize=chunksize)
    chunk_num = 1

    for chunk in df:
        chunk.to_csv(f'chunk_{chunk_num}.csv', index=False)
        chunk_num += 1

filename = 'contacts.csv'
chunksize = 10000
split_csv_pandas(filename, chunksize)