import classes as cl
import save
import time as t
import colors as c
import load
import sky
import anim
author='jajaio'

def inn():
    print(c.clear)
    innq=input(c.yellow+"You walk into your tent. Would you like to rest here? Or leave? (1), (2)"+c.reset+">>>"+c.violet).strip()
    if innq=="1":
        print(c.yellow+"You shut your eyes and rest for a bit.")
        t.sleep(.5)
        cl.show_player()
        print("[Game saved!]")
        save.save_game()
        qu=input('[Would you like to keep playing?] (Y/N)'+c.reset+' >>>'+c.violet).strip().lower()
        if qu=='y':
            print(c.yellow+'[Resuming game]')
        elif qu=='n':
            print(c.yellow+'[Exiting game...]')
            exit()
        else:
            print(c.yellow+'[Resuming game]')
        print(c.yellow+"You wake up feeling rested...")
        t.sleep(1.5)
        hub()
    elif innq=="2":
        print(c.yellow+"You go back outside.")
        t.sleep(1)
        hub()
    else:
        print(c.yellow+"I don't understand...")
        t.sleep(1)
        inn()

def hub():
    print(c.clear)
    print(c.yellow+"You arive on the King's Great Dragon, KillFang.")
    hubquestion=input("Would you like to go back to your tent? The shrine? Or into the open skies? (1), (2), (3)"+c.reset+" >>>"+c.violet)
    if hubquestion=="1":
        print(c.yellow+"You decide to go back to your tent.")
        t.sleep(1.3)
        inn()
    elif hubquestion=="2":
        print(c.yellow+"You decide to go to the shrine.")
        t.sleep(1.3)
        shrine()
    elif hubquestion=="3":
        print(c.yellow+"You hop on "+str(cl.Player.dragon)+" and fly off into the distance.")
        t.sleep(1.3)
        anim.dragonanim()
        sky.select()
    else:
        print("I don't understand...")
        t.sleep(1)
        hub()

def shrine():
    print(c.clear)
    #This is where the player can lvl up

if __name__=='__main__':
    hub()
