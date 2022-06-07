def convert_with_bin(num: int):
    # return bin(num).replace("0b", "")
    # return "{0:b}",format(num)
    return bin(n)[2:0]

def convert_with_recursion(num: int):
    if num >= 1:
        convert_with_recursion(num // 2)
    print(num % 2, end="")


print(convert_with_recursion(6))

