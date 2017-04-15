#-*- coding: utf-8 -*-

# 算出阿姆斯壯數
# 從一個範圍算出所有阿姆斯壯數
def find_armstrong_range(n):
    # 暫存的dictionary
    n_dices = {}
    # 結果陣列
    result = []

    for i in range(n + 1):
        seperate_num_list = list(str(i))
        # 先將數字進行排序，並放入暫存
        # 例如123、231、321結果相同，用暫存可避免重複計算
        seperate_num_list.sort()
        alias = ''.join(seperate_num_list)
        alias_len = len(alias)

        if alias not in n_dices:
            sum_a = 0
            for x in alias:
                sum_a += int(x) ** alias_len
            n_dices[alias] = sum_a

        if n_dices[alias] == i:
            result.append(i)

    return result

# 從一個為數算出所有阿姆斯壯數，例如3位數
def find_armstrong_digit(n):
    digit_start = '1' + ((n - 1) * str(0))
    digit_end = '1' + (n * str(0))
    # 暫存的dictionary
    n_dices = {}
    # 結果陣列
    result = []

    for i in range(int(digit_start), int(digit_end)):
        seperate_num_list = list(str(i))
        # 先將數字進行排序，並放入暫存
        # 例如123、231、321結果相同，用暫存可避免重複計算
        seperate_num_list.sort()
        alias = ''.join(seperate_num_list)

        if alias not in n_dices:
            sum_a = 0
            for x in alias:
                sum_a += int(x) ** n
            n_dices[alias] = sum_a

        if n_dices[alias] == i:
            result.append(i)

    return result


print(find_armstrong_digit(3))
print(find_armstrong_range(1000))
