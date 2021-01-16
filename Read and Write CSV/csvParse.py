fileNameRead = "data.csv"
fileRead = open(fileNameRead, 'r')

header = fileRead.readline().rstrip('\n')
headerList = header.split(',')

print(headerList)

lineList = []

ind = 0
for line in fileRead:
    lineList.append([])
    lineList[ind] = line.rstrip('\n').split(',')
    ind+=1

print(lineList)

fileNameWrite = 'writeData.csv'
fileWrite = open(fileNameWrite, 'w')

headerList.append('Temperature (C)')
headerList.append('Pressure (ATM)')

tempFIndex = headerList.index('Temperature (F)')
pressurePSIIndex = headerList.index('Pressure (PSI)')

def listToString(listName):
    delimeter = ','
    return delimeter.join(listName) + '\n'

fileWrite.write(listToString(headerList))

for x in range(0,len(lineList)):
    tempF = float(lineList[x][tempFIndex])
    tempC = str((tempF - 32)*5/9)
    lineList[x].append(tempC)

    pressurePSI = float(lineList[x][pressurePSIIndex])
    pressureATM = str(pressurePSI * 0.068046)
    lineList[x].append(pressureATM)

    fileWrite.write(listToString(lineList[x]))

