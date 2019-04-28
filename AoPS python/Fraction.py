class Fraction:
    '''represents fractions''' 

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        #Instanteates variables
        self.num = num
        self.denom = denom

        
        if denom == 0: #Raise an error if the denominator is zero
            raise ZeroDivisionError

    def simplified(self):

        #First get the GCF to divide numerator and denominator

        if self.num>self.denom: #If numerator > its denominator

            #Finds the gcf
            gcf = max([x for x in range(1,abs(self.num)+1)if self.num%x==self.denom%x==0])
        else: #If denominator > numerator

            #Finds the gcf
            gcf = max([x for x in range(1,abs(self.denom)+1)if self.num%x==self.denom%x==0])
           
        self.num = self.num//gcf #Simplifies numerator according to gcf
        self.denom = self.denom//gcf #Simplifies denominator according to gcf

        
        
    def __str__(self):
        
        self.simplified() #simplifies self


        if self.denom > 0 and self.num>0: #If fraction is positive
            return  str(self.num)+"/"+str(self.denom) #Return string
        
        return "-"+str(abs(self.num))+"/"+str(abs(self.denom)) #Else, return negative string


    def __float__(self):

        return self.num/self.denom #Return float

    def add(self, oth):

        #Simplify both fractions
        oth.simplified()
        self.simplified()

        #Get lcd

        #If abs(first denom) > abs(oth's denom)
        if abs(self.denom) > abs(oth.denom):

            #Get lcm
            lcm = min([x for x in range(1,abs(self.denom)+1) if (self.denom*x)%oth.denom==0])

            #Multiply with denominator to get lcd
            lcd = lcm*self.denom
        else:

            #Get lcm
            lcm = min([x for x in range(1, abs(oth.denom)+1) if (oth.denom*x)%self.denom==0])

            #Multiply with denominator to get lcd
            lcd = lcm*oth.denom

        #Variables for new numerators
        firstNum = self.num*(lcd//self.denom)
        secondNum = oth.num*(lcd//oth.denom)

        #Creates fractions with sum of new numerators, and lcd
        newFrac = Fraction(firstNum+secondNum, lcd)

        #Returns this fraction
        return newFrac

    def sub(self, oth):

        #Simplifies both fractions
        oth.simplified()
        self.simplified()

        #Same procedure of lcd as add method
        if abs(self.denom) > abs(oth.denom):
            
            lcm = min([x for x in range(1,abs(self.denom)+1) if (self.denom*x)%oth.denom==0])
            lcd = lcm*self.denom
        else:

            lcm = min([x for x in range(1, abs(oth.denom)+1) if (oth.denom*x)%self.denom==0])
            lcd = lcm*oth.denom
        
        firstNum = self.num*(lcd//self.denom)
        secondNum = oth.num*(lcd//oth.denom)

        #Creates fractions with subtracted numerators and lcd
        newFrac = Fraction(firstNum-secondNum, lcd)

        #Returns this fractions
        return newFrac

    def mul(self, oth):

        #Simplifies both fractions
        oth.simplified()
        self.simplified()

        #Creates multiplied fraction
        mulFrac = Fraction(self.num*oth.num, self.denom*oth.denom)
        #Simplifies fraction
        mulFrac.simplified()

        #Returns this fraction
        return mulFrac


    def div(self, oth):

        #Simplifies both fractions
        oth.simplified()
        self.simplified()

        #Creates divided fraction
        divFrac = Fraction(self.num*oth.denom, self.denom*oth.num)
        #Simplifes fraction
        divFrac.simplified()

        #Returns this fraction
        return divFrac

    def eq(self, oth):

        return float(self)==float(oth) #Returns whether fractions are equal



# examples
p = Fraction(3,6)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print -1/6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if implementing "normal" arithmetic methods
print(p.add(q))       # should print 1/3, since 1/2 + (-1/6) = 1/3
print(p.sub(q))  # should print 2/3, since 1/2 - (-1/6) = 2/3
print(p.sub(p))  # should print 0/1, since p-p is 0
print(p.mul(q)) # should print -1/12
print(p.div(q))  # should print -3/1
print(p.eq(r))   # should print True
print(p.eq(q))   # should print False
