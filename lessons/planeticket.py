"""Yeehaw plane ticket babyyyy."""

class PlaneTicket:
    """Ticket yeehaw."""

    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        """Initialize ticket object."""
        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost

    def __str__(self) -> str:
        """Return a readable ticket."""
        ticket_read: str = f"Flight from {self.departure_city} to {self.arrival_city}. "
        ticket_read += f"Depart at {self.departure_time}. Total cost is {self.ticket_cost} USD"
        return ticket_read
    
    def delay(self, delay_hours: int) -> None:
        """Update departure time."""
        self.departure_time += (delay_hours * 100)
        self.departure_time = self.departure_time % 2400

    def discount(self, discount: float) -> None:
        """Discount ticket cost by specific amount."""
        self.ticket_cost = self.ticket_cost * (1 - (discount/100))

def compare_prices(ticket1: PlaneTicket, ticket2: PlaneTicket) -> PlaneTicket:
    """Compare price of two tickets and pick lower one."""
    if ticket1.ticket_cost < ticket2.ticket_cost:
        return ticket1
    elif ticket1.ticket_cost > ticket2.ticket_cost:
        return ticket2
    elif ticket1.ticket_cost == ticket2.ticket_cost:
        return ticket2

ticket: PlaneTicket = PlaneTicket("LA", "NYC", 1100, 800.50)
ticket.delay(2)
ticket.discount(13.0)
print(ticket)

my_ticket: PlaneTicket = PlaneTicket("Raleigh", "New Orleans", 1000, 85.25)
print(my_ticket)
my_ticket.delay(2)
my_ticket.discount(10.0)

lauren_ticket: PlaneTicket = PlaneTicket("Orlando", "San Fransisco", 1100, 100.50)
print(compare_prices(my_ticket, lauren_ticket))