# datatypes.py

# Creating variables of different data types
integer_variable = 23768                     # int
float_variable = 556.8                     # float
complex_variable = 3 + 6j                  # complex
list_variable = [1, 2, 3,5]            # list
tuple_variable = (1, 2, 3)           # tuple
dict_variable = {'key1': 'value1',}  # dict
set_variable = {1, 2, 3, 4, 5}             # set
bool_variable = True                        # bool

# Printing the type of each variable
print("Type of integer_var:", type(integer_variable))
print("Type of float_var:", type(float_variable))
print("Type of complex_var:", type(complex_variable))
print("Type of list_var:", type(list_variable))
print("Type of tuple_var:", type(tuple_variable))
print("Type of dict_var:", type(dict_variable))
print("Type of set_var:", type(set_variable))
print("Type of bool_var:", type(bool_variable))

# Converting integer to float and vice versa
converted_float = float(integer_variable)
converted_integer = int(float_variable)

# Printing the results of conversions
print("Converted integer to float:", converted_float)
print("Converted float to integer:", converted_integer)