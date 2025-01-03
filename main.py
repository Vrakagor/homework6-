def split_list(lst):
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]

my_list = [1, 2, 3, 4, 5]
result_list = split_list(my_list)
print(result_list)
