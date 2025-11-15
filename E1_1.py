"E_1_1"

float_list = [1.2, 3.4, 5.6]

def add_sub_floats(float_list, value):
    add_float_list = []
    sub_float_list = []

    for item in float_list:
        add_float_list.append(item + value)
        sub_float_list.append(item - value)

    return add_float_list, sub_float_list


print(float_list)
print(add_sub_floats(float_list, 2))



