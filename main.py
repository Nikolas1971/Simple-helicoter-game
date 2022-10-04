# 🌲 🌊 🚁 💦 🔥 🏥 ❤️ 🪣 🏪 🌦️ ⚡️ 🏆🌩️
from clouds import Clouds
import map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard
import json

tick = 1
TICK_SLEEP = 0.01
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_W, MAP_H = 20, 10

helico = Helico(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
tmp = map.Map (MAP_W, MAP_H)

tmp.print_map(helico, clouds)


MOVES = {'w' : (-1,0),
         'd' : (0, 1),
         's' : (1, 0),
         'a' : (0, -1)}
# f - save, g - restore

def process_key(key):
    global helico, tick, clouds, tmp
    c = key.char.lower()
    
    # Move helicoter
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move (dx, dy)
    
    # Save game progress
    elif c == 'f':
        data = {'helicopter' : helico.export_data(),
                'clouds' : clouds.export_data(),
                'field' : tmp.export_data(),
                'tick' : tick}
        with open('level.json', 'w') as lvl:
            json.dump (data, lvl)
    
    # Load game progress
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load (lvl)
            helico.import_data(data['helicopter'])
            tick = data['tick'] or 0
            tmp.import_data(data['field'])
            clouds.import_data(data['clouds'])
            

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()



while True:
    os.system('clear')
    
    tmp.process_helicopter(helico, clouds)
    helico.print_stats()
    tmp.print_map(helico, clouds)
    print ('TICK', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        tmp.generate_tree()
    if tick % FIRE_UPDATE == 0:
        tmp.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update_clouds()

