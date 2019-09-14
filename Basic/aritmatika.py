value_one = input("Input Value 1 = ") # default type data from function input is String
value_two = input("Input Value 2 = ") # default type data from function input is String

print(value_one, '+', value_two, '=', (value_one + value_two))
print(value_one, '-', value_two, '=', (int(value_one) - int(value_two))) # function int() for set type data to integer
print(value_one, '*', value_two, '=', (int(value_one) * int(value_two)))
print(value_one, '/', value_two, '=', (int(value_one) / int(value_two)))
print('Akar 2 dari', value_one,'=', (int(value_one) ** 2))