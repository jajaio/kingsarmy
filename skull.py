import skullengine as b
import random
import classes as cl
import colors as c
import time as t
import sky
import anim
import dotdotdot as d
import elynbattle

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
        d.normal()
        random_monster()
        print(c.yellow+"You found a "+c.red+cl.Foe.mname+c.yellow+"!")
        t.sleep(1)
        b.fight()
        woods()
    elif f == "2":
        print(c.yellow+'You decide to enter the cave.')
        t.sleep(1)
        d.normal()
        print(c.yellow+"You see an old woman, writing in a journal.")
        t.sleep(2)
        print('As you take a another step, she notices you.')
        t.sleep(2)
        print('You draw your blade, so the flame will make more light.')
        t.sleep(2)
        print('She looks at you with rage, and releases a high pitched scream.')
        t.sleep(2)
        print('Her skin begins to peel off, showing her allegiance to the Dark Skulls.')
        t.sleep(2)
        print('You prepare to battle.')
        t.sleep(2)
        input('[Press enter to continue.]')
        monster=cl.Elyn
        elynbattle.fight()
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
