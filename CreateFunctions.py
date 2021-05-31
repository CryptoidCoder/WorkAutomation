#imports
import os #to interface with the os
from github import Github #for accessing github
from dotenv import load_dotenv #for accessing the .env file
from distutils.dir_util import copy_tree #copying folder contents
import sys, getopt #for arguments

# Init
load_dotenv() #activate the access to the .env

git_token = os.getenv('Github_Token')
git_user = os.getenv('Github_Username')

Python_Model_Path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Models\\Python\\")# add \Models\Python\ to this files path
Heroku_Model_Path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Models\\Heroku\\")# add \Models\Heroku\ to this files path
Other_Model_Path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Models\\Other\\")# add \Models\Other\ to this files path

thisdir = os.path.dirname(os.path.realpath(__file__))
currentdir = os.getcwd()


# git_token, git_user, License_type, commit_message, language, branchname = getdefaults()
def getdefaults():
    Github_Token = os.getenv('Github_Token')
    Github_Username = os.getenv('Github_Username')
    License = os.getenv('License')
    default_commit_message = os.getenv('default_commit_message')
    default_language = os.getenv('default_language')
    default_branchname = os.getenv('default_branchname')

    return Github_Token, Github_Username, License, default_commit_message, default_language, default_branchname

#getargs() - will get the command line arguments and create a current.temp file with them in [if not passed will set as defaults]
#this needs to get the arguments for reponame, language, branchname
def getargs(argv):
    language = ''
    branchname = ''
    reponame = ''
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["language=", "branchname=", "reponame="]) #see if any arguments exit
    except:
        print("Syntax Is: --language <language> --branchname <branchname> --reponame <reponame>") #state syntax if no args found
        sys.exit(2) #exit if none found

    for opt,arg in opts:
        opt = opt.lower() #change the case to lower

        if opt == '-h':
            print("Syntax Is: --language <language> --branchname <branchname> --reponame <reponame>") #state syntax
            sys.exit()
        elif opt in ("-lang", "--language"): #if -lang OR --language tag is present then save the following arg as 'language' variable
            language = arg
        elif opt in ("-branch", "--branchname"): #if -branch OR --branchname is present then save the following arg as 'branchname' variable
            branchname = arg
        elif opt in ("-repo", "--reponame"): #if -repo OR --reponame is present then save the following arg as 'rpeoname' variable
            reponame = arg

    Github_Token, Github_Username, default_license_type, default_commit_message, default_language, default_branchname = getdefaults()

    if reponame == '': #if no reponame given then set as default
        print("\nNo Reponame was given - exiting\n")
        sys.exit()
    if language == '': #if no language given then set as default
        language = default_language
    if branchname == '': #if no branchname given then set as default
        branchname = default_branchname

    return reponame, language, branchname

def addnewline(filename,text): #append text to a new line on a file
    # Open the file in append & read mode ('a+')
    with open(filename, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text)
        file_object.close()


##Create Stuff:

#init()
def init():
    print("Inititalizing...\n")
    global reponame, language, branchname, targetdir
    reponame, language, branchname = getargs(sys.argv[1:])
    targetdir = os.path.join(currentdir, reponame)
    targetdir = targetdir+'\\'
    print(targetdir)
    os.chdir(thisdir)
    addnewline('current.temp', f'reponame = {reponame}')
    addnewline('current.temp', f'branchname = {branchname}')
    addnewline('current.temp', f'language = {language}')
    addnewline('current.temp', f'targetdir = {targetdir}')

#end()
def end():
    os.chdir(thisdir)
    print("\nEnding - deleting 'current.temp' file\n")
    os.remove('current.temp')

#makerepo()
def makerepo():
    os.chdir(targetdir)
    print(f"\nMaking new repo on github: {reponame}\n")
    user = Github(git_token).get_user()
    login = user.login
    repo = user.create_repo(reponame)

#newbranch() - will create a new branch
def newbranch():
    os.chdir(targetdir)
    print(f"\nMaking New branch: {branchname}\n")
    os.system('git init')
    os.system(f'git checkout --orphan {branchname}')
    os.system('git commit --allow-empty -m "Root Commit"')
    os.system(f'git remote add origin https://github.com/{git_user}/{reponame}.git')
    os.system(f'git push origin {branchname}')

#initialcommit() - will run the first commit & push
def initialcommit():
    os.chdir(targetdir)
    print(f"\nInitial commit\n")
    os.system('git add --all')
    os.system('git commit -m "Initial Commit"')
    os.system(f'git push --set-upstream origin {branchname}')

#largefiles('.exe') to make all .exe files managed by git lfs
def largefiles(filetype):
    os.chdir(targetdir)
    print(f"\nSet Github LFS for: {filetype}\n")
    os.system(f'git lfs track "{filetype}"')
    os.system('git add .gitattributes')
    os.system(f'git commit -m "Using LFS For {filetype} Files"')

#foldercreate
def foldercreate():
    print(f"\nCreated Local folder: {targetdir}\ \n")
    os.mkdir(f'{targetdir}')
    os.chdir(targetdir)

def addfiles():
    os.chdir(targetdir)
    print(f"\nAdding files for: {language}\n")
    if language == 'python': #if the chosen language is python; create a venv, make a requirements.txt, add a line ot the TODO, Copy model files in
        os.chdir(targetdir) #move to the new directory
        print("\nMaking Venv...\n") #print message
        os.system('python -m venv venv') #create a virtual environment called 'venv'
        print("Venv Made\n") #print message
        os.system('venv\Scripts\pip.exe freeze >> requirements.txt') #make a requirements.txt using the venv pip
        addnewline('TODO','Need to un # venv in .gitignore if you want to upload the virtual environment to github')
        copy_tree(Python_Model_Path, targetdir) #move the model files into the new dir

    #elif language == 'heroku':
        #os.chdir(targetdir) #move to the new directory
        #copy_tree(Heroku_Model_Path, targetdir) #move the model files into the new dir

    else:
        os.chdir(targetdir) #move to the new directory
        addnewline('TODO', 'This Is The TODO File.')
        copy_tree(Other_Model_Path, targetdir) #move the model files into the new dir

