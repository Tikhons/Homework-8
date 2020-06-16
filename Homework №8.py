class Donkey:
    def __init__(self, name, load, years):
        self.name = name
        self.load = load
        self.years = years
        
    def __str__(self):  
        return f"Donkey-boy {self.name}, {self.load}"
    def cry(self):
        i=self.years
        s=""
        while i!=0:
            s+="Eeyore"
            i-=1
        return s
    def work_hard(self, amount):
        i=0
        if amount<0:
            self.years+=2
        else:
            while amount!=0:
                amount-=1
                i+=1
                if i==5 and self.years!=0:
                    self.years-=1
                    i=0
    def carry(self, m):
         return(m<=self.load)
  
d = Donkey('Tikhon', 10, 5)
print(d)
print(d.cry())
d.work_hard(16)
print(d.cry())
print(d.carry(10))
print('\n')
d1 = Donkey('Tikhon', 10, 5)
d2 = Donkey('Ivan', 10, 3)
print(d1, d2, sep='\n')
d1.work_hard(11)
print(d2.cry())


