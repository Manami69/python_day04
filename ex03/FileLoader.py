import pandas as pd

class FileLoader:

    def load(self, path):
        df = pd.read_csv(path)
        print("Loading dataset of dimensions {} x {}".format(*df.shape))
        return df
    
    def display(self, df, n):
        if n >= 0:
            print(df[:n:])
        else:
            print(df[n::])