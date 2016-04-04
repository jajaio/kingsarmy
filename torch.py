import battleengine as b
import random
import classes as cl
import colors as c
import time as t
import sky
import anim
import blarneybattle

author="jajaio"

def random_monster():
    monsters=[cl.Slime, cl.Bandit, cl.Goblin]
    monster=random.choice(monsters)
    cl.Foe=monster

def island():
    print(c.clear)
    print(c.yellow+"You arive on Torch island.")
    t.sleep(1)
    f=input(c.yellow+"Do you want to look for monsters? Travel up the volcano? Or fly back to the skies? (1), (2), (3)"+c.reset+" >>>"+c.violet)
    if f == "1":
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
        island()
    elif f == "2":
        print(c.clear)
        print(c.yellow+'You hike up the great volcano.')
        t.sleep(1)
        print('You are at the peak of the volcano. You begin to hear scratching and clawing against the inside.')
        t.sleep(2)
        print('A large goblin crawls out, with a skull mask on.')
        t.sleep(2)
        print('You draw your sword and prepare for battle.')
        monster=cl.Blarney
        t.sleep(2)
        input('[Press enter to continue]')
        blarneybattle.fight()
    elif f == "3":
        print(c.yellow+"You fly back into the sky.")
        t.sleep(1)
        anim.dragonanim()
        sky.select()
    else:
        print("I don't know what you mean....")
        t.sleep(1)
        island()

if __name__=='__main__':
    island()
