

student_name = "Eugene Boachie"
student_email = "ekb5621@psu.edu"
student_section = "004"

def list_xor(n, list1, list2):
    if 0 <= n < min(len(list1), len(list2)):
        result = bool((list1[n] and not list2[n]) or (not list1[n] and list2[n]))
        return result
    else:
        return False

l1 = list_xor(1, [1, 2, 3], [4, 5, 6])
print(l1)

l2 = list_xor(1, [0, 2, 3], [1, 5, 6])
print(l2)

l3 = list_xor(1, [1, 2, 3], [1, 5, 6])
print(l3)

l4 = list_xor(1, [2, 3, 4], [4, 5, 6])
print(l4)

# test cases
l5 = list_xor(0, [1, 0, 1], [0, 1, 1])
print(l5)

l6 = list_xor(2, [6, 5, 4], [3, 2, 1])
print(l6)
pass
#

def dict_extend(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        if key in dict2:
            result[key] = [value] + [dict2[key]]
        else:
            result[key] = [value]
    for key, value in dict2.items():
        if key not in result:
            result[key] = [value]
    return result

# cases
d1 = dict_extend({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400})
print(d1)

d2 = dict_extend({1: 'One', 2: 'Two'}, {})
print(d2)
# extra cases
d3 = dict_extend({'a': [2, 4], 'b': [6]}, {'a': [8], 'c': [10,12]})
print(d3)

d4 = dict_extend({1: 'rice', 2: 'chicken'}, {1: 'beans', 3: 'eggs'})
print(d4)

d5 = dict_extend({2: 'LEGO', 4: 'Hasbro'}, {2: 'Barbie', 4: 'Play-Doh'})
print(d5)
pass

def camel_case(var_name):
    words = var_name.split('_')
    words = [word for word in words if word]
    camel_case_name = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    return camel_case_name

# test cases
c1 = camel_case("to_camel_case")
print(c1)

c2 = camel_case("tO_cAMeL_CaSe")
print(c2)

c3 = camel_case("__TO_CAMEL____CASE")
print(c3)

c4 = camel_case("___")
print(c4)
# cases
c5 = camel_case("__to___CaMeL_CaSE")
print(c5)

c6 = camel_case("__TO__camel__CASE")
print(c6)

c7 = camel_case("_To_Camel_CaSe")
print(c7)
pass

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