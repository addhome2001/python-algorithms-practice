#-*- coding: utf-8 -*-

# 給出一個數，並算出範圍中的質數
num = int(raw_input("Give a range."))

import time

factors = []
# 因為2為第一個質數，所以跳過判斷2是質數的步驟
factors.append(2)

# 計算運算時間開始
tic = time.clock()

def f(i):
    # 因後半段因數包含了前半段，故只在只計算前半段
    for x in range(3, int(i/2+1), 2):
        if i % x == 0 and x != i:
            return False
    else:
        return True

# 每次加2，因為偶數不可能為質數
for i in range(3, num + 1, 2):
    if f(i) == True:
        factors.append(i)

# 計算運算時間結束
toc = time.clock()
time = toc - tic

print("Time cost: ", time)
print("Result: ", factors)
print("Length: ", len(factors))
