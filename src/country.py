import pandas as pd
import matplotlib.pyplot as plt

class country:

    def __init__(self, name, dataframe):
        self.name = name
        self.dataframe = dataframe

    def plot_life_expectancy(self, ax=plt, title: bool=True, mean=None, color="blue"):
        ax.plot(self.dataframe["year"], self.dataframe["life_expectancy"], label=self.name, color=color)

        if mean != None:
            ax.plot(self.dataframe["year"], mean, color="tab:gray")

        if title:
            ax.set_title(f"{self.name} Life Expectancy vs Year")

    

        
        