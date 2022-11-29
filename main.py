x = [5, 2, 3, 1, 4, -1, 3213, 23, 56, -245]

for j in range(len(x)):
    for i in range(j):
        if x[i] > x[i+1] :
            teomp= x[i]
            x[i] = x[i+1]
            x[i + 1] = teomp
        print(x)

