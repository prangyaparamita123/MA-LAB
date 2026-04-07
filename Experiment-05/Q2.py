def transpose(A):
  return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def multiply(A, B):
  is_b_1d = isinstance(B[0], (int, float))
  if is_b_1d:
    return [sum(A[i][k] * B[k] for k in range(len(B))) for i in range(len(A))]
  else:
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
      for j in range(len(B[0])):
        for k in range(len(B)):
          result[i][j] += A[i][k] * B[k][j]
    return result

def invert_matrix(matrix):
  n = len(matrix)
  identity = [[float(i == j) for j in range(n)] for i in range(n)]
  AM = [row[:] for row in matrix]
  for i in range(n):
    max_el = abs(AM[i][i])
    max_row = i
    for k in range(i + 1, n):
      if abs(AM[k][i]) > max_el:
        max_el = abs(AM[k][i])
        max_row = k

    if max_el < 1e-10:
      return None

    AM[i], AM[max_row] = AM[max_row], AM[i]
    identity[i], identity[max_row] = identity[max_row], identity[i]

    pivot = AM[i][i]
    for j in range(i, n):
      AM[i][j] /= pivot
    for j in range(n):
      identity[i][j] /= pivot

    for k in range(n):
      if k != i:
        factor = AM[k][i]
        for j in range(i,n):
          AM[k][j] -= factor * AM[i][j]
        for j in range(n):
          identity[k][j] -= factor * identity[i][j]

  return identity

try:
  print("--- Multiple Liner Regression (Manual Calculation) ---")
  n = int(input("Enter the number of data points (rows): "))
  k = int(input("Enter the number of features (independent variable): "))
  print(f"\nEnter the {k} features for each row :")
  x = []
  for i in range(n):
    while True:
      try:
        row_input = input(f"Row {i+1} features: ").split()
        row = [float(val) for val in row_input]
        if len(row) != k:
          print(f"Error: Expected {k} values. Please try again.")
          continue
        x.append([1.0]+row)
        break
      except ValueError:
        print("Error: Invalid input. Enter numbers only.")
  print("\nEnter the {n} target values (Y) separated by spaces:")
  while True:
    try:
      y_input = input("Y values: ").split()
      if len(y_input)!=n:
        print(f"Error: Excepted {n} values. Please try again.")
        continue
      y = [float(val) for val in y_input]
      break
    except ValueError:
      print("Error: Invalid input. Enter numbers only.")
  XT = transpose(x)
  XTX = multiply(XT, x)
  XTX_inv = invert_matrix(XTX)

  if XTX_inv is None:
    print("\n[!] Error: The matrix is singular (non-invertible). check for redundent data")
  else:
      XTY = multiply(XT, y)
      beta = multiply(XTX_inv, XTY)

      print("\n" + "="*45)
      print(f"{'variable':<20} | {'coefficient':<15}")
      print("-"*45)
      print(f"{'Intercept (B0)':<20} | {beta[0]:.4f}")
      for i in range(1, len(beta)):
        print(f"{f'Feature X{i} (B{i})':<20} | {beta[i]:.4f}")
      print("="*45)

except Exception as e:
  print(f"\nAn error occurred: {e}")