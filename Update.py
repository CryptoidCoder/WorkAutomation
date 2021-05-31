import UpdateFunctions
import sys

steps, custom = UpdateFunctions.getargs(sys.argv[1:])
if custom != None: #if there is a custom message:
    UpdateFunctions.update(custom) #commit using a custom message

else:
    UpdateFunctions.changecommitnumber(steps) #change the commit name [the file is currently the previous one - we need to make it the current one]
    stepsmessage = f"Updates {UpdateFunctions.getcommitnumber()}" #Updates {Numbers.Decimals} e.g. Updates 1.0
    UpdateFunctions.update(stepsmessage) #update using the 'Updates {Numbers.Decimals}'