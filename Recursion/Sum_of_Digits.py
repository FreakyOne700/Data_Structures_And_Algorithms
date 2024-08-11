def sumOfDigits(n):
    assert n>=0 and int(n) == n , "Numbers Should be positive only"
    if n==0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))
    
print(sumOfDigits(12423))