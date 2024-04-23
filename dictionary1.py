#The data is stored as key-value pairs using a Python dictionary.
'''This data structure is mutable
The components of dictionary were made using keys and values.
Keys must only have one component.
Values can be of any type, including integer, list, and tuple.'''

Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}        
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)

# Creating an empty Dictionary       
Dict = {}       
print("Empty Dictionary: ")       
print(Dict)       
      
# Creating a Dictionary       
# with dict() method       
Dict = dict({1: 'Mango', 2: 'Apple', 3:'Banana'})       
print("\nCreate Dictionary by using  dict(): ")       
print(Dict)       
      
# Creating a Dictionary       
# with each item as a Pair       
Dict = dict([(4, 'Nagaraj'), (2, 'Shetty')])       
print("\nDictionary with each item as a pair: ")       
print(Dict)


Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}      
print(type(Employee))      
print("printing Employee data .... ")      
print("Name : %s" %Employee["Name"])      
print("Age : %d" %Employee["Age"])      
print("Salary : %d" %Employee["salary"])      
print("Company : %s" %Employee["Company"])


# Creating an empty Dictionary       
Dict = {}       
print("Empty Dictionary: ")       
print(Dict)       
        
# Adding elements to dictionary one at a time       
Dict[0] = 'Kannan'      
Dict[2] = 'Joseph'      
Dict[3] = 'Mohammed'      
print("\nDictionary after adding 3 elements: ")       
print(Dict)       
        
# Adding set of values        
# with a single Key       
# The Emp_ages doesn't exist to dictionary      
Dict['Emp_ages'] = 20, 33, 24      
print("\nDictionary after adding 3 elements: ")       
print(Dict)       
  
# Updating existing Key's Value       
Dict[3] = 'Welcome to BITM'      
print("\nUpdated key value: ")       
print(Dict)



Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}         
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)        
print("Enter the details of the new employee....");        
Employee["Name"] = input("Name: ");        
Employee["Age"] = int(input("Age: "));        
Employee["salary"] = int(input("Salary: "));        
Employee["Company"] = input("Company:");        
print("printing the new data");        
print(Employee)


Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)        
print("Deleting some of the employee data")         
del Employee["Name"]        
del Employee["Company"]        
print("printing the modified information ")        
print(Employee)        
print("Deleting the dictionary: Employee");        
del Employee        
print("Lets try to print it again ");        
print(Employee)


# Creating a Dictionary       
Dict1 = {1: 'EZTS', 2: 'In-plant Training', 3: 'College'}       
# Deleting a key        
# using pop() method       
pop_key = Dict1.pop(2)       
print(Dict1)

# for loop to print all the keys of a dictionary    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}        
for x in Employee:        
    print(x)
    

#for loop to print all the values of the dictionary    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}
for x in Employee:        
    print(Employee[x])

#for loop to print the values of the dictionary by using values() method.    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}     
for x in Employee.values():        
    print(x)
    
#for loop to print the items of the dictionary by using items() method    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}
for x in Employee.items():        
    print(x)
    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}  
len(dict)

dict = {7: "Chennai", 5: "Vijayawada", 8: "Ballari", 1: "Banglore"}
sorted(dict)

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}   
# clear() method    
dict.clear()    
print(dict)

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}    
# copy() method    
dict_demo = dict.copy()    
print(dict_demo)

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# pop() method    
dict_demo = dict.copy()    
x = dict_demo.pop(1)    
print(x)

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# keys() method    
print(dict_demo.keys())

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# items() method    
print(dict_demo.items())

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# get() method    
print(dict_demo.get(3))

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# values() method    
print(dict_demo.values())

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# update() method    
dict_demo.update({3: "TCS"})    
print(dict_demo)   
 

