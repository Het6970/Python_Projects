#Vehicle Management System
vehicles=[]

def add_vehicle():
    name = input("Enter Vehicle Name = ")
    number = int(input("Enter Number of vehicle = "))
    vehicle = {"Name": name , "Number":number}
    vehicles.append(vehicle)
    print("Vehicle Added Successfully !!")

def delete_vehicle():
    name = input("Enter the name of Vehicle you want to delete = ")
    for i in vehicles:
        if i["name"] == name:
            vehicles.remove(i)
            print("Vehicle Deleted successfully !!")
            return
    print("Vehicle Not found !")

def update_vehicle():
    name = input("Enter the name of Vehicle you want to update = ")
    for i in vehicles:
        if i["name"]==name:
            i["name"]=input("Enter New Vehicle Name = ")
            i["number"]=input("Enter New Vehicle Number = ")
            print("Vehicle Updated Successfully !")
            return
    print("Vehicle Not found !!")
    
def search_vehicle():
    name=input("Enter vehicle name you want to search = ")
    for i in vehicles:
        if i["name"] == name:
            print("Vehicle Found = ",name)
            return
    print("Vehicle not found !!")

def display_vehicle():
    if not vehicles:
        print("No vehicle available.")
    else:
        print("\nAll Vehicles : ")
        for i in vehicles:
            print(i)

while True:
        print("\n=== Vehicle Mangement System ===")
        print("1.Add vehicle")
        print("2.Delete vehicle")
        print("3.Update vehicle")
        print("4.Search vehicle")
        print("5.Display all vehicle")
        print("6.Exit")
        choice=int(input("Enter the choice [1-6] = "))

        if choice == 1:
            add_vehicle()
        elif choice == 2:
            delete_vehicle()
        elif choice == 3:
            update_vehicle()
        elif choice == 4:
            search_vehicle()
        elif choice == 5:
            display_vehicle()
        elif choice == 6:
            print("Exiting From System, GoodBye !")
            break
        else:
            print("Invalid choice.")

