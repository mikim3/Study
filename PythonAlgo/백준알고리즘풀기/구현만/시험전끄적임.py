rows = 10
cols = 5
arr = [[0 for j in range(cols)] for i in range(rows)]

print(arr)

arr[0][0] = 1
print(arr)

for i in range(len(arr)):
  print(arr[i])
# arr[rows][cols] 임