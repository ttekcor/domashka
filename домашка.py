file = open("17_6024.txt", "r")

arr = []

for line in file.readlines():
    arr.append(int(line))
print(arr)
pairs_count = 0
summ = 0
max_count = 0 

for a in arr:
    if abs(a) % 100 == 12:
        max_count = max(abs(a), max_count)

for i in range(0, arr.__len__()-1):
    p1 = arr[i]
    p2 = arr[i+1]

    if ((p1 % 100 == 12) ^ (p2 % 100 == 12)) and ((p1 + p2) ** 2) < (max_count ** 2):
        pairs_count += 1

        if (p1 + p2) > summ:
            summ = p1 + p2 

print(pairs_count, summ)