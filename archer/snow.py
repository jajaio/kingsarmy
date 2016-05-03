import battleengine as b
import random
import classes as cl
import colors as c
import time as t
import sky
import anim
import blarneybattle
import save
import dotdotdot as d

author="jajaio"

def random_monster():
    monsters=[cl.Slime, cl.Bandit, cl.Goblin]
    monster=random.choice(monsters)
    cl.Foe=monster

def explore():
        print(c.yellow+"You decide to explore the mountain for a bit.")
        d.normal()
        if cl.Player.wname=='Wooden Bow':
            print(c.yellow+'You find a bow, placed nicely at a shrine of Adari.')
            t.sleep(1)
            sword=input('Do you want to take the bow? (Y/N)'+c.reset+" >>>"+c.violet).strip().lower()
            if sword == 'y':
                print(c.yellow+"You picked up the bow, and it's arrows.")
                t.sleep(1)
                print("You received Adari's personal Bow, the Sun Bow!")
                cl.Player.wname="Sun Bow"
                cl.Player.att+=3
                save.save_game()
                cl.show_player()
                input('[Game saved! Press enter to continue.]')
                mountain()
            elif sword == 'n':
                print(c.yellow+'You hike back to the main part of the mountain.')
                t.sleep(1)
                input('[Press enter to continue.]')
                mountain()
            else:
                print(c.yellow+"I don't understand...")
                t.sleep(1.25)
                explore()
        else:
            print(c.yellow+'You arrive at the shrine of Adari.')
            t.sleep(1)
            print('Nothing to see here!')
            input('[Press enter to continue.]')
            mountain()

def mountain():
    print(c.clear)
    print(c.yellow+"You arrive on Snow Mountain.")
    t.sleep(1)
    f=input(c.yellow+"Do you want to look for monsters? Travel into the ice cavern? Explore the mountain? Or fly back to the skies? (1), (2), (3), (4)"+c.reset+" >>>"+c.violet)
    if f == "1":
        print(c.yellow+"You decide to look around.")
        t.sleep(1.5)
        d.normal()
        random_monster()
        print(c.yellow+"You found a "+c.red+cl.Foe.mname+c.yellow+"!")
        t.sleep(1)
        b.fight()
        mountain()
    elif f == "2":
        print(c.clear)
        print(c.yellow+'You enter the ice cavern.')
        t.sleep(1)
        d.normal()
        if cl.Player.bcomp == 0:
            #work on this
            print(c.yellow+'You are at the peak of the volcano. You begin to hear scratching and clawing against the inside.')
            t.sleep(2)
            print('A large goblin crawls out, with a skull mask on.')
            t.sleep(2)
            print('You draw your sword and prepare for battle.')
            monster=cl.Blarney
            t.sleep(2)
            input('[Press enter to continue]')
            blarneybattle.fight()
        elif cl.Player.bcomp != 0:
            print(c.yellow+"Nothing to see here!")
            t.sleep(1.25)
            mountain()

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
        mountain()

if __name__=='__main__':
    mountain()
