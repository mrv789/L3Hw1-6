def sum_of_three(num_1, num_2, num_3):
    result = num_1 * num_2 * num_3
    result.remove(min(num_1, num_2, num_3))
    return sum(result)

sum_of_three(1, 3, 8)
print(sum_of_three)