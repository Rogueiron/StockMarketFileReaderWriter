try:
    readorwrite = input("Would you like to (r)ead or (w)sell or (a)buy: ")
    percentIncrease = 0.02
    if(readorwrite == "w"):
        file = open("Market.txt", "r")
        lines = file.readlines()
        print(lines)
        file.close()
        file = open("Market.txt", "w")
        lineToChange = int(input("Which line would you like to change: "))
        name = input("Name:")
        itemNumber = int(input("How much did they buy?:"))
        price = int(input("what is price per item?:"))
        lines[lineToChange - 1] = (name + " " + str(itemNumber) + " " + str(price))
        file.writelines(lines)
        file.close()
        print("Prices rose by: " + str((price * itemNumber) * percentIncrease))
    if(readorwrite == "r"):
        file = open("Market.txt", "r")
        name = file.readline().rstrip('\n')
        while(name != ""):
            print(name)
            name = file.readline().rstrip('\n')
        file.close()
    if(readorwrite == "a"):
        file = open("Market.txt", "a+")
        empty = file.readline().rstrip('\n')
        if(empty == ""):
            name = input("Name:")
            itemNumber = int(input("How much did they buy?:"))
            price = int(input("what is price per item?:"))
            file.write(name + " " + str(itemNumber) + " " + str(price) + ('\n'))
            file.close()
            print("Prices rose by: " + str((price * itemNumber) * percentIncrease))

except FileNotFoundError:
    print("Error")

