def addBinary(a, b):
    ind = 0
    length_a = len(a)
    length_b = len(b)
    output = []
    carry = 0
    while True:
        if (ind >= length_a and ind >= length_b):
            if carry == 1:
                output.insert(0, str(carry))
            break
        a_i = int(a[length_a - ind - 1]) if ind < length_a else 0
        b_i = int(b[length_b - ind - 1]) if ind < length_b else 0
        carry, c_i = divmod((a_i + b_i + carry), 2)
        output.insert(0, str(c_i))
        ind += 1
    return ''.join(output)

def addBinary(a, b):
    return '{0:b}'.format(int(a, 2) + int(b, 2))

a = ["11", "1010"]
b = ["1", "1011"]

for i in range(len(a)):
    print(a[i], b[i])
    print(addBinary(a[i], b[i]))
