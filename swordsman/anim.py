import time as t
import colors as c

heroatt1='''
      |
      |
\_0___+
  |
  |
 / /
'''
archer1='''
\_0___}
  |
  |
 / /
'''
archer2='''
\_0___}  -->
  |
  |
 / /
'''

archer3='''
\_0___}    -->
  |
  |
 / /
'''
archer4='''
\_0___}      -->
  |
  |
 / /
'''
heroatt2='''


\_0___+----
  |
  |
 / /
'''
dragon1='''
\\    O    /
 \\  \\|/  /
  \\_^v^_/



'''
dragon2='''
     O
    \\|/
   _^v^_
  /     \\
 /       \\
/         \\
'''
heromp1='''
   <3

 \\ 0 /
  \\|/
   |
  | |
'''
heromp2='''
   <3

__ 0 __
  \\|/
   |
  | |
'''
foemp1='''
   <3

 \\ 6 /
  \\|/
   |
  | |
'''
foemp2='''
   <3

__ 6 __
  \\|/
   |
  | |
'''
foeatt1='''


 ----+___6_\\
         |
         |
        \\ \\
'''

foeatt2='''
     | 
     |
     +___6_\\
         |
         |
        \\ \\  
'''

def foeattanim():
    for count in range(2):
        print(c.clear)
        print(c.red+foeatt1)
        t.sleep(.25)
        print(c.clear)
        print(foeatt2)
        t.sleep(.25)
        print(c.clear)

def dragonanim():
    for count in range(2):
        print(c.clear)
        print(c.blue+dragon1)
        t.sleep(.5)
        print(c.clear)
        print(dragon2)
        t.sleep(.5)
        print(c.clear)

def foempanim():
    for count in range(2):
        print(c.clear)
        print(c.red+foemp1)
        t.sleep(.25)
        print(c.clear)
        print(foemp2)
        t.sleep(.25)
        print(c.clear)

def archeranim():
    for count in range(2):
        print(c.clear)
        print(c.blue+archer1)
        t.sleep(.25)
        print(c.clear)
        print(archer2)
        t.sleep(.25)
        print(c.clear)
        print(archer3)
        t.sleep(.25)
        print(c.clear)
        print(archer4)
        t.sleep(.25)
        print(c.clear)

def playerattanim():
    for count in range(2):
        print(c.clear)
        print(c.blue+heroatt1)
        t.sleep(.25)
        print(c.clear)
        print(heroatt2)
        t.sleep(.25)
        print(c.clear)

def playermpanim():
    for count in range(2):
        print(c.clear)
        print(c.blue+heromp1)
        t.sleep(.25)
        print(c.clear)
        print(heromp2)
        t.sleep(.25)
        print(c.clear)
        
if __name__=='__main__':
    print('You fly away.')
    dragonanim()
    print("You shoot your bow.")
    t.sleep(1)
    archeranim()
    print("The Player attacks!")
    t.sleep(1)
    playerattanim()
    print("The player heals!")
    t.sleep(1)
    playermpanim()
    print("The foe attacks!")
    t.sleep(1)
    foeattanim()
    print("The foe heals!")
    t.sleep(1)
    foempanim()
