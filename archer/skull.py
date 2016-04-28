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
import archerbattle

author="jajaio"

def random_monster():
    monsters=[cl.Skeleton, cl.SkullKid, cl.DarkSkull]
    monster=random.choice(monsters)
    cl.Foe=monster

def final():
    des=input(c.yellow+"Do you want to side with Grimnove? Or fight him with the archer? (1), (2)"+c.reset+" >>>"+c.violet).strip()
    if des == '1':
        print(c.yellow+"You point your blade at the archer.")
        t.sleep(2)
        print("He draws his arrow.")
        t.sleep(2)
        print("The battle between Amerus's two chosen heroes begin.")
        t.sleep(2)
        input('[Press enter to continue.]')
        archerbattle.fight()
    elif des == '2':
        print(c.yellow+'The archer aims his bow, and you grip your sword.')
        t.sleep(2)
        print("And Amerus's two chosen heroes begin the final fight against Grimnove.")
        input('[Press enter to continue]')
        grimnovebattle.fight()
    else:
        print(c.yellow+"I don't know what you mean...")
        t.sleep(1.25)
        final()

def fortress():
    print(c.clear)
    print(c.yellow+'You arrive the fortress of the Dark Skulls.')
    t.sleep(1)
    prompt=input('Do you want to enter? (Y/N)'+c.reset+' >>>'+c.violet).strip().lower()
    if prompt == 'y':
        if cl.Player.skulls == 3:
            print(c.yellow+'The power of the 3 ancient skulls break down the dark magic beam.')
            t.sleep(2)
            print('You dash into the fortress.')
            t.sleep(2)
            print('You look around.')
            t.sleep(2)
            print("It's empty.")
            t.sleep(2)
            print('You begin to feel the ground shake.')
            t.sleep(2)
            print('The fortress ground gives out, and you fall down with the debris.')
            t.sleep(2)
            print('You lift yourself up.')
            t.sleep(2)
            print('You see another soldier of the army, with a bow and a flaming arrow.')
            t.sleep(2)
            print('You look ahead, and see a large Dark Skull approaching you.')
            t.sleep(2)
            print("Grimnove, the god of dark is standing in front of you two.")
            t.sleep(2)
            print('"Kill that archer, and we can rule the world together. You will be king, and I will be god."')
            t.sleep(2)
            input('[Press enter to continue.]')
            final()

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
        if cl.Player.ecomp == 0:
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
        elif cl.Player.ecomp != 0:
            print(c.yellow+'Nothing to see here!')
            t.sleep(1.25)
            woods()
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
