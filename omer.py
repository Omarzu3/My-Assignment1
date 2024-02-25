#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Import the datetime module to handle date and time information
from datetime import datetime

class Airport:
    def __init__(self, name):
        # Initialize the Airport object with a name and an empty list of flights
        self.name = name
        self.flightList = []

    def getName(self):
        # Return the name of the airport
        return self.name

    def setName(self, name):
        # Set the name of the airport
        self.name = name

    def getFlightList(self):
        # Return the list of flights associated with the airport
        return self.flightList

    def setFlightList(self, flightList):
        # Set the list of flights associated with the airport
        self.flightList = flightList


class Passenger:
    def __init__(self, name, ticketNumber, seatNumber):
        # Initialize the Passenger object with a name, ticket number, and seat number
        self.name = name
        self.ticketNumber = ticketNumber
        self.seatNumber = seatNumber

    def getName(self):
        # Return the name of the passenger
        return self.name

    def setName(self, name):
        # Set the name of the passenger
        self.name = name

    def getTicketNumber(self):
        # Return the ticket number of the passenger
        return self.ticketNumber

    def setTicketNumber(self, ticketNumber):
        # Set the ticket number of the passenger
        self.ticketNumber = ticketNumber

    def getSeatNumber(self):
        # Return the seat number of the passenger
        return self.seatNumber

    def setSeatNumber(self, seatNumber):
        # Set the seat number of the passenger
        self.seatNumber = seatNumber
class BoardingPass:
    def __init__(self, passengerName, flightNumber, departureAirport, destinationAirport, arrivalDateTime, gate, seatNumber, electronicTicket):
        # Initialize the BoardingPass object with passenger information, flight details, and ticket information
        self.passengerName = passengerName
        self.flightNumber = flightNumber
        self.departureAirport = departureAirport
        self.destinationAirport = destinationAirport
        self.arrivalDateTime = arrivalDateTime
        self.gate = gate
        self.seatNumber = seatNumber
        self.electronicTicket = electronicTicket

    def getPassengerName(self):
        # Return the name of the passenger
        return self.passengerName

    def setPassengerName(self, passengerName):
        # Set the name of the passenger
        self.passengerName = passengerName

    def getFlightNumber(self):
        # Return the flight number
        return self.flightNumber

    def setFlightNumber(self, flightNumber):
        # Set the flight number
        self.flightNumber = flightNumber

    def getDepartureAirport(self):
        # Return the departure airport
        return self.departureAirport

    def setDepartureAirport(self, departureAirport):
        # Set the departure airport
        self.departureAirport = departureAirport

    def getDestinationAirport(self):
        # Return the destination airport
        return self.destinationAirport

    def setDestinationAirport(self, destinationAirport):
        # Set the destination airport
        self.destinationAirport = destinationAirport

    def getArrivalDateTime(self):
        # Return the arrival date and time
        return self.arrivalDateTime

    def setArrivalDateTime(self, arrivalDateTime):
        # Set the arrival date and time
        self.arrivalDateTime = arrivalDateTime

    def getGate(self):
        # Return the gate
        return self.gate

    def setGate(self, gate):
        # Set the gate
        self.gate = gate

    def getSeatNumber(self):
        # Return the seat number
        return self.seatNumber

    def setSeatNumber(self, seatNumber):
        # Set the seat number
        self.seatNumber = seatNumber

    def getElectronicTicket(self):
        # Return the electronic ticket information
        return self.electronicTicket

    def setElectronicTicket(self, electronicTicket):
        # Set the electronic ticket information
        self.electronicTicket = electronicTicket

    def setTicketNumber(self, ticketNumber):
        # Set the ticket number
        self.electronicTicket = ticketNumber
class BoardingPassSystem:
    def __init__(self):
        # Initialize the BoardingPassSystem object with no boarding pass information
        self.boardingPass = None

    def generateBoardingPass(self, passenger, flight):
        # Generate a boarding pass using passenger and flight information
        self.boardingPass = BoardingPass(passenger.getName(), flight.getFlightNumber(), flight.getDepartureAirport(),
                                         flight.getDestinationAirport(), flight.getArrivalDateTime(), flight.getGate(),
                                         passenger.getSeatNumber(), passenger.getTicketNumber())

    def updateBoardingPass(self, boardingPass):
        # Update the boarding pass with new information
        self.boardingPass = boardingPass

    def viewBoardingPass(self):
        # View the boarding pass information
        if self.boardingPass:
            print("Passenger Name:", self.boardingPass.getPassengerName())
            print("Flight Number:", self.boardingPass.getFlightNumber())
            print("Departure Airport:", self.boardingPass.getDepartureAirport())
            print("Destination Airport:", self.boardingPass.getDestinationAirport())
            print("Arrival Date Time:", self.boardingPass.getArrivalDateTime())
            print("Gate:", self.boardingPass.getGate())
            print("Seat Number:", self.boardingPass.getSeatNumber())
            print("Electronic Ticket:", self.boardingPass.getElectronicTicket())
        else:
            print("No boarding pass information available.")

    def updatePassengerInfo(self):
        # Ask user if they want to update passenger info
        update_passenger = input("Do you want to update passenger information? (Y/n): ").lower()
        if update_passenger == 'y':
            # Ask user which information they want to update
            print("Which passenger information would you like to update?")
            print("1. Name")
            print("2. Ticket Number")
            print("3. Seat Number")
            choice = input("Enter your choice: ")

            if choice == '1':
                new_name = input("Enter new passenger name: ")
                self.boardingPass.setPassengerName(new_name)
            elif choice == '2':
                new_ticket_number = input("Enter new ticket number: ")
                passenger.setTicketNumber(new_ticket_number)  # Update passenger information directly
                self.boardingPass.setTicketNumber(new_ticket_number)  # Update boarding pass with new ticket number
            elif choice == '3':
                new_seat_number = input("Enter new seat number: ")
                self.boardingPass.setSeatNumber(new_seat_number)
            else:
                print("Invalid choice.")
        else:
            print("Passenger information not updated.")



# Create objects for all classes
airport = Airport("National Airport")
passenger = Passenger("Omer", "123456789", "09A")
flight = Flight("1234", "Dubai", "NewYork", datetime(2024, 2, 28, 8, 0), datetime(2024, 2, 28, 10, 0), "Gate1")
boardingPassSystem = BoardingPassSystem()

# Generate boarding pass
boardingPassSystem.generateBoardingPass(passenger, flight)

# View boarding pass information
print("\n\t\tView the Boarding pass")
boardingPassSystem.viewBoardingPass()



# Update passenger information
print("\n\t\tTo Update the Boarding pass Information")
boardingPassSystem.updatePassengerInfo()

# View updated boarding pass information
print("\n\t\tView the Boarding pass After Update the Boarding pass Information")
boardingPassSystem.viewBoardingPass()


# In[ ]:




