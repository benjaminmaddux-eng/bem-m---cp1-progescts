#benjamin maddux user sing in for computer programing 
print("Please log in")
name=input("username: ")
while True:
    password=input("exactly 9 didget password: ")

    if len(password) !=9:
        print("password to short or to long")
        continue   
    
    print("your password is now "+password)
    break
print("please confirm your password and username")

good_username=name
while True:
    user_try2=input("check your username:")

    if user_try2 == good_username:
        print("good job")
        break
    else:
        print("try again")
good_pasword=password
while True:
    user_try=input("check your password:")

    if user_try == good_pasword:
        print("good job")
        break
    else:
        print("try again")
print(" you have suceffuly logged in good job!")