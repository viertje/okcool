list1 = ["-", "-", "-"]
list2 = ["-", "-", "-"]
list3 = ["-", "-", "-"]

x = True

listOptions = [1,2,3,4,5,6,7,8,9]

def check_result():
        if (list1[0] == "x") and (list1[1] == "x") and (list1[2] == "x"):
            return False

        elif (list2[0] == "x") and (list2[1] == "x") and (list2[2] == "x"):
            return False

        elif (list3[0] == "x") and (list3[1] == "x") and (list3[2] == "x"):
            return False

        elif (list1[0] == "x") and (list2[0] == "x") and (list3[0] == "x"):
            return False

        elif (list1[1] == "x") and (list2[1] == "x") and (list3[1] == "x"):
            return False

        elif (list1[2] == "x") and (list2[2] == "x") and (list3[2] == "x"):
            return False

        elif (list1[0] == "x") and (list2[1] == "x") and (list3[2] == "x"):
            return False

        elif (list1[2] == "x") and (list2[1] == "x") and (list3[0] == "x"):
            return False
        else:
            return True

def check_result2():
        if (list1[0] == "o") and (list1[1] == "o") and (list1[2] == "o"):
            return False

        elif (list2[0] == "o") and (list2[1] == "o") and (list2[2] == "o"):
            return False

        elif (list3[0] == "o") and (list3[1] == "o") and (list3[2] == "o"):
            return False

        elif (list1[0] == "o") and (list2[0] == "o") and (list3[0] == "o"):
            return False

        elif (list1[1] == "o") and (list2[1] == "o") and (list3[1] == "o"):
            return False

        elif (list1[2] == "o") and (list2[2] == "o") and (list3[2] == "o"):
            return False

        elif (list1[0] == "o") and (list2[1] == "o") and (list3[2] == "o"):
            return False

        elif (list1[2] == "o") and (list2[1] == "o") and (list3[0] == "o"):
            return False
        else:
            return True

def ask_input_player_1():
    y = True
    while y == True:
        x = int(input("player 1 choose option: "))
        if x in listOptions:
            if x == 1:
                list1[0] = "x"
                listOptions.remove(x)
                y = False
            elif x == 2:
                list1[1] = "x"
                listOptions.remove(x)
                y = False
            elif x == 3:
                list1[2] = "x"
                listOptions.remove(x)
                y = False
            elif x == 4:
                list2[0] = "x"
                listOptions.remove(x)
                y = False
            elif x == 5:
                list2[1] = "x"
                listOptions.remove(x)
                y = False
            elif x == 6:
                list2[2] = "x"
                listOptions.remove(x)
                y = False
            elif x == 7:
                list3[0] = "x"
                listOptions.remove(x)
                y = False
            elif x == 8:
                list3[1] = "x"
                listOptions.remove(x)
                y = False
            elif x == 9:
                list3[2] = "x"
                listOptions.remove(x)
                y = False
        else:
            x = int(input("Try another option: "))

def ask_input_player_2():
    y = True
    while y == True:
        x = int(input("player 2 choose option: "))
        if x in listOptions:
            if x == 1:
                list1[0] = "o"
                listOptions.remove(x)
                y = False
            elif x == 2:
                list1[1] = "o"
                listOptions.remove(x)
                y = False
            elif x == 3:
                list1[2] = "o"
                listOptions.remove(x)
                y = False
            elif x == 4:
                list2[0] = "o"
                listOptions.remove(x)
                y = False
            elif x == 5:
                list2[1] = "o"
                listOptions.remove(x)
                y = False
            elif x == 6:
                list2[2] = "o"
                listOptions.remove(x)
                y = False
            elif x == 7:
                list3[0] = "o"
                listOptions.remove(x)
                y = False
            elif x == 8:
                list3[1] = "o"
                listOptions.remove(x)
                y = False
            elif x == 9:
                list3[2] = "o"
                listOptions.remove(x)
                y = False
        else:
            print("Try another option: ")

def printlists():
    print(list1)
    print(list2)
    print(list3)

while(x == True):

    printlists()

    ask_input_player_1()
    x = check_result()
    if x == False:
        printlists()
        print("player 1 won")
        break
    x = check_result2()
    if x == False:
        printlists()
        print("player 2 won")
        break

    printlists()

    ask_input_player_2()
    x = check_result()
    if x == False:
        printlists()
        print("player 1 won")
        break
    x = check_result2()
    if x == False:
        printlists()
        print("player 2 won")
        break
