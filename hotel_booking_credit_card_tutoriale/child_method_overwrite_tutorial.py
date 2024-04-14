
# this is an example of how to overwrite a method in a child class
# that was inherited from the parent class

class Ticket:
    def __init__(self):
        pass
    def generate(self):
        return "Ticket generated"
# as you can see the above the generate method in the parent class
# returns "Ticket generated"

class DigitalTicket(Ticket):
    def download(self):
        pass
    def generate(self):
        return "Different Ticket generated"
# here the generate method is re defined within the child class

dt = DigitalTicket()

t = Ticket()


print(dt.generate())
# here when the DigitalTicket is generated it returns
# "Different Ticket generated"

print (t.generate())
# here when the Ticket is generated it returns
# "Ticket generated" keeping the original txt within the generate
# method. this means the original parent method is not modified