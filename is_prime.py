def is_prime(num):
    is_divisible=False
    for i in range(2,num-1):
        if num%i==0:
            is_divisible=True
    if is_divisible:
        return False
    else:
        return True
