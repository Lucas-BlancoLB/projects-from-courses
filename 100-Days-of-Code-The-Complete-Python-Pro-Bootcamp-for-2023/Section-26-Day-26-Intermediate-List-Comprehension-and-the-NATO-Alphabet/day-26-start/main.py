NUMBERS = [1,2,3]

num_add_1 = [n + 1 for n in NUMBERS]
print(NUMBERS, num_add_1)

name = "Lucas"

letter_list = ["_" + letter + "_" for letter in name]
print(name, letter_list)

range_num = range(1,5)
doable_numb = [n * 2 for n in range_num]
print(range_num, doable_numb)

doable_numb = [n * 2 for n in range(1, 5)]
print(doable_numb)

even_num_in_100 = [x for x in range(1, 101) if x % 2 == 0]
print(even_num_in_100)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
long_names = [x.upper() for x in names if len(x) >= 5]
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_number = [n ** 2 for n in numbers]
print(squared_number)

num_input = ['1', ' 1', ' 2', ' 3', ' 5', ' 8', ' 13', ' 21', ' 34', ' 55']
clear_list = [int(x.strip()) for x in num_input ]
even_nums = [n for n in clear_list if n % 2 == 0]
print(clear_list, even_nums)

###

with open("file1.txt") as file1, open("file2.txt") as file2:
    data1, data2 = file1.read(), file2.read()
    data1, data2 = [int(x) for x in data1.splitlines()], [int(x) for x in data2.splitlines()]
    same_num = [x for x in data1 if x in data2]
    print(same_num)










