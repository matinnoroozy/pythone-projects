#st_nums names nums
#limit1 len st_nums == 4 start with s
#limit2 st_nums are not equal 
#limit3 nums <= 10 and num >= 0
#add remove edit search display exit
def add():
    st_num = input("enter st_num: ")
    if st_num not in st_nums:
        if len(st_num) == 4 and st_num[0] == "s":
            num = int(input("enter num: "))
            if num <= 10 and num >= 0:
                name = input("enter name: ")
                st_nums.append(st_num)
                nums.append(num)
                names.append(name)
                print("added!")
            else:
                print("error num")
        else:
            print("error st_num")
    else:
        print("exist!")
def remove():
    x = input("st_num for del? ")
    if x in st_nums:
        y = st_nums.index(x)
        j = [st_nums ,names ,nums]
        for i in j:
            q = i.pop(y)
        print("removed!")
    else:
        print("not exist!")
def edit():
    x = input("st_num for edit? ")
    if x in st_nums:
        y = st_nums.index(x)
        q = input("new name? ")
        w = input("new num? ")
        #if q != "":
        names[y] = q or names[y]               
        nums[y] = int(w or nums[y])
        print("edited!")
    else:
        print("not exist!")
def search():
    x = input("st_num for search? ")
    if x in st_nums:
        y = st_nums.index(x)
        j = [st_nums ,names ,nums]
        for i in j:
            print(i[y],end = ", ")
        print()
    else:
        print("not exist!")
def display():
    for i ,v in enumerate(nums):
        print(f"count:{i + 1}-->num:{v}-->name:{names[i]}-->st_num:{st_nums[i]}")
st_nums = ["s456" ,"s451"]
names = ["jkl" ,"ghj"]
nums = [5 ,10]
while True:
    x = input("add ,remove ,edit ,search ,display ,exit?! ").lower()
    if x == "add":
        add()
    elif x == "remove":
        remove()
    elif x == "edit":
        edit()
    elif x == "search":
        search()
    elif x == "display":
        display()
    elif x == "exit":
        break
    else:
        print("error")
