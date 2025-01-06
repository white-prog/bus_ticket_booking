import booking



def main():
    #work in progress
    ticket = booking.Tickets(50,"Messi")
    print(f"BUS TICKET BOOKING SYSTEM {ticket.get_busName}")
    print("1. Book seat")
    print("2. Show tickets")
    print("3. Cancel ticket")
    print("4. Exit")
    while True:
        choice = int(input("Enter choice"))
        if choice == 4:
            break
        elif choice == 1:
            username = input("Enter name: ")
            age = int(input("Enter age: "))
            seats = int(input("Enter number of seats: "))
            ticket.book_seat(username,age,seats)


if __name__ == "__main__":
    main()