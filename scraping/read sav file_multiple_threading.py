import multiprocessing as mp
from time import time

import pandas as pd
import pyreadstat
import threading

def worker(inpt):
    import pyreadstat
    offset, chunksize, path = inpt
    df, meta = pyreadstat.read_sav(path, row_offset=offset, row_limit=chunksize)
    return df

# calculate the number of rows in the file
_, meta = pyreadstat.read_sav("Surgery.sav", metadataonly=True)
numrows = meta.number_rows
# calculate number of cores in the machine, this could also be set manually to some number, i.e. 8
numcores = mp.cpu_count()
# calculate the chunksize and offsets
divs = [numrows // numcores + (1 if x < numrows % numcores else 0)  for x in range (numcores) ]
chunksize = divs[0]
offsets = [indx*chunksize for indx in range(numcores)]
# pack the data for the jobs
jobs = [(x, chunksize, "Surgery.sav") for x in offsets]

threads = []
max_threads = 100
while threads or jobs:
    for thread in threads:
        if not thread.is_alive():
            threads.remove(thread)

    while len(threads) < max_threads and jobs:
        job = jobs.pop()
        thread = threading.Thread(target=worker, args=(job,))
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)