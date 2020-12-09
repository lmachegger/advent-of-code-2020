# Day 9
# Part 1
with open('9/input9', 'r') as f:
    numbers = f.read().splitlines()
numbers = [int(i) for i in numbers]


def find_pair(arr, num):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == num:
                return True
    return False


for i in range(25, len(numbers)):
    sub_arr = numbers[i-25:i]

    if not find_pair(sub_arr, numbers[i]):
        print(numbers[i])
        break
