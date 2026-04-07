import math

print("--- Logistic Regression (Gradient Descent) ---")

n = int(input("Enter the number of data points (rows): "))

x1_list = []
x2_list = []
y_list = []

print("\nEnter x1, x2 and y (0 or 1) for each row (space-separated): ")
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    x1_list.append(row[0])
    x2_list.append(row[1])
    y_list.append(row[2])


b0 = 0
b1 = 0
b2 = 0

learning_rate = 0.01
epochs = 1000


def sigmoid(z):
    if z >= 0:
        return 1 / (1 + math.exp(-z))
    else:
        return math.exp(z) / (1 + math.exp(z))


for epoch in range(epochs):
    db0 = 0
    db1 = 0
    db2 = 0

    for i in range(n):
        z = b0 + b1 * x1_list[i] + b2 * x2_list[i]
        y_pred = sigmoid(z)

        error = y_pred - y_list[i]

        db0 += error
        db1 += error * x1_list[i]
        db2 += error * x2_list[i]


    b0 -= learning_rate * db0 / n
    b1 -= learning_rate * db1 / n
    b2 -= learning_rate * db2 / n

print("\nCalculated coefficients:")
print(f"b0 (intercept): {b0:.4f}")
print(f"b1 (coefficient for x1): {b1:.4f}")
print(f"b2 (coefficient for x2): {b2:.4f}")


test = input("\nWould you like to predict a value? (y/n): ")
if test.lower() == 'y':
    tx1, tx2 = map(float, input("Enter new x1 and x2: ").split())

    z = b0 + b1 * tx1 + b2 * tx2
    prob = sigmoid(z)

    prediction = 1 if prob >= 0.5 else 0

    print(f"Predicted probability: {prob:.4f}")
    print(f"Predicted class: {prediction}")
     
