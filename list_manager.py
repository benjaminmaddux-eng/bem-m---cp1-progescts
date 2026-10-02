#benjamin maddux ms larose cs1
# FL class Shopping List Manager
lis=["egg", "milk"]
while True:
    action = input("What would you like to do? (add, remove, view, exit):")
    if action == "add":
        chose=input("enter what you want to add: ")
        lis.append(chose)
    elif action == "remove":
        chose2=input("enter what you want to remove: ")
        lis.remove(chose2)
    elif action == "view":
        print("this is your list");print(*lis)
    elif action == "exit":
        print("thanks for shopping")
        break