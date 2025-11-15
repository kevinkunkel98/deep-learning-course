random_dict = {
    'value0': 2.5,
    'value1': 3,
    'value2': 7.2,
    'value3': 2
}

def quadratic_float_dictionary(input_dict):
    return {
            key: value ** 2 if isinstance(value, float) else value
            for key, value in input_dict.items()
        }

squared_dict = quadratic_float_dictionary(random_dict)
print(squared_dict)

