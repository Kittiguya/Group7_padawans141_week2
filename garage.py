# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary
    
class Garage:
    def __init__(self, tickets = 10, parking_spaces = 10):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}
        

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
        
    def take_ticket(self):        
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

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True  
                        
    def pay_4_parking(self):
        paid = input("Enter '5' to pay for parking. ")
        if paid == '5':
            print("Thank you for your payment. You have 15 minutes to park.")
            self.current_ticket[paid] = True
            print(self.current_ticket)
        else:
            print("Please pay to park or leave.")

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)
            
    def leave_garage(self):
            tickets = self.tickets + 1
            spaces = self.parking_spaces + 1
            print(f"Upon exit, the garage now has {self.tickets} tickets and {self.parking_spaces} spaces.")
            print("Thank you for parking. Have a nice day!") 


    def run_garage(self):
        self.take_ticket()
        self.pay_4_parking()
        


parking = Garage()
parking.run_garage()
parking.leave_garage()

