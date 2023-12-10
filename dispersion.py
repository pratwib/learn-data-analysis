import numpy as np
import pandas as pd

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

range = jumlah_kucing.max() - jumlah_kucing.min()
print(range)

iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print(iqr)

jumlah_kucing_series = pd.Series(jumlah_kucing)
variance = jumlah_kucing_series.var()
print(variance)

std = jumlah_kucing_series.std()
print(std)
