class Event:
    def __init__(
        self, date, name, num_guests, room_location, description, done, recurring
    ):
        self.date = date
        self.name = name
        self.num_guests = num_guests
        self.room_location = room_location
        self.description = description
        self.done = done
        self.recurring = recurring
