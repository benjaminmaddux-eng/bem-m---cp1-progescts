#benjamin maddux ms larose cs1
# FL class Shopping List Manager
lis=["egg", "milk"]
while True:
    action = input("What would you like to do? (add, remove, view, exit):")
    if action == "add":
        chose=input("enter what you want to add( egg or milk )")
        if chose == "egg":
            lis.append("egg")
        if chose == "milk":
            lis.append("milk")
    elif action == "remove":
        chose2=input("enter what you want to remove ( egg or milk )")
        if chose2=="egg":
            lis.remove("egg")
        if chose2=="milk":
            lis.remove("milk")
    elif action == "view":
        print("this is your list");print(*lis)
    elif action == "exit":
        print("thanks for shopping")
        break