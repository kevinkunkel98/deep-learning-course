string_list1 = ["aaa", "bbb"]
string_list2 = ["ccc", "ddd"]

def combine_string_lists(list1, list2):
    combined_list = []

    for u in list1:
        for v in list2:
            combined_list.append(u + v)

    return combined_list

print(string_list1 + string_list2)
print(combine_string_lists(string_list1, string_list2))