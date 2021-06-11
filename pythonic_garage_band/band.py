from abc import abstractmethod

class Band():
    all_bands=[]
    all_members=[]
    def __init__(self,name,members) :
        self.name=name
        self.members=members
        Band.all_bands.append(self)


class Musician ():
    '''
    base class
    '''
    member=[] #all instance
    def __init__(self,name) :
        self.name=name
    @abstractmethod
    def __str__(self) :
        pass
    @abstractmethod
    def __repr__(self) :
        pass
    @abstractmethod
    def get_instrument(self) :
        pass

class Guitarist (Musician):
    def __init__(self,name):
        self.name=name
        Guitarist.member.append(self)
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return "guitar"

class Drummer (Musician):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'My name is {self.name} and I play drums'
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    def get_instrument(self):
        return "drums"
        
class Bassist (Musician):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'My name is {self.name} and I play bass'
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return "bass"

if __name__ == '__main__':
    Drummer("Ginger Baker")
    
