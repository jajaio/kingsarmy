import json
import classes as cl
author="jajaio"

def save_game():
	with open('player.json', 'w') as pfile:
		pfile.write(json.dumps({
            "hp":cl.Player.hp,
            "agi":cl.Player.agi,
            "deff":cl.Player.deff,
            "att":cl.Player.att,
            "mp":cl.Player.mp,
            "xp":cl.Player.xp,
            "name":cl.Player.name,
            "lvl":cl.Player.lvl,
            "dragon":cl.Player.dragon
            }))
        
if __name__=='__main__':
    save_game()
