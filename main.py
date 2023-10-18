import difflib
import pandas as pd
from charts import plot_population_data

def find_best_matches(country_names, available_countries):
    user_countries = [country.strip() for country in country_names.replace(',', ' ').split()]

    best_matches = []
    for user_country in user_countries:
        matches = difflib.get_close_matches(user_country.lower(), available_countries, n=4, cutoff=0.6)
        if matches:
            best_matches.append(matches[0].title())

    return best_matches

if __name__ == '__main__':
    data = pd.read_csv('data.csv')

    input_countries = input("Enter the names of the countries separated by commas or spaces: ").strip().lower()

    user_countries = [country.strip() for country in input_countries.replace(',', ' ').split()]

    matched_countries = find_best_matches(' '.join(user_countries), data['Country/Territory'].str.lower())

    if matched_countries:
        print("Generating Chart...")
        plot_population_data(data[data['Country/Territory'].str.title().isin(matched_countries)])
    else:
        print("No close matches found for the entered countries.")
