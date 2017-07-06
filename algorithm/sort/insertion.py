# -*- coding: utf-8 -*-
"""插入排序法"""

def insertion_sort(original_list):
    """
    透過遍歷陣列中元素
    並將當前元素的位置和值暫存起來
    當遍歷進行時，依序比較前面的元素
    如前一個元素大於當前元素，則將前一個元素放入當前的位置（當前元素依然存放在暫存中）
    在遍歷結束後，將放在暫存中的當前元素放在最小的位置上（最小的位置為結束迴圈時的索引）
    效率尚可
    """
    new_list = original_list[:]
    for i, val in enumerate(new_list):
        curr_index = i
        while curr_index > 0 and new_list[curr_index - 1] > val:
            new_list[curr_index] = new_list[curr_index - 1]
            curr_index -= 1
        new_list[curr_index] = val

    return new_list

EXAMPLE = [12, 22, 5, 3, 25, 33, 45, 10, 16, 20]
print(insertion_sort(EXAMPLE))
