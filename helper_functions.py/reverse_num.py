def reverse_num(given_num: int):
    reversed_num = 0
    while given_num > 0:
        reversed_num *= 10
        reversed_num += given_num % 10
        given_num //= 10
    return reversed_num


print(reverse_num(3125784))