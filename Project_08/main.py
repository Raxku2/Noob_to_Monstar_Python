from csv import writer,reader

def add_Contact(nam,bari,number):
    data = [
        [nam,number,bari]
    ]

    # open a csv file in write mode 
    with open("data.csv", 'a') as csvFile:
        writerObj = writer(csvFile)
        writerObj.writerows(data)

def read_Contact():
    dataSet = []
    with open("data.csv", 'r') as csvFile:
        rederObj = reader(csvFile)
        for data in rederObj:
            dataSet.append(data)
            # print(data)
    
    return dataSet

all_contacts = read_Contact()
print(f"{"Sl.":<4}. {'Name':<30} | {'Phone':<20} | City")
print(f"-----------------------------------------------------------------")
for i,contact in enumerate(all_contacts):
    print(f"{i+1:<4}. {contact[0]:<30} | {contact[1]:<20} | {contact[2]}")



userChoice = input("Enter 'Q' for Quit, 'a' for add new contacts, 'd' for delete: ")

if userChoice == 'Q':
    exit()


elif userChoice.lower() == 'a':
    nam = input("Enter Contact er nam: ")
    number = input("Number ??: ")
    address = input("Bari kothay ?? :")

    add_Contact(bari=address, nam=nam, number=number)
    all_contacts = read_Contact()
    print(f"{'Name':<30} | {'Phone':<20} | City")
    print(f"-----------------------------------------------------------------")
    for contact in all_contacts:
        print(f"{contact[0]:<30} | {contact[1]:<20} | {contact[2]}")


elif userChoice.lower() == 'd':
    beforeDelete = read_Contact()
    deleteIndex = int(input("Delete Sl no: "))-1

    print(f"{beforeDelete[deleteIndex][0]:<30} | {beforeDelete[deleteIndex][1]:<20} | {beforeDelete[deleteIndex][2]}| Deleting...\n")

    del beforeDelete[deleteIndex]
    aterDelete = beforeDelete.copy()
    
    with open("data.csv", 'w') as csvFile:
        writerObj = writer(csvFile)
        writerObj.writerows(aterDelete)
        print("Done..\n")


else:
    print("Invalid input!!")