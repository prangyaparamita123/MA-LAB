try:
  raw_x = input("Enter x values separated by space: ")
  raw_y = input("Enter y values separated by space: ")

  x = [float(i) for i in raw_x.split()]
  y = [float(i) for i in raw_y.split()]

  n = len(x)

  if n != len(y):
    print("Error: The number of X and Y values must be the same.")
  elif n < 2:
    print("Error: You need at least two points to form a line.")
  else:
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x_sq = sum([x[i] ** 2 for i in range(n)])

    numerator_m = (n * sum_xy) - (sum_x * sum_y)
    denominator_m = (n * sum_x_sq) - (sum_x ** 2)

    if denominator_m == 0:
      print("Error: Vertical line detected (denominator is zero).")
    else:
      m = numerator_m / denominator_m

      c = (sum_y - (m * sum_x)) / n

      print("\n" + "-"*30)
      print(f"Slope (m):     {m:.4f}")
      print(f"Intercept (c): {c:.4f}")
      print(f"Equation:      y = {m:.4f}x + {c:.4f}")
      print("-"*30)

except ValueError:
    print("Error: Please enter only numbers separated by spaces.")
