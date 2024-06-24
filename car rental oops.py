class rental:

    def __init__ (self, itemlist,name):
        self.itemlist = itemlist
        self.name = name
        self.lendDict = {} 

    def displayitem(self):
        print(f"We have following cars in our garage: {self.name}")
        for item in self.itemlist:
            print(item)

    def lenditem(self, user, item):
        if item not in self.lendDict.keys():
            self.lendDict.update({item:user})
            print("database has been updated. You can take the vehicle now")
        else:
            print(f"vehicle is already being used by {self.lendDict[item]}")
    
    def additem(self,item):
        self.itemlist.append(item)
        print("vehicle has been added to garage")

    def returnitem(self,item):
        self.lendDict.pop(item)

class car(rental):
    def __init__(self,car_list,name):
        super().__init__(car_list,name)

class bike(rental):
    def __init__(bike,bike_list,name):
        super().__init__(bike_list,name)     


if __name__ == '__main__':
    car_rental = car(['Maruti Suzuki Alto', 'Swift', 'Ford Figo'],"CARS IN GARAGE")
    bike_rental = bike(['Honda Activa','TVS Jupyter','Honda Aviator'], "BIKES IN GARAGE")

    while(True):
        print("--------Welcome to the Vehicle rental management system---------")
        print("1. Rent a car")
        print("2. Rent a bike")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3) :  ")

        if choice == '1':
            while True:
                 print("1. Display cars parked in garage ")
                 print("2. Renting out a car")
                 print("3. Add a new car to garage")
                 print("4. Return a car ")
                 print("5. Return to Main menu ")

                 car_choice = (input("Enter operation (1,2,3,4) : "))
       
                 if car_choice == '1':
                    car_rental.displayitem()

                 elif car_choice == '2':
                    car = input("Enter the name of the car you want to lend: ")
                    user = input("Enter your name: ")
                    car_rental.lenditem(user,car)

                 elif car_choice == '3':
                    car = (input("Enter name of cars you want to add: "))
                    car_rental.additem(car)

                 elif car_choice == '4':
                    car = (input(" Enter name of car to be returned: "))
                    car_rental.returnitem(car)

                 elif car_choice == '5':
                    print("Returning to Main menu.")
                    break
                 
                 else:
                    print("Invalid choice.  Try again")

        elif choice == '2':
            while True:
                 print("1. Display bikes parked in garage ")
                 print("2. Renting out a bike")
                 print("3. Add a new bike to garage")
                 print("4. Return a bike ")
                 print("5. Return to Main menu ")

                 bike_choice = input("Enter operation (1,2,3,4) : ")
       
                 if bike_choice == '1':
                    bike_rental.displayitem()

                 elif bike_choice == '2':
                    bike = input("Enter the name of the bike you want to lend: ")
                    user = input("Enter your name")
                    bike_rental.lenditem(user,bike)

                 elif bike_choice == '3':
                    bike = (input("Enter name of bike you want to add: "))
                    bike_rental.additem(bike)

                 elif bike_choice == '4':
                    bike = (input(" Enter name of bike to be returned: "))
                    bike_rental.returnitem(bike)

                 elif bike_choice == '5':
                    print("Returning to Main menu.")
                    break
                 
                 else:
                    print("Invalid choice.  Try again")           

        elif choice == '3':
            print("Exiting")
            break
         
        else:
            print(" invalid")

        