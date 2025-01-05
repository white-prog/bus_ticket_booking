class Tickets:
    def __init__(self,seats_available,bus_Name):
        self.seats_available = seats_available
        self.bus_Name = bus_Name
        self.tickets = []
    def book_seat(self,name,age,number_of_seats):
        if self.seats_available >= number_of_seats:
            tkt_id = len(self.tickets)
            self.tickets.append([tkt_id,name,age,number_of_seats])
            print(f"{name} ticket is available, ticket id is {tkt_id}")
            self.seats_available -= number_of_seats
        else:
            print(f"{name} ticket not found")
    def show_ticket(self,id):
        low = 0 
        high = len(self.tickets) - 1
        while low <= high:
            mid = (low + high) // 2
            if show_ticket[mid][0] == id:
                print(show_ticket[mid])
            elif show_ticket[mid][0] > id:
                low = mid + 1
            else:
                high = mid - 1
        print("Ticket not found")
    def delete_ticket(self,id):
        self.seats_available += self.tickets[id - 1][3]
        self.tickets.remove(self.tickets[id  - 1])

