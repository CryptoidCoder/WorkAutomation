#imports
import os #to interface with the os
from github import Github #for accessing github
from dotenv import load_dotenv #for accessing the .env file
import sys, getopt #for arguments
import shutil #for copying files
from distutils.dir_util import copy_tree #copying folder contents

# Init
load_dotenv() #activate the access to the .env

git_token = os.getenv('Github_Token')
git_user = os.getenv('Github_Username')


Python_Model_Path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Models\\Python\\")# add \Models\Python\ to this files path
Heroku_Model_Path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Models\\Heroku\\")# add \Models\Heroku\ to this files path
Other_Model_Path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Models\\Other\\")# add \Models\Other\ to this files path

thisdir = os.path.dirname(os.path.realpath(__file__))

#init()
def init():
    print("Inititalizing...\n")
    global language, branchname, reponame
    reponame = getfoldername()
    language, branchname = getargs(sys.argv[1:])
    addnewline('current.temp', f'reponame = {reponame}')
    addnewline('current.temp', f'branchname = {branchname}')
    addnewline('current.temp', f'language = {language}')


#end()
def end():
    print("\nEnding - deleting 'current.temp' file\n")
    os.remove('current.temp')

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

# git_token, git_user, License_type, commit_message, language, branchname = getdefaults()
def getdefaults():
    Github_Token = os.getenv('Github_Token')
    Github_Username = os.getenv('Github_Username')
    License = os.getenv('License')
    default_commit_message = os.getenv('default_commit_message')
    default_language = os.getenv('default_language')
    default_branchname = os.getenv('default_branchname')

    return Github_Token, Github_Username, License, default_commit_message, default_language, default_branchname

#getfoldername()
def getfoldername(): #return the foldername of whatever directory your in
    current_path = os.getcwd()
    current_folder = os.path.basename(current_path)
    return current_folder

#makerepo()
def makerepo():
    print(f"\nMaking new repo on github: {reponame}\n")
    user = Github(git_token).get_user()
    login = user.login
    repo = user.create_repo(reponame)

#newbranch() - will create a new branch
def newbranch():
    print(f"\nMaking New branch: {branchname}\n")
    os.system('git init')
    os.system(f'git checkout --orphan {branchname}')
    os.system('git commit --allow-empty -m "Root Commit"')
    os.system(f'git remote add origin https://github.com/{git_user}/{reponame}.git')
    os.system(f'git push origin {branchname}')

#initialcommit() - will run the first commit & push
def initialcommit():
    print(f"\nInitial commit\n")
    os.system('git add --all')
    os.system('git commit -m "Initial Commit"')
    os.system(f'git push --set-upstream origin {branchname}')

#largefiles('.exe') to make all .exe files managed by git lfs
def largefiles(filetype):
    print(f"\nSet Github LFS for: {filetype}\n")
    os.system(f'git lfs track "{filetype}"')
    os.system('git add .gitattributes')
    os.system(f'git commit -m "Using LFS For {filetype} Files"')



def addfiles():
    if language == 'python':
        #venv/
        if os.path.isdir('venv'):
            print("Venv already exists.")
        else:
            print("\nCreating venv\n")
            os.system("python -m venv venv")

        #LICENSE
        if os.path.exists('LICENSE'):
            print("LICENSE already exists.")
        else:
            print("\nCreating LICENSE\n")
            filepath = str(Python_Model_Path) + '\\' + 'LICENSE'
            shutil.copyfile(filepath, 'LICENSE')

        #README.md
        if os.path.exists('README.md'):
            print("\nREADME.md Already Exists\n")
        else:
            print("\nCreating README.md\n")
            filepath = str(Python_Model_Path) + '\\' + 'README.md'
            shutil.copyfile(filepath, 'README.md')

        #.gitignore
        if os.path.exists('.gitignore'):
            print("\n.gitignore Already Exists\n")
        else:
            print("\nCreating .gitignore\n")
            filepath = str(Python_Model_Path) + '\\' + '.gitignore'
            shutil.copyfile(filepath, '.gitignore')

        #commit.txt
        if os.path.exists('commit.txt'):
            print("\ncommit.txt Already Exists\n")
        else:
            print("\nCreating commit.txt\n")
            filepath = str(Python_Model_Path) + '\\' + 'commit.txt'
            shutil.copyfile(filepath, 'commit.txt')

        #.vscode
        if os.path.isdir('.vscode'):
            print("\n.vscode Already Exists\n")
        else:
            print("\nCreating .vscode\n")
            filepath = str(Python_Model_Path) + '\\' + '.vscode'
            copy_tree(filepath, '.vscode')

    else:
        #LICENSE
        if os.path.exists('LICENSE'):
            print("LICENSE already exists.")
        else:
            print("\nCreating LICENSE\n")
            filepath = str(Other_Model_Path) + '\\' + 'LICENSE'
            shutil.copyfile(filepath, 'LICENSE')

        #README.md
        if os.path.exists('README.md'):
            print("\nREADME.md Already Exists\n")
        else:
            print("\nCreating README.md\n")
            filepath = str(Other_Model_Path) + '\\' + 'README.md'
            shutil.copyfile(filepath, 'README.md')

        #.gitignore
        if os.path.exists('.gitignore'):
            print("\n.gitignore Already Exists\n")
        else:
            print("\nCreating .gitignore\n")
            filepath = str(Other_Model_Path) + '\\' + '.gitignore'
            shutil.copyfile(filepath, '.gitignore')

        #commit.txt
        if os.path.exists('commit.txt'):
            print("\ncommit.txt Already Exists\n")
        else:
            print("\nCreating commit.txt\n")
            filepath = str(Other_Model_Path) + '\\' + 'commit.txt'
            shutil.copyfile(filepath, 'commit.txt')

        #.vscode
        if os.path.isdir('.vscode'):
            print("\n.vscode Already Exists\n")
        else:
            print("\nCreating .vscode\n")
            filepath = str(Other_Model_Path) + '\\' + '.vscode'
            copy_tree(filepath, '.vscode')
            

#getargs(sys.argv[1:])
def getargs(argv):
    language = ''
    branchname = ''
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["language=", "branchname="]) #see if any arguments exit
    except:
        print("Syntax Is: --language <language> --branchname <branchname>") #state syntax if no args found
        sys.exit(2) #exit if none found

    for opt,arg in opts:
        opt = opt.lower() #change the case to lower

        if opt == '-h':
            print("Syntax Is: --language <language> --branchname <branchname>") #state syntax
            sys.exit()
        elif opt in ("-lang", "--language"): #if -lang OR --language tag is present then save the following arg as 'language' variable
            language = arg
        elif opt in ("-branch", "--branchname"): #if -branch OR --branchname is present then save the following arg as 'branchname' variable
            branchname = arg

    Github_Token, Github_Username, default_license_type, default_commit_message, default_language, default_branchname = getdefaults()

    
    if language == '': #if no language given then set as default
        language = default_language
    if branchname == '': #if no branchname given then set as default
        branchname = default_branchname

    return language, branchname


