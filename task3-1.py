from datetime import datetime


class Event:
    def __init__(self, name, regular_price, date):
        self.name = name
        self.regular_price = regular_price
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        if (self.date - datetime.now()).days < 0:
            raise ValueError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @property
    def regular_price(self):
        return self.__regular_price

    @regular_price.setter
    def regular_price(self, regular_price):
        if not isinstance(regular_price, int):
            raise TypeError
        if regular_price < 0:
            raise ValueError
        self.__regular_price = regular_price

    def __str__(self):
        return f"Event called \"{self.name}\" \nPrice: {self.regular_price} \nDate: {self.date}\n\n"


class Ticket:
    __tickets = {}

    def __init__(self, event):
        self.event = event
        self.number = len(self.__tickets) + 1
        self.order_date = datetime.now()
        self.date = event.date
        self.price = event.regular_price
        if event not in self.__tickets.keys():
            self.__tickets.update({event: []})
        self.__tickets[event].append(self)

    def ask_price(self):
        return f"Price: {self.price}\n\n"

    def ticket_by_number(self, number):
        for i in self.__tickets:
            for ticket in self.__tickets[i]:
                if ticket.number == number:
                    return self.__tickets.get(i)

    def __str__(self):
        return f"Ticket №{self.number} to the {self.event.name} event for {self.date} \nRegular price: {self.price}\n\n"


class RegularTicket(Ticket):
    def __init__(self, event):
        super().__init__(event)

    def __str__(self):
        return f"Type: regular ticket \nPrice: {self.price}\n\n"


class AdvanceTicket(Ticket):
    def __init__(self, event, discount=0.4):
        super().__init__(event)
        self.price = event.regular_price - event.regular_price * discount

    def __str__(self):
        return f"Type: advance ticket \nPrice: {self.price}\n\n"


class StudentTicket(Ticket):
    def __init__(self, event, discount=0.5):
        super().__init__(event)
        self.price = event.regular_price - event.regular_price * discount

    def __str__(self):
        return f"Type: student ticket \nPrice: {self.price}\n\n"


class LateTicket(Ticket):
    def __init__(self, event, discount=0.1):
        super().__init__(event)
        self.price = event.regular_price + event.regular_price * discount

    def __str__(self):
        return f"Type: late ticket \nPrice: {self.price}\n\n"


def type_of_ticket(self, student, advance_limit=60, late_limit=10):
    difference = (self.date.date() - self.order_date.date()).days
    if student:
        return StudentTicket(self.event)
    elif difference >= advance_limit:
        return AdvanceTicket(self.event)
    elif 0 < difference < late_limit:
        return LateTicket(self.event)
    elif difference < 0:
        return "The event has already passed"
    else:
        return RegularTicket(self.event)


def main():
    event1 = Event("a", 500, "2022-11-12 10:00")
    ticket1 = Ticket(event1)
    print(type_of_ticket(ticket1, False))
    print(ticket1.ask_price())
    print(ticket1)

    event2 = Event("b", 1000, "2023-01-10 18:00")
    ticket2 = Ticket(event2)
    print(type_of_ticket(ticket2, False))
    print(ticket2.ask_price())
    print(ticket2)


main()
