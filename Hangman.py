
from random import *

names = ['alborz','ardebil','bushehr','azarbaijan','esfahan','fars','gilan',
        'golestan','hamadan','hormozgan','ilam','kerman','kermanshah',
        'khuzestan','kordestan','lorestan','markazi','mazandaran','khorasan',
        'qazvin','qom','semnan','sistan','tehran','yazd','zanjan']
answer = "y"
while answer == "y" :   
    n=randint(0,len(names)-1)
    name=names[n]

    charNumber=len(name)
    userList=["-"]*charNumber    
    print(userList,end="")

    wrongs=0

    while userList.count("-")>0:

        guess=input("guess a character: ")

        for i in range(charNumber):
            if guess == name[i]:
                userList[i]=guess
        if name.count(guess)==0:
            wrongs=wrongs + 1
            if wrongs == charNumber :
                print(" :( -you lose!! ")
                break
            print("no! you have" , charNumber - wrongs , "more chances")
        
            
        print(userList,end="")
    if charNumber > wrongs :
        print("\nyou win!")
    answer = input("do you want to continue? (y/n) :")          
