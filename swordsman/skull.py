import skullengine as b
import random
import classes as cl
import colors as c
import time as t
import sky
import anim
import dotdotdot as d
import elynbattle
import grimnovebattle
import load

author="jajaio"

def random_monster():
    monsters=[cl.Skeleton, cl.SkullKid, cl.DarkSkull]
    monster=random.choice(monsters)
    cl.Foe=monster

def fortress():
    print(c.clear)
    print(c.yellow+'You arrive the fortress of the Dark Skulls.')
    t.sleep(1)
    prompt=input('Do you want to enter? (Y/N)'+c.reset+' >>>'+c.violet).strip().lower()
    if prompt == 'y':
        if cl.Player.skulls == 3:
            print(c.yellow+'The power of the 3 ancient skulls break down the dark magic beam.')
            #Setup for fight with story text here
            grimnovebattle.fight()
        else:
            print(c.yellow+'You try to open the door, but a beam of dark magic blocks your way.')
            t.sleep(1)
            print("You head back into the woods.")
            t.sleep(1)
            input('[Press enter to continue.]')
            woods()
    elif prompt == 'n':
        print(c.yellow+"Head head back to the woods.")
        d.normal()
        woods()
    else:
        print("I don't know what you mean...")
        t.sleep(1.25)
        fortress()

def woods():
    print(c.clear)
    print(c.yellow+"You arrive in the Skull Woods.")
    t.sleep(1)
    f=input(c.yellow+"Do you want to look for monsters? Enter the cave? Explore the woods? Or fly back to the skies? (1), (2), (3), (4)"+c.reset+" >>>"+c.violet)
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
        print(c.yellow+"You decide to exlpore the woods.")
        t.sleep(1)
        d.normal()
        fortress()
    elif f == "4":
        print(c.yellow+"You fly back into the sky.")
        t.sleep(1)
        anim.dragonanim()
        sky.select()
    else:
        print("I don't know what you mean....")
        t.sleep(1.25)
        woods()

if __name__=='__main__':
    load.load_game()
    woods()
