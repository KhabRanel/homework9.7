def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        k = 0
        for i in range(2, num):
            if num % i == 0:
                k += 1
                break
        if k == 0:
            print("Простое")
        else:
            print("Составное")
        return func(*args)
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
