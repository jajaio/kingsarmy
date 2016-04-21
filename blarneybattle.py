import random
import colors as c
import classes as cl
import time as t
import anim
import save
import load
import torch
import bossanim

author="jajaio"


'''
My text-based battle engine, the same one used in AlphaQuest.
'''

def foeattack():
    global player, monster
    print(c.yellow+"Your foe strikes you!")
    t.sleep(1)
    bossanim.blarneyattanim()
    player.hp -= monster.att
    player.hp += player.deff

def foeheal():
    global player, monster
    if monster.mp<1:
        print(c.yellow+"Your foe tried to heal, but attacked instead!")
        t.sleep(1)
        bossanim.blarneyattanim()
        player.hp -= monster.att
        player.hp += player.deff
    else:
        print(c.yellow+"Your foe Heals.")
        t.sleep(1)
        bossanim.blarneyattanim()
        monster.hp+=30
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
        player.hp+=30
        player.mp-=1

def scanner():
    if player.hp < 1:
        print("You Died!")
        t.sleep(1)
        ter=input(c.yellow+"Do you want to keep playing, or quit? (1), (2)"+c.reset+" >>>"+c.violet).strip()
        if ter == '1':
            torch.island()
        elif ter == '2':
            exit()
        else:
            torch.island()
    elif monster.hp < 1:
        finish()

def finish():        
    print(c.yellow+"You won!")
    t.sleep(1)
    print("You got 75 XP!")
    cl.Player.xp+=75
    t.sleep(1)
    print("You pry the mask off of Blarney's head.")
    t.sleep(2)
    print("Dark energy flies everywhere.")
    t.sleep(2)
    print("You got an ancient skull!")
    cl.Player.skulls+=1
    t.sleep(2)
    print('Your Magic and Defence stat went up by 1!')
    cl.Player.mp +=1
    cl.Player.deff +=1
    save.save_game()
    t.sleep(2)
    input('[Game Saved! Press enter to continue.]')
    torch.island()

def fight():
    global q, player, monster
    load.load_game()
    player=cl.Player()
    monster=cl.Blarney()
    while True:
        if player.hp < 1:                                                                                                                                                                            
            print(c.yellow+"You Died!")                                                                                                                                                                       
            t.sleep(1)                                                                                                                                                                               
            ter=input("Do you want to keep playing, or quit? (1), (2)"+c.reset+" >>>"+c.violet).strip()                                                                                          
            if ter == '1':                                                                                                                                                                           
                torch.island()                                                                                                                                                                                
            elif ter == '2':                                                                                                                                                                         
                exit()                                                                                                                                                                               
            else:                                                                                                                                                                                    
                break                                                                                                                                                                                
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
    cl.Foe=cl.Blarney
    fight()
