import battleengine as b
import random
import classes as cl
import colors as c
import time as t
import sky
import anim
import blarneybattle
import save

author="jajaio"

def random_monster():
    monsters=[cl.Slime, cl.Bandit, cl.Goblin]
    monster=random.choice(monsters)
    cl.Foe=monster

def explore():
        print(c.yellow+"You decide to explore the island for a bit.")
        t.sleep(1)
        print(c.clear)
        print(c.reset+".")
        t.sleep(.5)
        print(c.clear)
        print("..")
        t.sleep(.5)
        print(c.clear)
        print("...")
        t.sleep(.5)
        print(c.clear)
        if cl.Player.wname=='Dull Blade':
            print(c.yellow+'You find a sword, sitting atop a stone at a shrine of Adari.')
            t.sleep(1)
            sword=input('Do you want to take the sword? (Y/N)'+c.reset+" >>>"+c.violet).strip().lower()
            if sword == 'y':
                print(c.yellow+'As you take the sword, the blade begins to burn with fire.')
                t.sleep(1)
                print("You received Adari's Holy Blade, Flameblade!")
                cl.Player.wname="Flameblade"
                cl.Player.att+=3
                save.save_game()
                cl.show_player()
                input('[Game saved! Press enter to continue.]')
                island()
            elif sword == 'n':
                print(c.yellow+'You walk back to the main part of the island.')
                t.sleep(1)
                input('[Press enter to continue.]')
                island()
            else:
                print(c.yellow+"I don't understand...")
                t.sleep(1.25)
                explore()
        else:
            print(c.yellow+'You arrive at the shrine of Adari.')
            t.sleep(1)
            print('Nothing to see here!')
            input('[Press enter to continue.]')
            island()

def island():
    print(c.clear)
    print(c.yellow+"You arrive on Torch island.")
    t.sleep(1)
    f=input(c.yellow+"Do you want to look for monsters? Travel up the volcano? Explore the island? Or fly back to the skies? (1), (2), (3), (4)"+c.reset+" >>>"+c.violet)
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
        explore()
    elif f == "4":
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
