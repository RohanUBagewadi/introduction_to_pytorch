
"""
    OOp
   """


class User:

    def log(self):
        print(self)


class Teacher(User):

    def log(self):
        print("I am a teacher")


class Customer(User):

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        print("Getting name")
        return self._name

    @name.setter
    def name(self, name):
        print("Setting name")
        self._name = name

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    @staticmethod
    def read_customer():
        print("Reading customer")

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        else:
            return False


c = Customer("Caleb", "Gold")
print(c.name, c.membership_type)

c2 = Customer("Brad", "Silver")
print(c2.name, c2.membership_type)

customers = [Customer("Caleb", "Gold"), Customer("Brad", "Silver")]
print(customers[0].membership_type)
customers[0].update_membership("Bronze")
print(customers[0].membership_type)

print(customers[1])

print(customers[0] == customers[1])
customers = [Customer("Caleb", "Gold"), Customer("Caleb", "Gold")]
print(customers[0] == customers[1])

customers = [Customer("Caleb", "Gold"), Customer("Brad", "Silver"), Teacher()]
print(customers[2].log())