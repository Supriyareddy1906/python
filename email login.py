email="supriyareddy4edu@gmail.com"
pwd=123456789
uemail=str(input("enter email"))
upwd=int(input("enter pwd"))
if(email == uemail):
    if(pwd == upwd):
        print("login success")
    else:
            print("login failed due to incorrect pwd")
else:
                print("login failed due to incorrect email")
