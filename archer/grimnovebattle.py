import random
import colors as c
import classes as cl
import time as t
import anim
import save
import load
import bossanim
import skull
import credits

author="jajaio"


'''
My text-based battle engine, the same one used in AlphaQuest.
'''

def foeattack():
    global player, monster
    print(c.yellow+"Your foe strikes you!")
    t.sleep(1)
    bossanim.grimnoveanim()
    player.hp -= monster.att
    player.hp += player.deff

def foeheal():
    global player, monster
    if monster.mp<1:
        print(c.yellow+"Your foe tried to heal, but attacked instead!")
        t.sleep(1)
        bossanim.grimnoveanim()
        player.hp -= monster.att
        player.hp += player.deff
    else:
        print(c.yellow+"Your foe Heals.")
        t.sleep(1)
        bossanim.grimnoveanim()
        monster.hp+=15
        monster.mp-=1

def ai():
	listy=[foeheal,foeattack]
	move=random.choice(listy)
	if move==foeheal:
		foeheal()
	elif move==foeattack:
		foeattack()
	else:
		input("Fatal Error")

def pmove():
    global q, player, monster
    if q=="1":
        print(c.yellow+"You attack!")
        t.sleep(1.25)
        anim.playerattanim()
        monster.hp-=player.att
        monster.hp+=monster.deff
    elif q=="2" and player.mp <1:
        print(c.yellow+"You can not heal, so you attack instead.")
        t.sleep(1)
        anim.playerattanim()
        monster.hp-=player.att
        monster.hp+=monster.deff
    elif q=="2":
        print(c.yellow+"You decide to stay back and heal.")
        t.sleep(1)
        anim.playermpanim()
        player.hp+=15
        player.mp-=1

def scanner():
    if player.hp < 1:
        print("You Died!")
        t.sleep(1)
        ter=input(c.yellow+"Do you want to keep playing, or quit? (1), (2)"+c.reset+" >>>"+c.violet).strip()
        if ter == '1':
            skull.woods()
        elif ter == '2':
            exit()
        else:
            skull.woods()
    elif monster.hp < 1:
        finish()

def finish():        
    print(c.yellow+'You go in for the final blow.')
    t.sleep(2)
    print('Flameblade unleashes a large burning flame.')
    t.sleep(2)
    print("An arrow punctures Grimnove's head")
    t.sleep(2)
    print("Light begins to spurt out from Grimnove's broken body")
    t.sleep(2)
    print('Debris is crashing down through the room, but flames cover you two like a shield.')
    t.sleep(2)
    print('You crawl out from the debris.')
    t.sleep(2)
    input('[Press enter to continue.]')
    credits.roll()

    
def fight():
    global q, player, monster
    load.load_game()
    player=cl.Player()
    monster=cl.Grimnove()
    while True:
        if player.hp < 1:                                                                                                                                                                            
            print(c.yellow+"You Died!")                                                                                                                                                                       
            t.sleep(1)                                                                                                                                                                               
            ter=input("Do you want to keep playing, or quit? (1), (2)"+c.reset+" >>>"+c.violet).strip()                                                                                          
            if ter == '1':                                                                                                                                                                           
                skull.woods()                                                                                                                                                                               
            elif ter == '2':                                                                                                                                                                         
                exit()                                                                                                                                                                               
            else:                                                                                                                                                                                    
                skull.woods()                                                                                                                                                                               
        elif monster.hp < 1:                                                                                                                                                                         
            finish()
        else:
            print(c.clear)
            print(c.blue+player.name+str(" HP = ")+str(player.hp)+str(": ")+player.name+str(" MP = ")+str(player.mp))
            print(c.red+monster.mname+str(" HP = "+str(monster.hp)+str(": ")+monster.mname+str(" MP = ")+str(monster.mp)))
            q=input(c.reset+"Attack(1) or Heal(2)? >>>"+c.violet).strip().lower()
            if player.agi >= monster.agi:
                pmove()
                scanner()
                ai()
            elif monster.agi > player.agi:
                ai()
                scanner()
                pmove()

if __name__=='__main__':
    load.load_game()
    cl.Foe=cl.Grimnove
    fight()
