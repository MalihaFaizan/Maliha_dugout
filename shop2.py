import numpy as np
bill = np.array([120, 80, 250, 60, 250, 310])
 
print(bill > 200)
print(bill == 250)

bill = np.array([120, 80, 250, 60, 250, 310])
 
big = bill > 200
 
print(big.sum())
print((bill == 250).sum())
print(bill[big])
print(bill[big].sum())

bill = np.array([120, 800, 250, 1500, 60])
 
# np.where(question, yes, no)
bonus = np.where(bill >= 1000, 100, 0)
print(bonus)
 
print(np.cumsum(bill))

