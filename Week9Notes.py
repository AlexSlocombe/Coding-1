example = "Hello Coding One".split(" ")
#example is the property, .split is the method

print (example)

#Defining your own class
class Vehicle:
    type = "Unknown"
    size = "Unknown"
    __license = "A" #creating a private member, not too relevant to python
    occupant_layout = [2, 3]

    def getSize(self):  #defining a method
        return self.size; 

    def __init__(self, type="Unknown", size="Unknown"):  #defining a constructor
        self.type = type
        self.size = size

    def __calculate_occupant_numbers(self): #creating a private function
        return sum(self.occupant_layout)
Car = Vehicle() 
Truck = Vehicle("Truck", "Big")

print(Vehicle.type) #== Car
print(Car) #== Vehicle object
print(Truck.type) #== Truck
print(Truck.getSize())



