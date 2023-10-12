try:
    readorwrite = input("Would you like to (r)ead or (w)override a line or (a)dd")

    if(readorwrite == "w"):

        fileagain = open("Market.txt","r")
        overridename = input("Who would you like to override:")
        linename = fileagain.readline().rstrip('\n')
        while (overridename != linename):
            if(linename == " "):
                print("Couldn't find name")
            if (overridename == linename.split()[0]):
                file = open("Market.txt", "w")
                name = input("Name:")
                itemNumber = int(input("How much did they buy?:"))
                price = int(input("what is price per item?:"))
                linename.replace(linename, name + " " + str(itemNumber) + " " + str(price) + ('\n'))
                file.close()
                print("Prices rose by: " + str((price * itemNumber) * 0.2))
            linename = fileagain.readline().rstrip('\n')
        fileagain.close()
    if(readorwrite == "r"):
        file = open("Market.txt", "r")
        name = file.readline().rstrip('\n')
        while(name != ""):
            print(name)
            name = file.readline().rstrip('\n')
        file.close()
    if(readorwrite == "a"):
        file = open("Market.txt", "a")
        name = input("Name:")
        itemNumber = int(input("How much did they buy?:"))
        price = int(input("what is price per item?:"))
        file.write(name + " " + str(itemNumber) + " " + str(price) + ('\n'))
        file.close()
        print("Prices rose by: " + str((price * itemNumber) * 0.2))

except FileNotFoundError:
    print("Error")

