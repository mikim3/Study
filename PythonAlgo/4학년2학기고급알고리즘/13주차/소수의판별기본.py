
def is_prime_num(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

print(is_prime_num(4))
print(is_prime_num(7))
    