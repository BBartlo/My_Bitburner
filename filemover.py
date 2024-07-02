import shutil as sh
import os
import time

files = []
folders = []

destinationdir = input('Destination Directory: ').replace('\\', '/')

if destinationdir[-1] == '/': destinationdir = destinationdir[:-1]

path = os.path.dirname(__file__).replace('\\', '/')
path = path + '/' + os.listdir(path)[-1] 
start = os.listdir(path)

while True:
    while True:
        for item in start:
            if '.' in item: 
                files.append([str(path + '/' + item), str(destinationdir + '/' + item)])
            elif '.' not in item:
                folders.append(str(destinationdir + '/' + item))
                for item2 in os.listdir(path + '/' + item):
                    start.append(item + '/' + item2)
        break

    for item in folders:
        try:
            os.mkdir(item)
        except:
            FileExistsError

    for item in files:
        source = open(item[0], 'r', encoding='utf8')
        try:
            destination = open(item[1], 'r', encoding='utf8')
        except:
            FileNotFoundError
        
        try:
            if source.read() != destination.read(): 
                sh.copy(item[0], item[1])
        except NameError:
            sh.copy(item[0], item[1])
            
    time.sleep(1)