import classes as cl
import json
author="jajaio"
def load_game():
    with open('player.json', 'r') as pfile:
        j=json.load(pfile)
        cl.Player.hp=j['hp']
        cl.Player.agi=j['agi']
        cl.Player.deff=j['deff']
        cl.Player.att=j['att']
        cl.Player.mp=j['mp']
        cl.Player.xp=j['xp']
        cl.Player.name=j['name']
        cl.Player.lvl=j['lvl']
        cl.Player.dragon=j['dragon']
if __name__=='__main__':
    load_game()
    cl.show_player()
