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
             self.Year,
             self.Status,
             self.Life_Expectancy,
             self.Adult_Mortality,
             self.Infant_Deaths,
             self.Alcohol,
             self.PercentageExpenditure,
             self.Hepatitis_B,
             self.Measles,
             self.BMI,
             self.Under_Five_Deaths,
             self.Polio,
             self.TotalExpenditure,
             self.Diphtheria,
             self.HIV_AIDS,
             self.GDP,
             self.Population,
             self.Thinness_1_19_Years,
             self.Thinness_5_9_Years,
             self.Income_Composition_Of_Resources,
             self.Schooling
             ])

def getEntry(line, index):
    entry = line.split(",")[index]
    return entry if len(entry) > 0 else 'NA'