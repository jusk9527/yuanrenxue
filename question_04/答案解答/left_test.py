num_list = [[8, 23.0], [6, -11.5], [1, 11.5], [0, -23.0]]			#
new_num_list = num_list.copy()
for i, tup in enumerate(num_list):
    index = int(tup[1] / 11.5)
    if index != 0:
        new_num_list[i + index] = num_list[i]
num_str = ''.join([str(num[0]) for num in new_num_list])

print(num_str)
# 6081
