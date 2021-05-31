import UpgradeFunctions
import sys, os

#os.chdir(os.getcwd())
#reponame = UpgradeFunctions.getfoldername() #the reponame is the name of the current folder
language, branchname = UpgradeFunctions.getargs(sys.argv[1:])


UpgradeFunctions.init()
UpgradeFunctions.makerepo()
UpgradeFunctions.newbranch()
UpgradeFunctions.addfiles()
UpgradeFunctions.largefiles('.exe')
UpgradeFunctions.initialcommit()

UpgradeFunctions.end()