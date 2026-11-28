import numpy as np

bills = np.array([120, 450, 80, 1200, 260, 95])

print(bills.sum(), bills.max(), bills.mean())

print(bills * 0.9)
print(bills)

print((bills * 0 + 300).sum())