try:
    filename = input("What File would you like to open:")
    readorwrite = input("Would you like to (r)ead or (w)rite:")
    file = open(filename,readorwrite)
    if(readorwrite == "w"):
        file.write(input("Name:") + " " + input("How much did they buy?:") + " "+ input("at what price?:"))
    if(readorwrite == "r"):
        while(file.readline().rstrip('\n') != ""):
            name = file.readline().rstrip('\n')
            print(name)

except FileNotFoundError:
    print("Error")
