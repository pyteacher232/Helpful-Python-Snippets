import itertools

for i in itertools.product([1, 2, 3], ['a', 'b'], [4, 5]):
    # print(i)
    pass

total_list = ([1, 2, 3], ['a', 'b'], [4, 5])
for i in itertools.product(*total_list):
    print(i)