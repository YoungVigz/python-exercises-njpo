import pickle
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import time
import numpy as np

def generate_data(size):
    return list(np.random.randint(0, 100, size))

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def save_to_parquet(data, filename):
    df = pd.DataFrame(data, columns=['value'])
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)

def save_to_xlsx(data, filename):
    df = pd.DataFrame(data, columns=['value'])
    df.to_excel(filename, index=False)

def benchmark(size):
    data = generate_data(size)
    
    start = time.time()
    save_to_pickle(data, 'data.pkl')
    save_time_pickle = time.time() - start
    
    start = time.time()
    save_to_parquet(data, 'data.parquet')
    save_time_parquet = time.time() - start
    
    start = time.time()
    save_to_xlsx(data, 'data.xlsx')
    save_time_xlsx = time.time() - start
    
    return {
        'pickle': save_time_pickle,
        'parquet': save_time_parquet,
        'xlsx': save_time_xlsx
    }

sizes = [100, 10000, 100000]
results = {size: benchmark(size) for size in sizes}

for size, times in results.items():
    print(f"\nDla {size} elemetnów:")
    for method, save_time in times.items():
        print(f"{method}: {save_time:.6f}s")
