# -*- coding: utf-8 -*-
"""堆疊"""

class Stack(object):
    """
    堆疊類別
    為後進先出的資料結構
    資料的操作都在資料結構的最前方
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        判斷堆疊是長度否為空
        """
        return len(self.items) <= 0

    def push(self, item):
        """
        新增資料
        從頭部入堆資料
        """
        self.items.append(item)

    def pop(self):
        """
        移除資料
        從頭部出堆資料
        """
        if not self.is_empty():
            return self.items.pop()
        return False

    def size(self):
        """
        返回堆疊長度
        """
        return len(self.items)

    def clear(self):
        """
        清空該堆疊
        """
        self.items = []

# practice
def decimal_convert(int_num, base):
    """
    十進制轉換十六進制
    """
    remainder_num = int_num
    rem_stack = Stack()
    result = ''
    reference = '0123456789ABCDEF'

    while remainder_num > 0:
        rem_stack.push(reference[remainder_num % base])
        remainder_num = remainder_num // base

    while not rem_stack.is_empty():
        result += str(rem_stack.pop())

    return result

def to_decimal(num, base):
    """
    十六進制轉換十進制
    """
    reverse = str(num)[::-1]
    reference = '0123456789ABCDEF'
    decimal_result = 0

    for index, val in enumerate(reverse):
        multiple = reference.index(val)
        decimal_result += (base ** index) * multiple

    return decimal_result

if __name__ == '__main__':
    print('Decimal: {} -> Binary: {}'.format(100, decimal_convert(100, 2)))
    print('Decimal: {} -> Hex: {}'.format(250, decimal_convert(250, 16)))
    print('Binary: {} -> Decimal: {}'.format(10101, to_decimal(10101, 2)))
    print('Hex: {} -> Decimal: {}'.format('D1F', to_decimal('D1F', 16)))
