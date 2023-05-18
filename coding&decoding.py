import random


def coding(line):
    result, mult = [], random.randint(1, 9)
    for i in line:
        result.append(chr(ord(i) + mult))
    result.append(mult)
    result = list(map(lambda x: str(x), result))
    return "".join(result)


def decode(line):
    result, mult = [], line[-1]
    for i in line:
        result.append(chr(ord(i) - int(mult)))
    result.pop()
    return "".join(result)


if __name__ == "__main__":
    a = coding("Hello word!")
    print(a)
    print(decode(a))
