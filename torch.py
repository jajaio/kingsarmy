import battleengine as b
import random
import classes as cl
import colors as c
import time as t
import town
author="jajaio"
def random_monster():
    monsters=[cl.Slime, cl.Bandit, cl.Goblin]
    monster=random.choice(monsters)
    cl.Foe=monster

def island():
    print(c.clear)
    print(c.yellow+"You arive on Torch island.")
    t.sleep(1)
    f=input(c.yellow+"Do you want to look for monsters? Or fly back to the skies? (1), (2)"+c.reset+" >>>"+c.violet)
    if f=="1":
        print(c.yellow+"You decide to look around.")
        t.sleep(1.5)
        print(c.reset)
        print(c.clear)
        print(".")
        t.sleep(.5)
        print(c.clear)
        print("..")
        t.sleep(.5)
        print(c.clear)
        print("...")
        t.sleep(.5)
        print(c.clear)
        random_monster()
        print(c.yellow+"You found a "+c.red+cl.Foe.mname+c.yellow+"!")
        t.sleep(1)
        b.fight()
        field()
    elif f=="2":
        print(c.yellow+"You fly back into the sky.")
        t.sleep(1.25)
        town.hub()
    else:
        print("I don't know what you mean....")
        t.sleep(1)
        field()

if __name__=='__main__':
    island()