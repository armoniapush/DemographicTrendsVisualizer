import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random

def generate_random_color():
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def plot_population_data(country_data_list):
    # Create a figure for the graph
    plt.figure(figsize=(10, 6))

    max_population = 0  # Initialize to 0

    # Extract the dates from the first row of country_data_list
    years = list(country_data_list[0].keys())
    years = [year.split()[0] for year in years if year.endswith(" Population")]

    # Rearrange the list of years to go from left to right
    years.reverse()

    for country_data in country_data_list:
        populations = [int(value) for key, value in country_data.items() if key.endswith(" Population")]

        # Generate a random color for each country (important!)
        color = generate_random_color()

        # Create a scatter plot with round points
        plt.scatter(years, populations, color=color, marker='o', s=100, alpha=0.7, label=country_data["Country/Territory"])

        # Connect the points with a white line of the same color
        plt.plot(years, populations, color=color, linewidth=1, alpha=0.8, linestyle='--', marker='x')

        # Update the maximum population value
        max_population = max(max_population, max(populations))

    plt.title('Population Evolution', color='black')
    plt.xlabel('Year', color='black')
    plt.ylabel('Population (in millions)', color='black')

    if max_population > 0:
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.0f}m'))
        plt.gca().set_ylim(0, max_population * 1.1)
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=max_population / 10))

    plt.gca().tick_params(axis='x', rotation=45, colors='black')
    plt.gca().tick_params(axis='y', colors='black')

    plt.grid(axis='y', linestyle='--', alpha=0.2)
    plt.legend()

    plt.tight_layout()

    plt.savefig('graph.png')
