import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from country import country

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

def create_country_instance(country_string, dataframe):
    country_string_cleaned = create_df_name(country_string)
    return country(country_string_cleaned, dataframe)


def group_by_country(df):

    countries = df["Country"].unique()

    df_country = df.groupby('Country')
    list_of_dfs = [df_country.get_group(x) for x in df_country.groups]   
    
    chile = create_country_instance(countries[0], list_of_dfs[0])
    china = create_country_instance(countries[1], list_of_dfs[1])
    germany = create_country_instance(countries[2], list_of_dfs[2])
    mexico = create_country_instance(countries[3], list_of_dfs[3])
    united_states = create_country_instance(countries[4], list_of_dfs[4])
    zimbabwe = create_country_instance(countries[5], list_of_dfs[5])

    print(zimbabwe.dataframe)

    return (chile, china, germany, mexico, united_states, zimbabwe)
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

    chile, china, germany, mexico, united_states, zimbabwe = group_by_country(df)

    #plot_graph(zimbabwe.dataframe["Year"], zimbabwe.dataframe[])