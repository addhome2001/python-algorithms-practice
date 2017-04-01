class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) <= 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# practice

# decimal convert
def decimalConvert(intNum, base):
    remainder_num = intNum
    rem_stack = Stack()
    result = ''
    reference = '0123456789ABCDEF';

    while (remainder_num > 0):
        rem_stack.push(reference[remainder_num % base])
        remainder_num = remainder_num // base

    while (not rem_stack.isEmpty()):
        result += str(rem_stack.pop())

    return result

# convert to decimal
def toDecimal(num, base):
    reverse = str(num)[::-1]
    reference = '0123456789ABCDEF';
    decimal_result = 0

    for index, b in enumerate(reverse):
        multiple = reference.index(b)
        decimal_result += (base ** index) * multiple

    return decimal_result

print('Decimal: {} -> Binary: {}'.format(100, decimalConvert(100, 2)))
print('Decimal: {} -> Hex: {}'.format(250, decimalConvert(250, 16)))
print('Binary: {} -> Decimal: {}'.format(10101, toDecimal(10101, 2)))
print('Hex: {} -> Decimal: {}'.format('D1F', toDecimal('D1F', 16)))
