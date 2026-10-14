# benjamin maddux computer programing ms larose
code="6867"
while True:
    clue1=input("what didgit would you like to get a clue about[1,2,4] or you can try to code[try]: ")
    if clue1 == "1":
        print("sqrt(36)")
    if clue1 == "2":
        print("didgets 2 and 3 equals 21.5 * 4 ")
    if clue1 == "4":
        print("the last didget is the sqrt of 49")
    if clue1 == "try":
        tryed=input("whats your guses for the password: ")
        if tryed == "6867":
            print(" you have escaped good job!")
            break
        else:
            print("nice try, you should try agin")