from IOTools import getFileLines, getDataLines, writeDataLines
from Entry import Entry
from Country import Country
from statistics import mean, StatisticsError
from numbers import Number

rawData = [Entry(line) for line in getDataLines("LifeExpectancyDataRAW")]
countries = {}

for entry in rawData:
    if (("France" in entry.Country) | ("Finland" in entry.Country)):
        entry.Status = "Developed"
    countries[entry.Country] = Country(entry)

for country in countries.values():
    try:
        country.Life_Expectancy = mean([x.Life_Expectancy for x in list(filter(lambda y : isinstance(y.Life_Expectancy, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Life_Expectancy = "na"
    try:
        country.Adult_Mortality = mean([x.Adult_Mortality for x in list(filter(lambda y : isinstance(y.Adult_Mortality, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Adult_Mortality = "na"
    try:
        country.Infant_Deaths = mean([x.Infant_Deaths for x in list(filter(lambda y : isinstance(y.Infant_Deaths, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Infant_Deaths = "na"
    try:
        country.Alcohol = mean([x.Alcohol for x in list(filter(lambda y : isinstance(y.Alcohol, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Alcohol = "na"
    try:
        country.PercentageExpenditure = mean([x.PercentageExpenditure for x in list(filter(lambda y : isinstance(y.PercentageExpenditure, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.PercentageExpenditure = "na"
    try:
        country.Hepatitis_B = mean([x.Hepatitis_B for x in list(filter(lambda y : isinstance(y.Hepatitis_B, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Hepatitis_B = "na"
    try:
        country.Measles = mean([x.Measles for x in list(filter(lambda y : isinstance(y.Measles, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Measles = "na"
    try:
        country.BMI = mean([x.BMI for x in list(filter(lambda y : isinstance(y.BMI, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.BMI = "na"
    try:
        country.Under_Five_Deaths = mean([x.Under_Five_Deaths for x in list(filter(lambda y : isinstance(y.Under_Five_Deaths, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Under_Five_Deaths = "na"
    try:
        country.Polio = mean([x.Polio for x in list(filter(lambda y : isinstance(y.Polio, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Polio = "na"
    try:
        country.TotalExpenditure = mean([x.TotalExpenditure for x in list(filter(lambda y : isinstance(y.TotalExpenditure, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.TotalExpenditure = "na"
    try:
        country.Diphtheria = mean([x.Diphtheria for x in list(filter(lambda y : isinstance(y.Diphtheria, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Diphtheria = "na"
    try:
        country.HIV_AIDS = mean([x.HIV_AIDS for x in list(filter(lambda y : isinstance(y.HIV_AIDS, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.HIV_AIDS = "na"
    try:
        country.Thinness_1_19_Years =mean([x.Thinness_1_19_Years for x in list(filter(lambda y : isinstance(y.Thinness_1_19_Years, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Thinness_1_19_Years = "na"
    try:
        country.Thinness_5_9_Years = mean([x.Thinness_5_9_Years for x in list(filter(lambda y : isinstance(y.Thinness_5_9_Years, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Thinness_5_9_Years = "na"
    try:
        country.Schooling = mean([x.Schooling for x in list(filter(lambda y: isinstance(y.Schooling, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Schooling = "na"
    try:
        country.Population = mean([x.Population for x in list(filter(lambda y: isinstance(y.Population, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Population = "na"
    try:
        country.GDP = mean([x.GDP for x in list(filter(lambda y: isinstance(y.GDP, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.GDP = "na"
    try:
        country.Income_Composition_Of_Resources = mean([x.Income_Composition_Of_Resources for x in list(filter(lambda y: isinstance(y.Income_Composition_Of_Resources, Number), rawData)) if x.Country == country.Country])
    except StatisticsError:
        country.Income_Composition_Of_Resources = "na"



cleanData = "\n".join([entry.getCsvLine() for entry in rawData])
averagedData = "\n".join([country.getCsvLine() for country in countries.values()])

writeDataLines("LifeExpectancyDataCLEANED", cleanData)
writeDataLines("LifeExpectancyDataAVERAGED", averagedData)


