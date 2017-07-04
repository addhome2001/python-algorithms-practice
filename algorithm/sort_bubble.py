# -*- coding: utf-8 -*-
"""泡泡排序法"""

def bubble_sort(original_list):
    """
    透過與下一個項目進行比較，並且交換位置
    需要進行兩層比較：
        在進行第二層比較時，由於最右邊是已經排序過的（較大的數字）
        故第二層的範圍會是第一層剩下的數字
    效率非常的差
    """
    new_list = original_list[:]
    list_len = len(new_list)
    last_index = list_len - 1
    remainder_len = list_len + 1
    for i, _ in enumerate(new_list):
        for j, val in enumerate(new_list[:remainder_len - i]):
            if last_index > j and val > new_list[j + 1]:
                new_list[j + 1], new_list[j] = new_list[j], new_list[j + 1]

    return new_list

EXAMPLE = [12, 22, 5, 3, 25, 33, 45, 10, 16, 20]
print(bubble_sort(EXAMPLE))
