# DAY2
contacts = []


def Home():
    name = input("Enter Name:")
    number = input("Enter number :")
    contacts.append(name)
    contacts.append(number)
    print(contacts)
    def save_contact():
        with open("contacts.txt","w") as file:
            name, number = contacts
            file.write("|")
            file.write(name+" ")
            file.write(number)
            file.write("\n")    
    save_contact()

def read_contact():
    with open("contacts.txt","r") as file:
        contacts = file.read()
        print(contacts)

print("Contact Systems")
print("\n 01. Add \n 02. Read  \n 03. Exit")
opt = input("Select the option: ")

if opt == '1':
    Home()
elif opt == '2':
    read_contact()
else:
    print("Please select valid option")


