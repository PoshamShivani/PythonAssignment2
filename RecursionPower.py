def power(b, e):
    if e == 1:
        return b
    if e != 1:
        return b * power(b, e - 1)


b = int(input())
e = int(input())
print(power(b, e))
