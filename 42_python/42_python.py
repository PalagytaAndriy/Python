import re

def is_valid_IP(string):
    return True if re.search(r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",string) != None else False


print(is_valid_IP('12.255.56.1'))
print(is_valid_IP(''))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('123.456.789.0'))
print(is_valid_IP('12.34.56'))
print(is_valid_IP('123.045.067.089'))