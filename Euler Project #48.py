import time
start = time.time()

def Self_powers(n):
    sums =[]
    for x in range(1,n):
        sums.append(x**x)
    print((str(sum(sums)))[-10:])

Self_powers(1001)
end = time.time()
print(end - start)