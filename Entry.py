class Entry:
    def __init__(self, line):
        self.Country = getEntry(line, 0)
        self.Year = getEntry(line, 1)
        self.Status = getEntry(line, 2)
        self.Life_Expectancy = getEntry(line, 3)
        self.Adult_Mortality = getEntry(line, 4)
        self.Infant_Deaths = getEntry(line, 5)
        self.Alcohol = getEntry(line, 6)
        self.PercentageExpenditure = getEntry(line, 7)
        self.Hepatitis_B = getEntry(line, 8)
        self.Measles = getEntry(line, 9)
        self.BMI = getEntry(line, 10)
        self.Under_Five_Deaths = getEntry(line, 11)
        self.Polio = getEntry(line, 12)
        self.TotalExpenditure = getEntry(line, 13)
        self.Diphtheria = getEntry(line, 14)
        self.HIV_AIDS = getEntry(line, 15)
        self.GDP = getEntry(line, 16)
        self.Population = getEntry(line, 17)
        self.Thinness_1_19_Years = getEntry(line, 18)
        self.Thinness_5_9_Years = getEntry(line, 19)
        self.Income_Composition_Of_Resources = getEntry(line, 20)
        self.Schooling = getEntry(line, 21)
    def getCsvLine(self):
        return ",".join([
            self.Country,
            str(self.Year),
            self.Status,
            str(self.Life_Expectancy),
            str(self.Adult_Mortality),
            str(self.Infant_Deaths),
            str(self.Alcohol),
            str(self.PercentageExpenditure),
            str(self.Hepatitis_B),
            str(self.Measles),
            str(self.BMI),
            str(self.Under_Five_Deaths),
            str(self.Polio),
            str(self.TotalExpenditure),
            str(self.Diphtheria),
            str(self.HIV_AIDS),
            str(self.GDP),
            str(self.Population),
            str(self.Thinness_1_19_Years),
            str(self.Thinness_5_9_Years),
            str(self.Income_Composition_Of_Resources),
            str(self.Schooling)
            ])


def isNotEmpty(entry):
    return len(entry) > 0

def actualType(entry):
    try:
        return float(entry)
    except ValueError:
        return entry

def getEntry(line, index):
    entry = line.split(",")[index].replace("\n", "").replace("\r", "")
    return actualType(entry) if isNotEmpty(entry) else 'na'

