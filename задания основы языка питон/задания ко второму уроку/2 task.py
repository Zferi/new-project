while True:
    num = int(input('enter number 1-10: '))
    if num <= 0:
        print('repeat')
        continue
    if num >= 10:
        print('repeat')
        continue
    else:
        num = num ** 2
    print(num)
    break
