import colors as c
import time as t
import classes as cl
import duneengine as b
import save
import dotdotdot as d
import ancient

author = 'jajaio'

def shrine():
    print(c.clear)
    print(c.yellow+'You find a a broken down shrine of Adari.')
    t.sleep(1)
    pray=input("Do you wish to pray here? (Y/N)"+c.reset+' >>>'+c.violet).strip().lower()
    if pray == 'y':
        d.normal()
        if cl.Player.wname == 'Flameblade':
            cl.Player.att+=5
            cl.Player.wname='Divine Flameblade'
            print(c.yellow+'You got the Blessing of the god of flame, Adari!')
            t.sleep(1)
            print('Flameblade burns even brighter now!')
            t.sleep(1)
            save.save_game()
            input('[Game saved! Press enter to continue.]')
            main()
        else:
            print(c.yellow+'You take your stuff and leave.')
            t.sleep(1)
            input('[Press enter to continue.]')
            main()
    elif pray == 'n':
        print(c.yellow+'You decide to leave.')
        t.sleep(1)
        main()
    else:
        print("I don't understand...")
        t.sleep(1.25)
        shrine()

def main():
    print(c.clear)
    print(c.yellow+"You arrive in the Pyramid.")
    question=input('Do you want to look around? Or leave? (1), (2)'+c.reset+' >>>'+c.violet).strip()
    if question == '1':
        prompt=input(c.yellow+'Do you want to go left or right? (1), (2)'+c.reset+' >>>'+c.violet).strip()
        if prompt == '1':
            pass
        elif prompt == '2':
            shrine()
        else:
            print(c.yellow+"I don't understand...")
            t.sleep(1.25)
            main()
    elif question == '2':
        print(c.yellow+'You go back outside.')
        t.sleep(1)
        ancient.dunes()

if __name__=='__main__':
    main()
