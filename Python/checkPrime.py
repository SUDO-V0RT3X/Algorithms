def isPrime(n, i):
    
    if (n == 0 or n == 1):
        return False

    elif (n == i):
        return True

    elif (n % i == 0):
        return False

    i += 1 

    return isPrime (n, i)


if (isPrime(int(input("Enter a number to check: ")), 2)):
    print("Yaaa it is broski")
else:
    print("Nahhhhh it ain't boet")
