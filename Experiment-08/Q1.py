import math

def distance(p1, p2):
  sum_val = 0
  for i in range(len(p1)):
    sum_val += (p1[i] - p2[i])**2
  return math.sqrt(sum_val)

def knn(train_data, train_labels, test_point, k):
  dist = []
  for i in range(len(train_data)):
    d = distance(train_data[i], test_point)
    dist.append((d,train_labels[i]))
  dist.sort()
  count = {}
  for i in range(k):
    label = dist[i][1]
    if label in count:
      count[label] += 1
    else:
      count[label] = 1
  prediction = max(count, key=count.get)
  return prediction

n = int(input("Enter number of training data points : "))
f = int(input("Enter number of features : "))

train_data = []
train_labels = []

print("\nEnter training data :")
for i in range(n):
  point = []
  for j in range(f):
    val = float(input(f"Enter feature {j+1} :"))
    point.append(val)
  label = input("Enter class label :")
  train_data.append(point)
  train_labels.append(label)


test_point = []
print("\nEnter test data :")
for i in range(f):
  val = float(input(f"Enter feature {i+1} : "))
  test_point.append(val)

k = int(input("Enter value of k : "))
result = knn(train_data, train_labels, test_point, k)
print(f"\nPredicted class : {result}")

     


#.02

from itertools import count
def naive_bayes(train_data, train_labels, test):
  classes = {}
  for label in train_labels:
    if label in classes:
      classes[label] += 1
    else:
      classes[label] = 1
  total = len(train_labels)
  probabilites = {}

  for c in classes:
    prior = classes[c] / total
    likelihood = 1

    for i in range(len(test)):
      count = 0
      class_count = 0
      for j in range(len(train_data)):
        if train_labels[j] == c:
          class_count += 1
          if train_data[j][i] == test[i]:
            count += 1
      if class_count != 0:
        likelihood *= (count / class_count)
    probabilites[c] = prior * likelihood
  prediction = max(probabilites, key=probabilites.get)
  return prediction

n = int(input("Enter number of training data :"))
f = int(input("Enter number of features :"))

train_data = []
train_labels = []

print("\nEnter training data : ")
for i in range(n):
  row = []
  for j in range(f):
    val = input(f"Enter feature {j+1} :")
    row.append(val)
  label = input("Enter class label :")
  train_data.append(row)
  train_labels.append(label)

test = []
print("\nEnter test data :")
for i in range(f):
  val = input(f"Enter feature {i+1} :")
  test.append(val)

result = naive_bayes(train_data, train_labels, test)
print("\nPredicted Class :", result)
     
