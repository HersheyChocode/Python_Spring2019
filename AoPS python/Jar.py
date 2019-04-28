class Jar:

    def __init__(self, liters):

        #instantiates variable liters, which is the capacity of the jar
        self.liters = liters

        #instantiates variable status, which is the status of the jar
        #how much the jar is holding
        self.status = 0 #Jar starts off without any water in it

    def __str__(self):

        #returns string form of the jar capacity and its status
        return "A "+str(self.liters)+" liter jar with "+str(self.status)+" liters of water"

    def empty(self):

        #sets status to 0
        self.status = 0

    def fill(self):

        #fills status to jar capacity
        self.status = self.liters

    def pour(self, oth):

        #the sum of the liters in both jars
        total = self.status + oth.status

        #if the total is less than the other jar:
        #the other jar adds the first jar's status
        #the first jar gets emptied
        if total <= oth.liters:
            oth.status += self.status
            self.empty()

        #if the total is more than the other jar:
        #the first jar's status is the total minus the other jar's capacity
        else:
            self.status = total-oth.liters
            oth.fill()

#creates jars with 5 and 3 liter capacities
three = Jar(3)
five = Jar(5)

#steps:

three.fill() #3, 0 
three.pour(five) #0, 3
three.fill() #3, 3
three.pour(five) #1, 5
five.empty() #1, 0
three.pour(five) #0, 1
three.fill() #3, 1
three.pour(five) #0, 4

print(five) #4 L in 5 L jar

