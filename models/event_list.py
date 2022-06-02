from models.event import *

event1 = Event(
    "02/06/22",
    "Diamond Jubilee",
    100,
    "London",
    "70th Anniversary of being the Queen",
    True,
    False,
)
event2 = Event("20/05/22", "Birthday", 10, "Glasgow", "Mothers birthday", False, False)
event3 = Event(
    "23/05/22", "Python Meeting", 25, "Edinburgh", "CodeClan Python Meetup", False, True
)

events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)
