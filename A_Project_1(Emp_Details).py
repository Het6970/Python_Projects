#APP MANAGEMENT SYSTEM
'''
1.ADD
2.DELETE
3.UPDATE
4.SEARCH
5.DISPLAY
'''
d1={}
def add_emp():
    srno=int(input("Enter the sr no="))
    name=input("Enter the Name =")
    salary=int(input("enter the salary = "))
    d1[srno]=[name,salary]
    print("Emp added sucessfully !!")

def delete_emp():
    srno=int(input("Enter the serial number u want to delete = "))
    if srno in d1:
        del d1[srno]
        print("Emp deleted Sucessfully!!")
    else:
        print("emp not found.")
    

def update_emp():
    srno=int(input("Enter the sr no u want to update ="))
    if srno in d1:
        name=input("Enter the name = ")
        salary=int(input("Enter the salary ="))
        d1[srno]=[name,salary]
        print("emp updated successfully")
    else:
        print("emp not found.")

def search_emp():
    srno=int(input("Enter the srno you want to search ="))
    if srno in d1:
        print("Employee Found:",d1[srno])
    else:
        print("srno not found!")

def display_emp():
    for i in d1:
        print("SrNo-->",i)
        print("Name-->",d1[i][0])
        print("salary-->",d1[i][1],"\n")


while True:
    print("\n===Employee Management System===")
    print("1. Add Employee ")
    print("2. Delete Employee ")
    print("3. Update Employee ")
    print("4. Search Employee ")
    print("5. Display Employee ")
    print("6. Exit")

    choice = int(input("Enter your choice = "))
    if choice == 1:
        add_emp()
    elif choice == 2:
        delete_emp()
    elif choice == 3:
        update_emp()
    elif choice == 4:
        search_emp()
    elif choice == 5:
        display_emp()
    elif choice == 6:
        print("Exiting Program... GoodBye!")
        break
    else:
        print("Invalid Choice ! Please Try Again !")


