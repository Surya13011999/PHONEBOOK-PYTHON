def Addcontact():
    name=input("enter a name:")
    number=int(input("enter a number:"))
    person= {
        "name"  : name.lower(),
        "number":number
        }
    phonebook[name.lower()]=person
def viewContact():
        search_person=input("enter a person to search:")
        if search_person in phonebook.keys():
            print("person name:" ,phonebook[search_person]['name'])
            print("person number:" ,phonebook[search_person]['number'])
def view_all():
       print(phonebook.values)
def EditNumber():
        n=input("enter a name")
        if n in phonebook .keys():
            changed_num=int(input("enter a number:"))
            phonebook[n]['number']=changed_num
        else:
            print("not found")
def Edituser():
        person_name=input("enter a name").lower()
        if person_name in phonebook.keys():
            changed_name=input("enter a New name:").lower()
            phonebook[person_name]['name']=changed_name.lower()
            poped_person = phonebook.pop(person_name)
            phonebook[changed_name] = poped_person
        else:
            print("not found")
def delete():
    delete_person=input("enter a person to delete:").lower()
    if delete_person in phonebook.keys():
            del phonebook[delete_person]

phonebook={}
while True:
            print ('''
1-> Add a person to phonebook
2-> View Single person
3-> View All person
4-> change a person phone number
5-> change a person name
6-> show all users
7-> quit     
''')
            option=int(input("Enter Your Choice:"))
            if option==1:
                Addcontact()
            elif option==2:
                viewContact()
            elif option==3:
                  view_all()
            elif option==4:
                  EditNumber()
            elif option==5:
                  Edituser()
            elif option==6:
                  delete()
            elif option==7:
                  break
