from FileLoader import FileLoader
import pandas as pd

def proportionBySport(df, year, sport, gender):
    cut = df.loc[df['Year'] == year]
    cut = cut.loc[cut['Sex'] == gender]
    cut = cut.drop_duplicates(subset="Name")
    nb = len(cut.loc[cut["Sport"] == sport])
    prop = nb / cut.shape[0]
    print(prop)

# loader = FileLoader()
# data = loader.load('../data/athlete_events.csv')
# proportionBySport(data, 2004, 'Tennis', 'F')