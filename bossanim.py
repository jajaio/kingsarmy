import time as t
import colors as c

blarney1='''
             ,      ,   
            /(.-""-.)\\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \\
           \,___/\___,/
         ___\ \|--|/ /___
       /`    \      /    `\\
      /       '----'       \\

'''

blarney2='''
             ,      ,   
            /(.-""-.)\\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \\
           \,___/\___,/
         ___\ \|uu|/ /___
       /`    \ .--. /    `\\
      /       '----'       \\
'''

kingskull='''
                                            .""--.._
                                           []      `'--.._
                                           ||__           `'-,
                                         `)||_ ```'--..       \\
                     _                    /|//}        ``--._  |
                  .'` `'.                /////}              `\/
                 /  .""".\              //{///    
                /  /_  _`\\\           // `||
                | |(_)(_)||          _//   ||
                | |  /\  )|        _///\   ||
                | |L====J |       / |/ |   ||
               /  /'-..-' /    .'`  \  |   ||
              /   |  :: | |_.-`      |  \  ||
             /|   `\-::.| |          \   | ||
           /` `|   /    | |          |   / ||
         |`    \   |    / /          \  |  ||
        |       `\_|    |/      ,.__. \ |  ||
        /                     /`    `\ ||  ||
       |           .         /        \||  ||
       |                     |         |/  ||
       /         /           |         (   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \ `-._       |           /              ||
    \ ,//`\    /`           |              ||
     ///\  \  |             \              ||
    |||| ) |__/             |              ||
    |||| `.(                |              ||
    `\\` /`                 /              ||
       /`                   /              ||
      /                     |              ||
     |                      \              ||
    /                        |             ||
  /`                          \            ||
/`                            |            ||
`-.___,-.      .-.        ___,'            ||
         `---'`   `'----'`
'''
def kingattanim():
    for count in range(2):
        print(c.clear)
        print(c.red+kingskull)
        t.sleep(.25)
        print(c.clear)
        print(c.yellow+kingskull)
        t.sleep(.25)
        print(c.clear)

def blarneyattanim():
    for count in range(2):
        print(c.clear)
        print(c.red+blarney1)
        t.sleep(.5)
        print(c.clear)
        print(blarney2)
        t.sleep(.5)
        print(c.clear)
        
        
if __name__=='__main__':
    blarneyattanim()
