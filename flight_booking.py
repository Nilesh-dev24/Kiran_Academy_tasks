
from abc import ABC, abstractmethod

class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare


class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10


class Booking:
    def __init__(self, booking_id, passenger, flight, tickets, subtotal, discount, total):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.total = total

    def show_booking(self):
        print("\nBooking confirmed!")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.code, "|", self.flight.source, "to", self.flight.destination)
        print("Airline:", self.flight.airline)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger type:", type(self.passenger).__name__)
        print("Tickets:", self.tickets)
        print("Base fare per ticket: ₹", self.flight.fare)
        print("Subtotal: ₹", self.subtotal)
        print("Discount: ₹", self.discount)
        print("Final amount: ₹", self.total)


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Air India", "Pune", "Delhi", 20, 4000),
            Flight("MB102", "IndiGo", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PN103", "SpiceJet", "Pune", "Hyderabad", 15, 3000)
        ]
        self.bookings = []
        self.next_id = 1001

    def display_flights(self):
        print("\nAvailable Flights:")
        for flight in self.flights:
            print(
                flight.code, "|", flight.airline, "|",
                flight.source, "to", flight.destination,
                "| Seats:", flight.seats,
                "| Fare: ₹", flight.fare
            )

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    def book_flight(self):
        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()
        if name == "":
            print("Passenger name cannot be blank.")
            return

        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Age must be greater than 0.")
                return

            passenger_type = input("Passenger type (Regular/Student): ").strip().lower()

            if passenger_type == "regular":
                passenger = RegularPassenger(name, age)
            elif passenger_type == "student":
                passenger = StudentPassenger(name, age)
            else:
                print("Invalid passenger type.")
                return

            tickets = int(input("Enter number of tickets: "))
            if tickets <= 0:
                print("Ticket count must be greater than 0.")
                return

            if tickets > flight.seats:
                print("Booking failed: Not enough seats available.")
                return

        except ValueError:
            print("Invalid input. Please enter numbers correctly.")
            return

        subtotal = flight.fare * tickets
        discount = subtotal * passenger.get_discount()
        total = subtotal - discount

        booking = Booking(
            "BK" + str(self.next_id),
            passenger, flight, tickets,
            subtotal, discount, total
        )

        flight.seats -= tickets
        self.bookings.append(booking)
        self.next_id += 1

        booking.show_booking()

    def view_booking(self):
        if len(self.bookings) == 0:
            print("No booking found.")
        else:
            self.bookings[-1].show_booking()

    def run(self):
        print("Welcome to Kiran Air Booking")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")


system = FlightBookingSystem()
system.run()
