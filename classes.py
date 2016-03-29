import colors as c
author="jajaio"

class Thing():
	hp=None #Health
	agi=None #Agility
	deff=None #Defense
	att=None #Attack
	mp=None #Magic Power (Ammount of times you can heal)

class Player(Thing):
    xp=0
    name=None

class Foe(Thing):
    mname="Test mob name"

def show_player():    
    yext='''
    {p.name} Stats:
    Health: {p.hp}
    Agility: {p.agi}
    Attack: {p.agi}
    Defense: {p.deff}
    Magic: {p.mp}
    XP: {p.xp}
    '''
    print(yext.format(p=Player()))

if __name__=='__main__':
    show_player()
