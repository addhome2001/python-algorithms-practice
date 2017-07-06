# -*- coding: utf-8 -*-
"""選擇排序法"""

def selection_sort(original_list):
    """
    透過遍歷陣列中元素
    並假設當前位置為最小元素，且將它的位置暫存起來
    當遍歷進行時，如遇到更小元素，則改變最小元素的位置參考
    在遍歷結束後，如最小元素的位置已改變
    則將當前元素和最小元素做替換
    需要進行兩層比較：
        在進行第二層比較時，由於最左邊是已經排序過的（較小的數字）
        故第二層的範圍會以第一層為起始點
    效率也算差
    """
    new_list = original_list[:]
    for i, _ in enumerate(new_list):
        min_index = i
        for j, target in enumerate(new_list[i:]):
            target_index = j + i
            if new_list[min_index] > target:
                min_index = target_index

        if i != min_index:
            new_list[i], new_list[min_index] = new_list[min_index], new_list[i]

    return new_list

EXAMPLE = [12, 22, 5, 3, 25, 33, 45, 10, 16, 20]
print(selection_sort(EXAMPLE))
