def is_binary(argument):
    binary_chars = {'0', '1'}
    for char in argument:
        if char not in binary_chars:
            return False
    return True


numbers = list(filter(is_binary, ["1101", "6", "0110", "24"]))
print(numbers)
