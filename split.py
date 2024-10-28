import csv

def split_csv(filename, chunksize):
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        chunk = []
        chunk_num = 1

        for row in reader:
            chunk.append(row)
            if len(chunk) == chunksize:
                with open(f'chunk_{chunk_num}.csv', 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(chunk)
                chunk = []
                chunk_num += 1  

        if chunk:
            with open(f'chunk_{chunk_num}.csv', 'w', newline='', encoding='utf-8') as chunk_file:
                writer = csv.writer(chunk_file)
                writer.writerows(chunk)

filename = 'contacts 2.csv'
chunksize = 10000
split_csv(filename, chunksize)