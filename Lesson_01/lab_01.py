student_list = [
    {"name": "Bob",  "phone": "0631234567", "age": "19", "email": "bob@university.com"},
    {"name": "Emma", "phone": "0631234567", "age": "20", "email": "emma@university.com"},
    {"name": "Jon",  "phone": "0631234567", "age": "21", "email": "jon@university.com"},
    {"name": "Zak",  "phone": "0631234567", "age": "19", "email": "zak@university.com"}
]

def printAllList():
    print("\n--- СТАТУС ДОВІДНИКА ---")
    for elem in student_list:
        strForPrint = (f"Name: {elem['name']} | Phone: {elem['phone']} | "
                       f"Age: {elem['age']} | Email: {elem['email']}")
        print(strForPrint)
    print("------------------------\n")
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    email = input("Please enter student email: ")
    
    newItem = {"name": name, "phone": phone, "age": age, "email": email}
    
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
            
    student_list.insert(insertPosition, newItem)
    print("New element has been added.\n")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
            
    if deletePosition == -1:
        print("Element was not found.\n")
    else:
        print(f"Delete position {deletePosition}")
        del student_list[deletePosition]
        print("Element has been deleted.\n")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    
    for item in student_list:
        if name == item["name"]:
            updatePosition = student_list.index(item)
            break
            
    if updatePosition == -1:
        print("Element was not found.\n")
    else:
        print("Student found. Please enter new details.")
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone: ")
        new_age = input("Enter new age: ")
        new_email = input("Enter new email: ")
        
        updatedItem = {"name": new_name, "phone": new_phone, "age": new_age, "email": new_email}
        
        del student_list[updatePosition]
        
        insertPosition = 0
        for item in student_list:
            if new_name > item["name"]:
                insertPosition += 1
            else:
                break
                
        student_list.insert(insertPosition, updatedItem)
        print("Element has been updated successfully.\n")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed:")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice\n")

main()