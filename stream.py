# String has to be encoded and hexified
# key is in hexadecimal

str1 = "Agnes Driscoll".encode().hex()
str2 = "4bc26cbad972b0eee988e28a4d64"


def change_to_be_hex(to_str):
    return int(to_str, 16)


def xor_two_str(s1, s2):
    a = change_to_be_hex(s1)
    b = change_to_be_hex(s2)
    return hex(a ^ b)


out = xor_two_str(str1, str2)
print(out[2:])
