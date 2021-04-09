
n = 1
while n <= 5:
    print(f'n: {n}')
    n = n + 1
    n += 1


active = True
nSum = 0.0

while active:
    ival = input('enter value:')
    if ival == 'quit':
        active = False
    else:
        nSum += float(ival)       

print(f"sum entered is { nSum }")