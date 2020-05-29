from FileLoader import FileLoader

def howManyMedals(df, name):
    tab = df.loc[df['Name'] == name]
    