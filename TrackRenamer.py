# © Georgy Perepechko, 2017

import os
import unicodedata
from shutil import copy2

def genNewName():
    for number in range (1,100):
        newname='track' + str(number).zfill(3) + '.mp3'
        if newname not in os.listdir():
            return newname
            
def genPlaylist():
        if 'playlist.txt' in os.listdir():
            myfile = open("playlist.txt","r+")
            spl = sorted(myfile.readlines())
            myfile.seek(0)
            for song in spl:
                if song[:12] in os.listdir():
                    myfile.write('\n' + song)
            myfile.truncate()
            myfile.close() 
            return spl 

if __name__ == '__main__':
    if not os.path.exists(os.path.join('.', 'original_mp3s')):
        os.mkdir(os.path.join('.', 'original_mp3s'))
    spl=genPlaylist()
    for filename in os.listdir():
        if filename.endswith('.mp3'):
            if (filename.startswith('track0')!=True) or (len(filename)!=12) or (filename=='track000.mp3'):
                copy2(filename, os.path.join('.', 'original_mp3s', filename))
                newname=genNewName()
                os.rename(filename,newname)
                try:
                    with open("playlist.txt", "a") as myfile:
                        myfile.write("\n" + newname + " - " + filename)
                except UnicodeEncodeError:
                    with open("playlist.txt", "a") as myfile:
                        filename=str(unicodedata.normalize('NFKD', filename).encode('ascii','ignore'))[2:-1]
                        myfile.write("\n" + newname + " - " + filename)
            elif (filename not in str(spl)):
                copy2(filename, os.path.join('.', 'original_mp3s', filename))
                with open("playlist.txt", "a") as myfile:
                    myfile.write("\n" + filename + " - неизвестно; номер задан пользователем | unknown; number assigned by user")

    genPlaylist()
    genPlaylist()