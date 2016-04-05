import time as t
import colors as c

blarney1='''


'''
kingskull='''
                                            .""--.._
                                           []      `'--.._
                                           ||__           `'-,
                                         `)||_ ```'--..       \
                     _                    /|//}        ``--._  |
                  .'` `'.                /////}              `\/
                 /  .""".\              //{///    
                /  /_  _`\\            // `||
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
        print(c.red+foeatt1)
        t.sleep(.25)
        print(c.clear)
        print(foeatt2)
        t.sleep(.25)
        print(c.clear)
        
        
if __name__=='__main__':
    kingattanim()
