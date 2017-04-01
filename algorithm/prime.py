num = int(raw_input("Give a range."))

import time

factors = []
factors.append(2)
tic = time.clock()

def f(i):
    for x in range(3, int(i/2+1), 2):
        if i % x == 0 and x != i:
            return False
    else:
        return True

for i in range(3, num + 1, 2):
    if f(i) == True:
        factors.append(i)

toc = time.clock()
time = toc - tic

print("Time cost: ", time)
print("Result: ", factors)
print("Length: ", len(factors))
