email="supriyareddy4edu@gmail.com"
pwd=92312864
otp=89634
uemail=str(input("enter the email"))
upwd=int(input("enter the pwd"))
if(email==uemail):
    if(pwd==upwd):
        uotp=int(input("enter the otp"))
        if(otp==uotp):
            print("otp crt")
        else:
            print("otp wrng")
            
        print("login success")
    else:
        print("login unsuccessful due to incorrect password")
else:
    print("login failed due to incorrect email")
