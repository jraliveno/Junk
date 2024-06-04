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
print(d1)  # Output: {'a': [100, 300], 'b': [200, 200], 'c': [300], 'd': [400]}

d2 = dict_extend({1: 'One', 2: 'Two'}, {})
print(d2)  # Output: {1: ['One'], 2: ['Two']}
# extra cases
d3 = dict_extend({'a': [2, 4], 'b': [6]}, {'a': [8], 'c': [10,12]})
print(d3)

d4 = dict_extend({1: 'rice', 2: 'chicken'}, {1: 'beans', 3: 'eggs'})
print(d4)

d5 = dict_extend({2: 'LEGO', 4: 'Hasbro'}, {2: 'Barbie', 4: 'Play-Doh'})
print(d5)
