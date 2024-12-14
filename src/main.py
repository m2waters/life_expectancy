import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from country import country

def load_data(path):
    
    df = pd.read_csv(path)
    df.rename(columns={"Country": "country", "Year": "year", "Life expectancy at birth (years)" : "life_expectancy", "GDP": "gdp"}, inplace=True)
    
    return df


def summary_statistics(df):

    print(df.head())
    print(df.describe())
    print(df["country"].unique())

    df_corr = df.drop(["country"], axis=1)
    correlation_matrix = df_corr.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()
    plt.clf()

def sluggify(country):

    country = country.lower()
    special_characters = r'[^A-Za-z0-9\s-]'
    country = re.sub(special_characters, "", country)
    country = re.sub(r'\s+', "_", country)


    return country

def create_country_instance(country_string, dataframe):
    country_string_cleaned = sluggify(country_string)
    return country(country_string_cleaned, dataframe)


def group_by_country(df):

    countries = df["country"].unique()

    df_country = df.groupby('country')
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




def plot_country_vs_life_expectancy(country):

    

    plt.plot(country.dataframe["year"], country.dataframe["life_expectancy"])

    plt.suptitle(f"Graph showing life expectancy vs year for {country.name}")

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

    list_of_countries = [chile, china, germany, mexico, united_states, zimbabwe]
    plt.figure(figsize=(15, 10))
    for i in list_of_countries:
        i.plot_life_expectancy(title=False)
    
    plt.legend(loc="center right", bbox_to_anchor=(1.10, 0.63), ncol=1, fancybox=True, shadow=True)
    plt.suptitle("Plot of the life expectancy at birth against Year")
    # zimbabwe.plot_life_expectancy(title=False)
    plt.show()