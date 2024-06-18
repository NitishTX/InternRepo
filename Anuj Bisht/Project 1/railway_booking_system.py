import pandas as pd


class TrainInformation:
    def __init__(self, source: str, final: str):
        self.source = source
        self.final = final

    def train_list(self):
        # dictionary contains sample of trains
        data = {
            "Train": ["Amritsar Express", "Jammu Tawi Express", "Amritsar Intercity Express",
                      "Kalka Shatabdi Express", "Mumbai LTT Express", "Tirunelveli SF Express"],
            "Time of Departure": ["02:38", "03:13", "06:35", "07:40", "10:25", "01:50"],
            "Time of Arrival": ["08:20", "08:00", "11:30", "10:59", "13:55", "14:00"],
            "Departure Point": ["Chandigarh", "Chandigarh", "Chandigarh", "New Delhi", "Erode", "Vishakhapatnam"],
            "Arrival Point": ["Amritsar", "Amritsar", "Amritsar", "Chandigarh", "Mumbai", "Perambur"],
            "Seats Left": [100, 82, 77, 86, 73, 105]
        }

        # filtered dictionary contains the train of the user's route only
        filtered_data = {
            key: [value for value, dep, arr in zip(values, data["Departure Point"], data["Arrival Point"])
                  if dep == self.source and arr == self.final]
            for key, values in data.items()
        }

        return pd.DataFrame(filtered_data)


class RailwayBookingSystem(TrainInformation):
    def __init__(self, date: int, month: int, year: int, source_destination: str, final_destination: str,
                 num_passengers: int):
        super().__init__(source=source_destination, final=final_destination)
        self.date = date
        self.month = month
        self.year = year
        self.num_passengers = num_passengers

    # function to book the train
    def book_train(self):
        dataset = self.train_list()
        print(f"List of Trains from {self.source} to {self.final}:")
        print(dataset)

        # Select the train from the options
        select_train = input("Enter the name of the train you want to select: ")

        # find the row of the selected train in the dataset
        row_number = dataset[dataset['Train'] == select_train].index[0]
        # print(row_number)

        # Check whether the selected train has available seats
        if self.num_passengers <= dataset.at[row_number, 'Seats Left']:
            # Update the allocated seats in the dataset
            dataset.at[row_number, 'Seats Left'] -= self.num_passengers

            # create a dictionary that contains the data of the passengers
            passenger_details = {
                "Name": [],
                "Age": []
            }
            for i in range(self.num_passengers):
                name = input(f"Enter the name of the Passenger {i + 1}: ")
                age = int(input(f"Enter the age of Passenger {i + 1}: "))
                passenger_details["Name"].append(name)
                passenger_details["Age"].append(age)

            # convert the dictionary into the dataframe
            passenger_details = pd.DataFrame(passenger_details)
            print("Train Booking Confirmed!!")

            # print the train details
            print("Your Train Details:")
            print(dataset.loc[row_number])

            # print the passenger details
            print("Passenger Details:")
            for i in range(self.num_passengers):
                print(passenger_details.loc[i])

            print("Happy Journey!!")
        else:
            print("Select another train!!")

    # # function to print the ticket of journey
    # def print_ticket(self):
    #     print("!!   Ticket   !!")
    #     print(f"Departure Point: {self.source}")
    #     print(f"Arrival Point: {self.final}")
    #     print(f"Departure Date: {self.date}-{self.month}-{self.year}")


if __name__ == '__main__':
    print("!!   Welcome to Railway Booking System    !!")
    date, month, year = input("Enter the date of travel (DD-MM-YYYY): ").split("-")
    final_destination = input("Enter the final destination: ")
    source_destination = input("Enter the source destination: ")
    number_of_passengers = int(input("Enter number of passengers: "))

    # create the object of RailwayBookingSystem class
    rms = RailwayBookingSystem(date, month, year, source_destination, final_destination, number_of_passengers)

    print("Press 1: Book a Train")
    # print("Press 2: Print Ticket")
    print("Press 2: Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            rms.book_train()
        # case 2:
        #     rms.print_ticket()
        case 2:
            print("Thanks for using our services")
        case _:
            print("Enter right choice!!")
            
