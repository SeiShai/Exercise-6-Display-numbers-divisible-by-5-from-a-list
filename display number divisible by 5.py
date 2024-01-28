# Iterate the given list of numbers and
# print only those numbers which are divisible by 5

# create the list
number_list = [10, 20, 33, 46, 55]

print('The given numbers are:', number_list)
print('the numbers divisible by 5 are:')

# make iteration
for numbers in number_list:
    if numbers % 5 == 0:
        print(numbers)