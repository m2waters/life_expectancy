import pandas
import matplotlib.pyplot as plt

class country:

    def __init__(self, name, dataframe):
        self.name = name
        self.dataframe = dataframe

    def plot_life_expectancy(self, title: bool=True):

        plt.plot(self.dataframe["year"], self.dataframe["life_expectancy"], label=self.name)

        if title:
            plt.suptitle(f"Graph showing life expectancy vs year for {self.name}")

        
        