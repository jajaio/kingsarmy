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
    lvl=1
    name=None
    dragon=None

class Foe(Thing):
    mname="Test mob name"
#Torch Island
class Bandit(Foe):
    hp=10
    agi=3
    att=3

class Slime(Foe):
    hp=5
    agi=0
    att=1

class Goblin(Foe):
    hp=12
    agi=2
    att=2

class Blarney(Foe):
    hp=20
    agi=0
    att=5
    deff=1
#Skull Woods
class DarkSkull(Foe):
    hp=25
    agi=5
    att=7
    deff=1

class SkullKid(Foe):
    hp=15
    agi=5
    att=5

class Skeleton(Foe):
    hp=20
    agi=8
    att=5
    deff=2

class Elyn(Foe):
    hp=25
    agi=18
    att=6
    mp=1
#Ancient Dunes
class DarkBat(Foe):
    hp=20
    agi=30
    att=10
class DarkScorpion(Foe):
    hp=30
    agi=15
    att=8
    deff=1

class DeathSkull(Foe):
    hp=50
    agi=0
    att=12
    deff=1

class King(Foe):
    mname='King of the Skulls'
    hp=60
    #learn more about the character before cont.

def show_player():    
    yext='''
    {p.name} Stats:
    Level: {p.lvl}
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
