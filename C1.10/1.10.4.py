class People:
    def __init__(self, name = None, city = None):
        if name is None:
            name = input("Enter name: ")
        self.name = name
        if city is None:
            city = input("Enter city: ")
        self.city = city

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

class Volunteer(People):
    def __init__(self, name = None, city = None, status = None):
        super().__init__(name, city)
        if status is None:
            city = input("Enter status: ")
        self.status = status

    def get_status(self):
        return self.status
    
    def represent(self):
        return f"{self.name} from {self.city}. Status: {self.status}"

guest_1 = Volunteer(name = "Ivan Petrov", city = "Moscow", status = "Mentor")
guest_2 = Volunteer(name = "Peter Torov", city = "Kaluga", status = "Padawan")
guest_3 = Volunteer(name = "Ira Seter", city = "New York", status = "Jedi")

guests_list = [guest_1, guest_2, guest_3]

for guest in guests_list:
    print(guest.represent())