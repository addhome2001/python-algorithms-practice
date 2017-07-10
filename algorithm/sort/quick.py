# -*- coding: utf-8 -*-
"""快速排序法"""

def quick_sort(original_list):
    """
    為分治演算法的一種
    需以遞迴排列
    是非常用常的排序演算法
    """
    return quick_recursive(original_list[:])

def quick_recursive(sub_list):
    """
    在將原陣列進行分治排序後
    可得到分治點，而分治點的左數字會小於分治點、右邊會大於分治點
    以分治點進行切割後
    以遞迴的方式對左右陣列重複同樣操作
    直到陣列長度為1為止
    """
    if len(sub_list) > 1:
        index = partition(sub_list)

        if index < len(sub_list) and index > 0:
            return quick_recursive(sub_list[:index]) + quick_recursive(sub_list[index:])

    return sub_list

def partition(sub_list):
    """
    得到分治點後
    找到小於（左邊）、大於（右邊）的數字時
    代表排序位置正確
    則將索引加1
    直到該索引的數字需被排序（和原本邏輯相反）
    最後將左右兩邊需被排序的數字對調
    並將兩邊索引值加1
    直到左邊索引大於右邊索引
    """
    mid = sub_list[len(sub_list) // 2]
    l_index = 0
    r_index = len(sub_list) - 1

    while l_index <= r_index:
        while sub_list[l_index] < mid:
            l_index += 1

        while sub_list[r_index] > mid:
            r_index -= 1

        if l_index <= r_index:
            sub_list[l_index], sub_list[r_index] = sub_list[r_index], sub_list[l_index]
            l_index += 1
            r_index -= 1

    return l_index

EXAMPLE = [12, 22, 5, 3, 25, 33, 45, 16, 10, 20]
print(quick_sort(EXAMPLE))
