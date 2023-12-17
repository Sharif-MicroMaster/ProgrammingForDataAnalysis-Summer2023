def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def decimal_to_base_k(decimal_num, k):
    if decimal_num == 0:
        return '0'

    result = ''
    while decimal_num > 0:
        remainder = decimal_num % k
        result = str(remainder) + result
        decimal_num //= k
    return result

def is_palindrome_in_base_k(num_str):
    return num_str == num_str[::-1]

def find_nth_palindrome_prime_in_base(n, k):
    count = 0
    num = 0

    while count < n:
        num_str = decimal_to_base_k(num, k)
        if is_palindrome_in_base_k(num_str) and is_prime(num):
            count += 1
        num += 1

    return num - 1

n, k = map(int, input().split())
print(find_nth_palindrome_prime_in_base(n, k))