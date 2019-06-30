class Country:
    def __init__(self, entry):
        self.Country = entry.Country
        self.Status = entry.Status
        self.Life_Expectancy = "na"
        self.Adult_Mortality = "na"
        self.Infant_Deaths = "na"
        self.Alcohol = "na"
        self.PercentageExpenditure = "na"
        self.Hepatitis_B = "na"
        self.Measles = "na"
        self.BMI = "na"
        self.Under_Five_Deaths = "na"
        self.Polio = "na"
        self.TotalExpenditure = "na"
        self.Diphtheria = "na"
        self.HIV_AIDS = "na"
        self.GDP = "na"
        self.Population = "na"
        self.Thinness_1_19_Years = "na"
        self.Thinness_5_9_Years = "na"
        self.Income_Composition_Of_Resources = "na"
        self.Schooling = "na"
    def getCsvLine(self):
        return ",".join([
            self.Country,
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