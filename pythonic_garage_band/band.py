from abc import abstractmethod
'''
Use Python classes to model a Band made up of different kinds of musicians.

Start with Guitarist,Bassist, and Drummer.

Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.
'''
class Band :
    '''
    A Band instance should have a name attribute which is a string.
    A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
    A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
    A Band instance should have appropriate __str__ and __repr__ methods.
    A Band should have a class method to_list which returns a list of previously created Band instances

    '''
    allmembers=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members#attribute which is a list of instances that inherit from Musician base (or super) class.
        Band.allmembers.append(self)
        return print(f'hello')
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def play_solos():
        pass
    @classmethod
    def to_list (cls):
         return Band.allmembers
    
class Musician:
    '''
    Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
    Each kind of Musician instance should have a get_instrument method that returns string.
    Each kind of Musician instance should have a play_solo method that returns string.
    '''
    def __init__(self) :
        pass
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def get_instrument():
        return "string"
    def play_solo():
        pass

class Guitarist(Musician):
    pass
    # return "My name is Joan Jett and I play guitar"
class Bassist(Musician):
    pass
class Drummer(Musician):
    pass
if __name__ == '__main__':
    