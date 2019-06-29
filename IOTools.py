from os import path

def getRoot():
    return path.dirname(path.realpath(__file__))

def getDataPath(fileName):
    return "{r}\\{fn}.csv".format(r=getRoot(), fn=fileName)

def getFileLines(fileName):
    with open(getDataPath(fileName), mode='rt') as reader:
        return reader.readlines()

def getDataHeaders(fileName):
    return getFileLines(fileName)[0]

def getDataLines(fileName):
    return getFileLines(fileName)[1:]

def writeDataLines(fileName, dataLines):
	with open("{r}\\{fn}.csv".format(r=getRoot(), fn=fileName), mode='wt') as writer:
		writer.write(dataLines)