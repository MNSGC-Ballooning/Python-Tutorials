fileName = "sensitiveInfo.txt" # name of file containing usernames, passwords, etc.
delimeter = '=' 

file = open(fileName, 'r') # open file for reading

def findValue(fullString):
    fullString = fullString.rstrip('\n')
    value = fullString[fullString.index(delimeter)+1:]
    value = value.replace(" ", "")
    return value

for line in file: # read file line by line
    if line.startswith('username'):
        username = findValue(line)
    if line.startswith('password'):
        password = findValue(line)

# Now we have our information as variables, but they do not appear in the file
# So, if we push files to github, we can leave sensitiveInfo.txt out of the commit

print("username:_" + username + "_")
print("password:_" + password + "_")