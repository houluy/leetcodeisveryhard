def is_valid(s):
    starting = ['{', '[', '(']
    ending = ['}', ']', ')']
    mapping = dict(zip(starting, ending))
    d = []
    for i in s:
        if i in starting:
            d.append(mapping.get(i))
        else:
            if not d or d.pop() != i:
                return False
    return False if d else True

if __name__ == '__main__':
    test_data = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "}",
        "{",
    ]
    for d in test_data:
        print(is_valid(d))
