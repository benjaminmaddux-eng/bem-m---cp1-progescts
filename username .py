#username thingy

print("username maker")
name=input("nickname: ")
while True:
    try:
        favnum1=int(input("number:"))
    except:
        print("try again")
    else:
        break
while True:
    try:
        favnum2=int(input("number:"))
    except:
        print("try again")
    else:
        break
power=int(favnum1*favnum2)
print(name,power)
while True:
    password=input("9 didget password: ")

    if len(password) !=9:
        print("password to short")
        continue   
    
    print("your password is now "+password)
    break
print("please confirm your password and username")
good_pasword=password
while True:
    user_try=input("check your password:")

    if user_try == good_pasword:
        print("good job")
        break
    else:
        print("try again")
print("comleated user name and pasword")
print(name,power)
print(password)