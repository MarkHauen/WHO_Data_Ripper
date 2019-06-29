from IOTools import getDataHeaders, getDataLines, writeDataLines
from Entry import Entry

rawData = [Entry(line) for line in getDataLines("LifeExpectancyDataRAW")]

# Fixing France and Finland to Developed Countries
for entry in rawData:
    if (("France" in entry.Country) | ("Finland" in entry.Country)):
        entry.Country = "Developed"

cleanData = "".join([entry.getCsvLine() for entry in rawData])

writeDataLines("LifeExpectancyDataCLEANED", cleanData)

