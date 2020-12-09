# Day 9
# Part 2
with open('9/input9', 'r') as f:
    numbers = f.read().splitlines()
numbers = [int(i) for i in numbers]

number_to_find = 70639851

for i in range(len(numbers)):
    sum_num = 0
    idx = i
    while sum_num <= number_to_find:
        sum_num += numbers[idx]
        if sum_num == number_to_find and not i == idx:
            sub_arr = numbers[i:idx+1]
            print(max(sub_arr) + min(sub_arr))
            break
        idx += 1
