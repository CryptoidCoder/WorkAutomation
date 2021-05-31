#setup.py
'''

You run this to create a .env file with all the defualt values in it.

'''

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

print("This is the setup script:")
print("Please enter the appropriate values when prompted.")

print("Go to https://github.com/settings/tokens and Click `Generate Token` to createa token for this app.")
print("Make sure to select the 'repo' options\n")
github_token = input("What Is Your Github Token? \n > ")
github_user = input("What Is Your Github Username? \n > ")

print(" ")
print(" ")

print("What LICENSE do you want to use: ")

print("GNU Affero General Public License v3.0 - Enter 1")
print("MIT License - Enter 2")
license_type = input(" > ")
if license_type == '1':
    license_type = 'GNU Affero General Public License v3.0'
elif license_type == '2':
    license_type = 'MIT License'
else:
    print(f"custom license type: {license_type}")


print(" ")
print(" ")

print("Now to define the default values: ")
default_commit_message = input("What is the default commit message? \n > ")
default_language = input("What is the default language (python, heroku, other)? \n > ")
default_branchname = input("What is the default branch name? \n > ")


addnewline('.env', f"license = '{license_type}'")

addnewline('.env', f"default_commit_message = '{default_commit_message}'")
addnewline('.env', f"default_language = '{default_language}'")
addnewline('.env', f"default_branchname = '{default_branchname}'")

addnewline('.env', f"Github_Token = '{github_token}'")
addnewline('.env', f"Github_Username = '{github_user}'")

