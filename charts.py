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

    # Set the index of the DataFrame to the "Country/Territory" column
    data = data.set_index("Country/Territory")

    # Create a figure for the graph and set the background color to light gray
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.set_facecolor('#f3f3f3')

    max_population = data[population_columns].max().max()

    # Invert the order of years directly in the DataFrame
    data = data[population_columns].iloc[:, ::-1]
    years = data.columns.str.split().str[0]

    for idx, row in data.iterrows():
        # Generate a random color for each country (important)
        color = generate_random_color()

        # Create a scatter plot with round points, excluding white color
        ax.scatter(years, row, color=color, marker='o', s=100, alpha=0.7, label=idx)

        # Connect the points with a white line of the same color
        ax.plot(years, row, color=color, linewidth=1, alpha=0.8, linestyle='--', marker='x')

    ax.set_title('Population Evolution', color='black')
    ax.set_xlabel('Year', color='black')
    ax.set_ylabel('Population (in millions)', color='black')

    if max_population > 0:
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.0f}m'))
        ax.set_ylim(0, max_population * 1.1)
        ax.yaxis.set_major_locator(ticker.MultipleLocator(base=max_population / 10))

    ax.tick_params(axis='x', rotation=45, colors='black')
    ax.tick_params(axis='y', colors='black')

    # Ensure that the grid is behind the data
    ax.set_axisbelow(True)
    
    # Display a grid with a darker color
    ax.grid(axis='y', linestyle='--', alpha=0.2, color='gray')
    ax.legend()

    fig.tight_layout()

    # Create a folder named "assets" if it doesn't exist
    os.makedirs("assets", exist_ok=True)

    # Save the image in the "assets" folder with the name "graph.png"
    fig.savefig(os.path.join("assets", "graph.png"))
