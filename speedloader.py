import requests
import os
import shutil

user = os.environ.get('USERNAME')

info = '''
Use   load packname   to load a modpack into your mods folder
Use   import packcontent   to create a new modpack
'''
print(info)

def create():
    #   Makes mods folder if there isn't one
    try:
        os.mkdir(f"C:/Users/{user}/AppData/Roaming/.minecraft/mods")
    except:
        pass

    #   Make mod-switcher folder if not there
    try:
        os.mkdir(f"C:/Users/{user}/AppData/Roaming/.minecraft/mod-switcher")
    except:
        pass

    #   Make mod pack folder
    try:
        os.mkdir(f"C:/Users/{user}/AppData/Roaming/.minecraft/mod-switcher/packs")
    except:
        pass


create()


def load(pack):
    dir = f'C:/Users/{user}/AppData/Roaming/.minecraft/mods'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    pack = f'{pack}.txt'
    test = open(f'C:/Users/{user}/AppData/Roaming/.minecraft/mod-switcher/packs/{pack}').read()
    test = test.split(';')
    nameC = len(test) - 1
    urlC = len(test) - 2
    open(f'C:/Users/{user}/AppData/Roaming/.minecraft/mod-switcher/packs/{pack}').close()
    while urlC > 0:
        FILENAME = test[nameC]
        response = requests.get(test[urlC])
        open(f'C:/Users/{user}/AppData/Roaming/.minecraft/mods/{FILENAME}', "wb").write(response.content)
        open(f'C:/Users/{user}/AppData/Roaming/.minecraft/mods/{FILENAME}').close()
        urlC = urlC - 2
        nameC = nameC - 2


#  loop for command line  
x = 1
while x == 1:
    userI = input(f'Command: ')
    if userI.startswith('load '):
        userI = userI[5:]
        load(userI)
    if userI == 'exit' or userI == 'stop':
        exit()
    if userI.startswith('import '):
        userI = userI[7:]
        userI1 = userI.split(';')
        open(f'C:/Users/{user}/AppData/Roaming/.minecraft/mod-switcher/packs/{userI1[0]}.txt', "w").write(userI)
