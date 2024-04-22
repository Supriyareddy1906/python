num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if(num1>num2):
    print(num1,'is greater')
elif(num1==num2):
        print('both are equal')
else:
    print(num2,'is greater')
    
    
    

a=50
b=10
c=-15
print('a' if a>b and a>c else'b' if b>c else'c')


