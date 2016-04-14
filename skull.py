import skullengine as b
import random
import classes as cl
import colors as c
import time as t
import sky
import anim

author="jajaio"

def random_monster():
    monsters=[cl.Skeleton, cl.SkullKid, cl.DarkSkull]
    monster=random.choice(monsters)
    cl.Foe=monster

def woods():
    print(c.clear)
    print(c.yellow+"You arrive in the Skull Woods.")
    t.sleep(1)
    f=input(c.yellow+"Do you want to look for monsters? Enter the cave? Or fly back to the skies? (1), (2), (3)"+c.reset+" >>>"+c.violet)
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
        woods()
    elif f == "2":
        print(c.clear)
    elif f == "3":
        print(c.yellow+"You fly back into the sky.")
        t.sleep(1)
        anim.dragonanim()
        sky.select()
    else:
        print("I don't know what you mean....")
        t.sleep(1)
        woods()

if __name__=='__main__':
    woods()
