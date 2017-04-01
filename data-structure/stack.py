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

# binary to decimal
def binary2Decimal(binaryNum):
    binary_reverse = str(binaryNum)[::-1]
    decimal_result = 0

    for index, b in enumerate(binary_reverse):
        if int(b) > 0:
            decimal_result += (2 ** index)

    return decimal_result

# hex to decimal
def hex2Decimal(hexNum):
    hex_reverse = str(hexNum)[::-1]
    hex_reference = '0123456789ABCDEF';
    decimal_result = 0

    for index, b in enumerate(hex_reverse):
        multiple = hex_reference.index(b)
        decimal_result += (16 ** index) * multiple

    return decimal_result

print('Decimal: {} -> Binary: {}'.format(100, decimalConvert(100, 2)))
print('Decimal: {} -> Hex: {}'.format(250, decimalConvert(250, 16)))
print('Binary: {} -> Decimal: {}'.format(10101, binary2Decimal(10101)))
print('Hex: {} -> Decimal: {}'.format('D1F', hex2Decimal('D1F')))
