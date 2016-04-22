import time as t
import colors as c

author='jajaio'

def normal():
    print(c.reset)
    print(c.clear)
    print('.')
    t.sleep(.5)
    print(c.clear)
    print('..')
    t.sleep(.5)
    print(c.clear)
    print('...')
    t.sleep(.5)
    print(c.clear)

def slow():
    print(c.reset)
    print(c.clear)
    print('.')
    t.sleep(2)
    print('..')
    t.sleep(2)
    print(c.clear)
    print('...')
    t.sleep(2)
    print(c.clear)
if __name__=='__main__':
    print('Normal Speed')
    normal()
    print('Slow Speed')
    slow()
