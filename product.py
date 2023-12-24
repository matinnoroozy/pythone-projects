names = []
prices = []
while True:
    x = input("Add ,Remove ,Edit ,Search ,Display ,Exit: ").lower()
    if x == "add":
        name1 = input("name: ")
        if name1 not in names:
            names.append(name1)
            prc1 = int(input("price: "))
            prices.append(prc1)
            print("added!")
        else:
            print("exist!")
    elif x == "remove":
        if names == []:
            print("we dont have anything to remove!")
        else:
            name1 = input("name for del: ")
            if name1 in names:
                i = names.index(name1)
                del names[i]
                del prices[i]
                print("Removed!")
            else:
                print("not exist!")
    elif x == "edit":
        if names == []:
            print("we dont have anything to edit!")
        else:
            name1 = input("name for edit: ")
            if name1 in names:
                i = names.index(name1)
                n_p = int(input("new price: "))
                prices[i] = n_p
                print("edited!")
            else:
                print("not exist!")    
    elif x == "search":
        if names == []:
            print("not exist!")
        else:
            name1 = input("name for search: ")
            if name1 in names:
                i = names.index(name1)
                print(f"num:{i + 1} --> price:{prices[i]}")
            else:
                print("not exist!")  
    elif x == "display":
        if names == []:
            print("empty!")
        for i,n in enumerate(names):
            print(f"{i +1}(name:{n} --> price:{prices[i]})")
    elif x == "exit":
        print("bye(:")
        break
    else:
        print("not found!")
        print("try again!")