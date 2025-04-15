class Room:
    def __init__(self, room_number, room_type):
        self.__room_number = room_number
        self.__room_type = room_type
    
    def get_room_number(self):
        return self.__room_number
    
    def set_room_number(self, room_number):
        self.__room_number = room_number
    
    def get_room_type(self):
        return self.__room_type
    
    def set_room_type(self, room_type):
        self.__room_type = room_type
    
    def __str__(self):
        return f"Room: {self.__room_number}, Type: {self.__room_type}"


class SingleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, "Single")
    
    def get_room_type(self):
        return "Single"


class DoubleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, "Double")
    
    def get_room_type(self):
        return "Double"


class Guest:
    def __init__(self, name, guest_id):
        self.__name = name
        self.__guest_id = guest_id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_guest_id(self):
        return self.__guest_id
    
    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id
    
    def __str__(self):
        return f"Guest: {self.__name}, ID: {self.__guest_id}"


class Booking:
    def __init__(self, booking_id, guest, room):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
    
    def get_booking_id(self):
        return self.__booking_id
    
    def set_booking_id(self, booking_id):
        self.__booking_id = booking_id
    
    def get_guest(self):
        return self.__guest
    
    def set_guest(self, guest):
        self.__guest = guest
    
    def get_room(self):
        return self.__room
    
    def set_room(self, room):
        self.__room = room
    
    def __add__(self, other):
        if isinstance(other, Booking):
            combined_booking_id = f"{self.__booking_id}-{other.__booking_id}"
            return Booking(combined_booking_id, self.__guest, self.__room)
        return NotImplemented
    
    def __str__(self):
        return f"Booking: {self.__booking_id}, Guest: {self.__guest.get_name()}, Room: {self.__room.get_room_number()}"


# Example usage
guest1 = Guest("John Doe", "G001")
guest2 = Guest("Jane Smith", "G002")

room1 = SingleRoom(101)
room2 = DoubleRoom(102)

booking1 = Booking("B001", guest1, room1)
booking2 = Booking("B002", guest2, room2)

combined_booking = booking1 + booking2

print(booking1)
print(booking2)
print(combined_booking)
