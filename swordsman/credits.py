import time as t
import colors as c
import town
author='jajaio'

def roll():
    print(c.clear)
    print(c.reset+"Lead Developer: Jackson Martin")
    t.sleep(2)
    print("Lead Designers: Jackson Martin, Samuel Mock")
    t.sleep(2)
    print("Beta Testers: Gunnar Olsen, Cole Vahey, Christian Renaud, Soren Wilson, David Blalock")
    t.sleep(2)
    print("Special thanks to: Rob Muhlestein")
    t.sleep(2)
    input('[Game Saved! Press enter to continue]')
    town.hub()
if __name__ == '__main__':
    roll()
