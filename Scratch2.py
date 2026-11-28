import numpy as np

bills = np.array([120, 450, 80, 1200, 260, 95])

print((bills > 200).sum())
print(bills[bills > 200].sum())
print((bills == 80).sum())
print((bills > 200).mean())
