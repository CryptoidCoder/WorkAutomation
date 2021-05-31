import os
import sys, getopt #for arguments
###updating:

#getargs() - will get the command line arguments and create a current.temp file with them in [if not passed will set as defaults]
#this needs to get the arguments for reponame, language, branchname
def getargs(argv):
    steps = ''
    custom = ''
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["steps=", "custom="]) #see if any arguments exit
    except:
        print("Syntax Is: --steps <steps[big/small]>") #state syntax if no args found
        sys.exit(2) #exit if none found

    for opt,arg in opts:
        opt = opt.lower() #change the case to lower

        if opt == '-h':
            print("Syntax Is: --steps <steps[big/small]>") #state syntax
            sys.exit()
        elif opt in ("-steps", "--steps"): #if -steps OR --steps tag is present then save the following arg as 'steps' variable
            steps = arg
        elif opt in ("-custom", "--custom"): #if -custom OR --custom is present then save the following arg as 'custom' variable
            custom = arg


    if steps == '': #if no steps given then set as default
        steps = 'big'
    if custom == '': #if no custom message given then set as default
        custom = None

    return steps, custom

#get the last commit message
def getcommitnumber():
    try:
        f = open("commit.txt")
        commitnumber = f.read()
        f.close()
    except:
        print("No commit.txt present creating one")
        os.system('echo 1.0 > commit.txt')
        commitnumber = '1.0'
    #print(f"Previous Commit Message: Updates {commitnumber}")

    return commitnumber

#update the commit number
def changecommitnumber(type):
    prevcommitnumber = getcommitnumber()

    #if type is small add 0.1 to the number
    if type == 's' or type == 'small':
        nextcommitnumber = float(prevcommitnumber) + 0.1
        os.system(f"echo {str(nextcommitnumber)} > commit.txt")

    #if type is big add 1.0 to the number
    elif type == 'b' or type == 'big':
        nextcommitnumber = float(prevcommitnumber) + 1.0
        os.system(f"echo {str(nextcommitnumber)} > commit.txt")

    #print(f"Steps: {type}")


#update()
def update(message):
    os.system('git add --all')
    os.system(f'git commit -m "{message}"')
    os.system('git push')

