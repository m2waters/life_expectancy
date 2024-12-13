import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(path):
    
    df = pd.read_csv(path)
    
    return df


def summary_statistics(df):

    print(df.head())
    print(df.describe())

    df_corr = df.drop(["Country"], axis=1)
    correlation_matrix = df_corr.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()
    plt.clf()


def plot_graph(x, y):

    plt.plot(x, y)

    plt.show()
    plt.clf()



if __name__ == "__main__":

    df = load_data('data\\all_data.csv')

    print("Would you like to see summary statitics? (Y/N)")
    
    x = 0
    while x == 0:
        summary = input()
        if summary == "Y" or summary == "":
            x = 1
            print("Summary Statistics:")
            summary_statistics(df)
        elif summary == "N":
            x = 1
            print("Summary statistics will not be displayed")
        else:
            print("Please input Y or N to make a decision:")