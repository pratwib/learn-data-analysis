import numpy as np
from scipy import stats

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

mean_jumlah_kucing = jumlah_kucing.mean()
print(mean_jumlah_kucing)

median_jumlah_kucing = np.median(jumlah_kucing)
print(median_jumlah_kucing)

mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]
print(mode_jumlah_kucing)
