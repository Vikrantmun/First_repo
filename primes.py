p = int(input('write the no to check: '))
if p >= 1:
    for i in range(2, p + 1):
        if (p % 2 == 0):
            print(p, "is not prime")
            break
        elif (p % i == 0):
            print(p, "is not prime")
            break
        else:
            print(p, "is a prime")
else:
    pass
