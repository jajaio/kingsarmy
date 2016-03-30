import colors as c
import torch
import time as t
import classes as cl

author = 'jajaio'

def select():
    print("You are flying up in the sky.")
    t.sleep(1)
    where=input("Would you like to go Torch Island? Skull Woods? Ancient Dunes? Or back to KillFang? (1), (2), (3), (4)").strip()
    if where == '1':
        print('You fly down to Torch Island.')
        t.sleep(1)
        torch.island()
    elif where == '2':
        pass
    elif where == '3':
        pass
    elif where == '4':
        pass
    else:
        pass
