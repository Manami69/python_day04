import pandas as pd
from FileLoader import FileLoader

def youngestFellah(df, year):
    new = df.filter(['Year', 'Sex', 'Age'])
    new = new.loc[new['Year'] == year]
    fem = new.loc[new['Sex'] == 'F']
    hom = new.loc[new['Sex'] == 'M']
    youngest = {'f' : fem["Age"].min(), 'm' : hom['Age'].min()}
    print(youngest)

# loader = FileLoader()
# data = loader.load('../data/athlete_events.csv')
# youngestFellah(data, 2004)