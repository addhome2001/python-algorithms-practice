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

# decimal to binary
def decimal2Binary(intNum):
    remainder_num = intNum
    binary_stack = Stack()
    binary_result = ''

    while (remainder_num > 0):
        binary_stack.push(remainder_num % 2)
        remainder_num = remainder_num // 2

    while (not binary_stack.isEmpty()):
        binary_result += str(binary_stack.pop())

    return binary_result

# binary to decimal
def binary2Decimal(binaryNum):
    binary_reverse = str(binaryNum)[::-1]
    decimal_result = 0

    for index, b in enumerate(binary_reverse):
        if int(b) > 0:
            decimal_result += (2 ** index)

    return decimal_result

# decimal to hex
def decimal2Hex(intNum):
    remainder_num = intNum
    hex_stack = Stack()
    hex_result = ''
    hex_reference = '0123456789ABCDEF';

    while (remainder_num > 0):
        remainder = remainder_num % 16;
        hex_stack.push(hex_reference[remainder])
        remainder_num = remainder_num // 16

    while (not hex_stack.isEmpty()):
        hex_result += str(hex_stack.pop())

    return hex_result

# hex to decimal
def hex2Decimal(hexNum):
    hex_reverse = str(hexNum)[::-1]
    hex_reference = '0123456789ABCDEF';
    decimal_result = 0

    for index, b in enumerate(hex_reverse):
        multiple = hex_reference.index(b)
        decimal_result += (16 ** index) * multiple

    return decimal_result

print('Decimal: {} -> Binary: {}'.format(100, decimal2Binary(100)))
print('Decimal: {} -> Hex: {}'.format(250, decimal2Hex(250)))
print('Binary: {} -> Decimal: {}'.format(10101, binary2Decimal(10101)))
print('Hex: {} -> Decimal: {}'.format('D1F', hex2Decimal('D1F')))
