#From the minds of Katie & Dyonne :)

import time 
from time import sleep    
from datetime import datetime 

current_ticket = {}
class Parking_Garage():
    """
    Your parking gargage class should have the following methods:
- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1
- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)


You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

    """
    

    def __init__(self, spaces_available = 100):  
        self.tickets = [1,101] 
        self.spaces = [1,101]
        self.spaces_available = spaces_available

    def takeTicket(self):
        if self.spaces_available <= 0:
            print("Sorry our garage is full, please visit another location!")
        elif self.spaces_available > 0:
            ticket = int(input("Please pick your parking space (Enter a number 1-100)! "))
            if ticket in current_ticket:
                print("Sorry that spot is taken!")
            elif ticket not in current_ticket:
                current_ticket[ticket] = {}
                self.spaces.append(ticket)
                driver_lp = input("Please enter your license plate number: ")
                current_ticket[ticket]["license plate"] = driver_lp
                current_ticket[ticket]["Paid"] = False
                print("Please take your ticket below!")
                self.spaces_available -= 1
                print(f"Please park your car. There are now {self.spaces_available} spaces available")
            
    def show_used_spaces(self):
        print("These parking spaces are already in use: ")
        for i in current_ticket:
            print(current_ticket)

    def payforParking(self):
        confirm_pay = int(input("Please enter your spot number or enter '0' if you lost your ticket: "))
        if confirm_pay == 0:
            sleep(1)
            print(".....")
            print("Sorry you lost your ticket. Unfortunately you now have to pay $100.")
            print(".....")
        elif current_ticket[confirm_pay]["Paid"] == True:
            print("Payment Succesful! You have 15 minutes to exit the garage!")
            self.leaveGarage()
        elif current_ticket[confirm_pay]["Paid"] == False:
            print("Your fee is $40. Please enter your payment, we do not give change!")  
            final_pay = int(input("Please enter payment information below "))
            if final_pay >= 40:
                print("Payment Successful!")
                current_ticket[confirm_pay]["Paid"] = True
            else:
                print("Correct dollar amount was not entered. Try again.")
        else:
            print("Not a valid entry. Try again!")
            
    def leaveGarage(self):
        confirm = int(input("Please enter your ticket to confirm payment: "))
        if current_ticket[confirm]["Paid"] == True:
            print("You may now exit the garage. Have a nice day!")
            del current_ticket[confirm]
            self.spaces_available += 1
        elif current_ticket[confirm]["Paid"] == False:
            print("Please enter your payment, we do not give change!") 
            self.spaces_available += 1   
        else:
            print("Not a valid entry. Try again!")

garage = Parking_Garage()

while True:
    welcome = input("Welcome to the parking garage. Enter 'P' to proceed to parking, 'S' to see what parking spaces are being used, 'L' to leave, 'Q' to quit: ")
    if welcome.lower() == "p":
        garage.takeTicket()
    elif welcome.lower() == "l":
        garage.payforParking()
        garage.leaveGarage()
    elif welcome.lower() == "s":
        garage.show_used_spaces()
    elif welcome.lower() == "q":
        print("Have a nice day, Goodbye!")
        break 
    else:
        print("Invalid input, please try again.")

#Our garage is bad@$$!