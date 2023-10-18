import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random
import os
import pandas as pd

def generate_random_color():
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def plot_population_data(data):
    # Extract columns containing population data
    population_columns = [col for col in data.columns if col.endswith(" Population")]

    # Create a figure for the graph
    plt.figure(figsize=(10, 6))

    max_population = data[population_columns].max().max()

    years = [col.split()[0] for col in population_columns]

    for _, row in data.iterrows():
        # Generate a random color for each country (important)
        color = generate_random_color()

        populations = row[population_columns]

        # Create a scatter plot with round points
        plt.scatter(years, populations, color=color, marker='o', s=100, alpha=0.7, label=row["Country/Territory"])

        # Connect the points with a white line of the same color
        plt.plot(years, populations, color=color, linewidth=1, alpha=0.8, linestyle='--', marker='x')

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

    # Create a folder named "assets" if it doesn't exist
    os.makedirs("assets", exist_ok=True)

    # Save the image in the "assets" folder with the name "graph.png"
    plt.savefig(os.path.join("assets", "graph.png"))
