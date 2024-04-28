# Nested list comprehension 
matrix = [[j for j in range(5)] for i in range(3)] 

print(matrix) 

integer_input = list(map(int, input("Enter integers separated by space: ").split()))
float_input = list(map(float, input("Enter floats separated by space: ").split()))
string_input = list(input("Enter strings separated by space: ").split())

print("Integer input:", integer_input)
print("Float input:", float_input)
print("String input:", string_input)


# Storing multiple data types in the same variable using a list
data = list(map(int, input("Enter integers separated by space: ").split()))
data.extend(list(map(float, input("Enter floats separated by space: ").split())))
data.extend(input("Enter strings separated by space: ").split())

print("Data:", data)
