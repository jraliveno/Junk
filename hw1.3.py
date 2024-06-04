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


