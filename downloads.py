#this is a script to download all of te latest releases of certain programs / files


#imports
import selenium #to automate chrome
import requests #to download direct files
import os #to interface with the os
import linecache #to find a certain line number
import time #to access time

mode = 'latest'

def openchrome():
    print("Opeining Chrome...")

def urldirectdownload(fileurl): #if the program has a latest.xyz file then wget it
    myfile = requests.get(fileurl, allow_redirects=True)
    #program = f"'{program}'"
    open(f"{program}.exe", 'wb').write(myfile.content)
    

def githubclone(path): #to git clone something
    os.system(f'git clone git@github:{path}')

def gotoline(line, file):
    line = linecache.getline(file, int(line))
    return line

def lookup(mode,program): #get the url for the downloads page
    #print("finding program url")
    if mode == 'offline':

        file = open("softwaredownloadlocations.txt", 'r')
        flag,linenum = 0,0
        for line in file:
            linenum += 1
            if program in line:
                flag = 1
                break

        if flag == 0:
            print('String "', program , '" Not Found')
        else:
            print('String "', program, '" Found in Line', linenum)
            line = gotoline(linenum, "softwaredownloadlocations.txt")
            location = line.replace(f"{program} = ", '')
            print(location)

            if 'git://' in location or 'github.com/' in location:
                try:
                    location = location.replace('git://', '')
                except:
                    try:
                        location = location.replace('https://', '')
                    except:
                        try:
                            location = location.replace('http://', '')
                        except:
                            print("There is no identifier (git://, https://, http://)")
                githubclone(location)

            elif 'https://' in location or 'http://' in location:
                urldirectdownload(location)


    else:
        print(f"mode {mode} not available")
#Main:
softwarelist = ['spotify', 'discord', 'winget']
for program in softwarelist:
    lookup('offline', program)
    #lookup('online', program)

