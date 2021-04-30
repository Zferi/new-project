a = int(input('Enter a positive integer: '))
r = -1
while a > 10:
    d = a % 10
    a //= 10
    if d > r:
        r = d
print(r)
