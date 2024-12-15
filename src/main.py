import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from country import country
import os

def load_data(path):
    # Loads the data csv into a dataframe
    df = pd.read_csv(path)
    df.rename(columns={"Country": "country", "Year": "year", "Life expectancy at birth (years)" : "life_expectancy", "GDP": "gdp"}, inplace=True)
    
    return df


def summary_statistics(df):
    # provides df summary statistics and a correlation matrix heatmap
    # User can choose to see summary statistics or not

    print(df.head())
    print(df.describe())
    print(df["country"].unique())

    df_corr = df.drop(["country"], axis=1)
    correlation_matrix = df_corr.corr()

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()
    plt.clf()


def sluggify(country):
    # turns country names into slugs

    country = country.lower()
    special_characters = r'[^A-Za-z0-9\s-]'
    country = re.sub(special_characters, "", country)
    country = re.sub(r'\s+', "_", country)

    return country


def create_country_instance(country_string, dataframe):
    # initialises an instance of the country class

    country_string_cleaned = sluggify(country_string)

    return country(country_string_cleaned, dataframe)


def group_by_country(df):
    # creates dataframes for each country

    countries = df["country"].unique()

    df_country = df.groupby('country')
    list_of_dfs = [df_country.get_group(x) for x in df_country.groups]   
    
    chile = create_country_instance(countries[0], list_of_dfs[0])
    china = create_country_instance(countries[1], list_of_dfs[1])
    germany = create_country_instance(countries[2], list_of_dfs[2])
    mexico = create_country_instance(countries[3], list_of_dfs[3])
    united_states = create_country_instance(countries[4], list_of_dfs[4])
    zimbabwe = create_country_instance(countries[5], list_of_dfs[5])

    return (chile, china, germany, mexico, united_states, zimbabwe)
    

def calculate_global_mean(df):
    # calculates the mean life expectancy by grouping by year and then
    # aggregating them into a tuple

    life_expactancy_mean = df.groupby('year')['life_expectancy'].mean()
    
    mean_df = life_expactancy_mean.aggregate(lambda x: tuple(round(x, 2)))

    return mean_df



if __name__ == "__main__":

    graph_folder = r'./figures'
    if not os.path.exists(graph_folder):
        os.makedirs(graph_folder)

    df = load_data('data\\all_data.csv')

    print("Would you like to see summary statitics? (Y/N)")
    
    # while loop to determine whether summary statistics are shown
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
    list_of_countries = group_by_country(df)


    mean_life_expectancy = calculate_global_mean(df)

    plt.figure(figsize=(12, 8))

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown"]
    for i in range(len(list_of_countries)):
        list_of_countries[i].plot_life_expectancy(title=False, color=colors[i])

    plt.plot(chile.dataframe['year'].unique(), mean_life_expectancy, label="mean", linestyle='--', color="tab:gray")

    plt.legend(loc="center right", bbox_to_anchor=(1.10, 0.63), ncol=1, fancybox=True, shadow=True)
    plt.suptitle("Plot of the life expectancy at birth against Year")

    plt.savefig("./figures/country_comparison.png")

    fig, axs = plt.subplots(2, 3, figsize=(18, 8))
    
    chile.plot_life_expectancy(ax=axs[0,0], mean=mean_life_expectancy, color="tab:blue")
    china.plot_life_expectancy(ax=axs[0, 1], mean=mean_life_expectancy, color="tab:orange")
    germany.plot_life_expectancy(axs[0, 2], mean=mean_life_expectancy, color="tab:green")
    mexico.plot_life_expectancy(axs[1, 0], mean=mean_life_expectancy, color="tab:red")
    united_states.plot_life_expectancy(axs[1, 1], mean=mean_life_expectancy, color="tab:purple")
    zimbabwe.plot_life_expectancy(axs[1, 2], mean=mean_life_expectancy, color="tab:brown")
    

    plt.savefig("./figures/individual_country_life_expectancy.png")

    plt.close()