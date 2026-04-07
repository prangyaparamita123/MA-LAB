import numpy as np
from scipy import stats

try:
  raw_x = input("Enter X values separated by space: ")
  raw_y = input("Enter X values separated by space: ")

  x=np.array([float(i) for i in raw_x.split()])
  y=np.array([float(i) for i in raw_y.split()])

  slope, intercept, _, _, _=stats.linregress(x,y)

  print(f"slope (m): {slope:.4f}")
  print(f"intercept (c): {intercept:.4f}")
  print(f"Equation: Y ={slope:.4f}X + {intercept:.4f}")
except Exception as e:
  print(e)