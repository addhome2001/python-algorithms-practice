# -*- coding: utf-8 -*-
"""合併排序法"""

def merge_sort(original_list):
    """
    為分治演算法的一種
    需以遞迴排列
    算是常用的排序演算法
    """
    return merge_recursive(original_list)

def merge_recursive(sub_list):
    """
    將陣列進行對切
    直至長度為1為止，才對分割後的左右兩邊進行合併
    """
    list_len = len(sub_list)
    if list_len <= 1:
        return sub_list

    mid = list_len // 2
    left = sub_list[:mid]
    right = sub_list[mid:]
    return merge_list(merge_recursive(left), merge_recursive(right))

def merge_list(left, right):
    """
    在合併的同時進行排序
    合併前判斷較小一方，並將其推入結果陣列
    之後將該方索引變數加一
    當有某一方的索引變數不再小於長度時
    代表該方的陣列已被推入結果陣列
    這時將另一方的陣列依序推入結果陣列（雙方都已經排序過）
    最後返回結果陣列
    """
    result = []
    l_c = 0
    r_c = 0
    while l_c < len(left) and r_c < len(right):
        if left[l_c] < right[r_c]:
            result.append(left[l_c])
            l_c += 1
        else:
            result.append(right[r_c])
            r_c += 1

    while l_c < len(left):
        result.append(left[l_c])
        l_c += 1

    while r_c < len(right):
        result.append(right[r_c])
        r_c += 1

    return result

EXAMPLE = [12, 22, 5, 3, 25, 33, 45, 10, 16, 20]
print(merge_sort(EXAMPLE))
