def format_number(num):
    formatted_num = "{:,}".format(num)
    return formatted_num

# cases
f1 = format_number(1)
print(f1)

f2 = format_number(11)
print(f2)

f3 = format_number(12)
print(f3)

f4 = format_number(123)
print(f4)

f5 = format_number(1234)
print(f5)

f6 = format_number(12345)
print(f6)

f7 = format_number(123456)
print(f7)

f8 = format_number(1234567)
print(f8)
# extra cases
f9 = format_number(12345678)
print(f9)

f10 = format_number(123456789)
print(f9)

f11 = format_number(29371989128)
print(f11)

f12 = format_number(99999999999999)
print(f12)