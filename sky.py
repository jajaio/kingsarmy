import colors as c
import torch
import time as t
import classes as cl
import anim
import town
import skull

author = 'jajaio'

def select():
    print(c.clear)
    print(c.yellow+"You are flying up in the sky.")
    t.sleep(1)
    where=input("Would you like to go Torch Island? Skull Woods? Ancient Dunes? Or back to KillFang? (1), (2), (3), (4)"+c.reset+" >>>"+c.violet).strip()
    if where == '1':
        print(c.yellow+'You fly down to Torch Island.')
        t.sleep(1)
        anim.dragonanim()
        torch.island()
    elif where == '2':
        if cl.Player.wname == 'Dull Blade':
            print(c.yellow+'Your weapon is too weak! Go find a new one before you come here.')
            t.sleep(1)
            input('[Press enter to continue]')
            select()
        else:
            print(c.yellow+'You fly down to Skull Woods.')
            t.sleep(1)
            anim.dragonanim()
            skull.woods()
    elif where == '3':
        print('Still in development.')
        t.sleep(2)
        select()
    elif where == '4':
        print(c.yellow+'You fly back to KillFang.')
        t.sleep(1)
        anim.dragonanim()
        town.hub()
    else:
        print(c.yellow+"I don't understand...")
        t.sleep(1)
        select()

if __name__=='__main__':
    select()
