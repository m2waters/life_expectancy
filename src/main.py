import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

def load_data(path):
    
    df = pd.read_csv(path)
    
    return df


def summary_statistics(df):

    print(df.head())
    print(df.describe())
    print(df["Country"].unique())

    df_corr = df.drop(["Country"], axis=1)
    correlation_matrix = df_corr.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()
    plt.clf()

def create_df_name(country):

    country = country.lower()
    special_characters = r'[^A-Za-z0-9\s-]'
    country = re.sub(special_characters, "", country)
    country = re.sub(r'\s+', "_", country)


    return "df_" + country



def group_by_country(df):

    countries = df["Country"].unique()

    # df_chile = df[df["Country"] == "chile"]

    df_country = df.groupby('Country')
    list_of_dfs = [df_country.get_group(x) for x in df_country.groups]
    
    for i in range(len(countries)):
        
        df_name = create_df_name(countries[i])
        print(df_name)

        print(list_of_dfs[i].head())

    #for country in countries:




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

    group_by_country(df)