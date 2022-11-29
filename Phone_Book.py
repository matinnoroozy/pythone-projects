#******************************************************Phone book project**********************************************
names = []    # list of names
phones = []    # list of phone
#*******************************************************functions******************************************************
#function1-add cantact
def add():
	while True:
		name = input('name of cantact for add (for leave use "exit" !):')
		if name == "exit":
			break
		elif name in names:
			answer_user = input(f'you have "{name}" in your contacts, wanna add?[y/n] ')
			if answer_user.lower() == "y":
				phone = input(f'number of "{name}": ')
				phones.append(phone)
				names.append(name)
			elif answer_user.lower() == "n":
				pass
			else:
				print(f"{answer_user}: command not found!")
		else:
			phone = input(f'number of "{name}": ')
			phones.append(phone)
			names.append(name)	
#function2-showlist of contact		
def show():
	for i in range(len(names)):
		print(f"cantact_{i+1} {names[i]}:{phones[i]}")
#function3-edit contact
def edit():
	name=input("name of contact for edit:")
	if name in names:
		c=names.count(name)
		if c == 1 :
			new_name=input(f"new name of {name}:")
			new_phone=input(f"new number of {name}:")
			i=names.index(name)
			names[i]=new_name
			phones[i]=new_phone
		else:
			for i in range(len(names)):
				if names[i] == name:
					print(f"{i+1}:{phones[i]}")
			h=int(input(f'ID of "{name}" phone:')) 
			new_name=input(f"new name of {name}:")
			new_phone=input(f"new number of {name}:")		
			names[h-1]=new_name
			phones[h-1]=new_phone
	else:
		print ("not found")
#function4-dlete contact
def dl():
	name=input("name of contact for delet:")
	if name in names:
		c=names.count(name)
		if c == 1 :
			i=names.index(name)
			names.remove(name)
			phones.pop(i)
		else:
			for i in range(len(names)):
				if names[i] == name:
					print(f"{i+1}:{phones[i]}")
			h=int(input(f'ID of "{name}" phone:')) 
			names.pop(h-1)
			phones.pop(h-1)
	else:
		print ("not found")
#function5-show number of contacts
def detail():
	print (f"u have {len(names)} contact ")
#function6-search
def search():
	srch_name=input("name:")
	if srch_name in names:
		i=names.index(srch_name)
		print(f'number of "{srch_name}" is "{phones[i]}"!')
	else:
		print("not found!")
while True:
	Q=input("Add , Edit , Dlete , Search , Deatil , ShowList . exit : ")
	Q = Q.lower()
	if Q == "add":
		add()
	elif Q == "edit":
		edit()
	elif Q == "dlete":
		dl()
	elif Q == "search":
		search()
	elif Q == "deatil":
		detail()
	elif Q == "showlist":
		show()
	elif Q == "exit":
		break	
	elif Q == "":
		pass
	else:
		print(f"{Q} is not found!")
