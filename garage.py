class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        pass  # Initialize Car properties

class Spot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        pass  # Initialize Spot properties

    def park_car(self, car):
        self.car = car
        pass  # Logic to park a car in the spot

    def remove_car(self):                                                   #dont touch this yet. 
        pass  # Logic to remove a car from the spot

class Ticket:
    def __init__(self, car, spot):
        self.car = car
        self.spot = spot
        pass  # Initialize Ticket properties

class Garage:
    def __init__(self, tickets = [10], parking_spaces = [10]):
        self.tickets = tickets 
        self.parking_spaces = parking_spaces
        #self.capacity = capacity
        pass  # Initialize Garage properties
        #test

    def take_Ticket(self):        
        while True:
            user_inp = input('Are you parking with us today? Type Y for yes, N for no ').upper()
            if user_inp == 'Y': 
                tickets = self.tickets - 1
                spaces = self.parking_spaces - 1
                print(f'Thanks for parking with us! {tickets} out {self.tickets} tickets remaining! {spaces} out of {self.parking_spaces} spaces remaining!')
                break
            elif user_inp == 'N':
                print('Please Leave now!')
                break
            else:
                print('Please input Y for yes, N for no to continue!')

            
    def pay_4_parking(self):
        amount_paid = input("What is the amount you'd like to pay? It's 5 to pay for parking.")
        #if amount_paid == 5
        pass

    def leave_garage(self):
        self.leave_garage = leave_garage
        if pay_4_parking == True:
            print('Thank you! Have a nice day!!')
        else: 
            please_pay = input('Please pay the amount before leaving!')

    def park_car(self, car):
        pass  # Logic to park a car in the garage

    def retrieve_car(self, ticket):
        pass  # Logic to retrieve a car from the garage

def main():
    pass  # Runner code to interact with the parking lot system

parking = Garage()
parking.take_Ticket()

if __name__ == "__main__":
    main()