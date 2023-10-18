markdown
# 📊 Population Graph Generator

## 📝 Description

The "Population Graph Generator" project is dedicated to creating dynamic population evolution visualizations for diverse countries over multiple years. At its core, the project leverages a Python script developed for Python (`3.10.12`), extracting comprehensive population data from structured CSV files to generate informative scatter plots. These plots offer an insightful perspective on comparative population trends across a multitude of countries.

## 🚀 Getting Started

To use the "Population Graph Generator," follow these steps:

### 1. Clone the Repository

Clone the repository to your local machine using the following git command:

```shell
git clone https://github.com/yourusername/population_graph.git
```
**Or FORK it**

### 2. Create and Activate the Virtual Environment

#### Create

**On Unix (Linux and macOS):**

```shell
python3 -m venv pg_310env
```

**On Windows:**

```shell
python -m venv pg_310env
```

#### Activate

**On Unix (Linux and macOS):**

```shell
source pg_310env/bin/activate
```

**On Windows:**

```shell
pg_310env\Scripts\activate
```

### 3. Install Dependencies

Once the virtual environment is active, navigate to the project directory and create or ensure the existence of a `requirements.txt` file. If it doesn't exist, create it and list the dependencies as follows:

```
contourpy==1.1.1
cycler==0.12.1
fonttools==4.43.1
kiwisolver==1.4.5
matplotlib==3.8.0
numpy==1.26.1
packaging==23.2
Pillow==10.1.0
pyparsing==3.1.1
python-dateutil==2.8.2
six==1.16.0
```

### 4. Install Dependencies

Install the project's dependencies using the following pip command:

```shell
pip3 install -r requirements.txt
```

### 5. Run the Script

Run the main script using Python 3:

```shell
python3 main.py
```

### 6. Country Selection

The script will prompt you to input the names of countries, separated by commas or spaces (up to a maximum of 4 countries).

### 7. Graph Generation

After entering the countries, the script will generate scatter plots that display the population evolution of the selected countries over the years.

## 🌟 Benefits

The key advantages of this project are as follows:

- **Comparative Visualization:** It allows for the comparison of population evolution among several countries in a single graph, making it easier to discern trends and disparities.

- **Access to Population Data:** It utilizes population data available in a CSV file, offering the opportunity to analyze and visualize demographic information from various regions across the globe.

- **Customization and Collaboration:** The project is open-source and can be customized and enhanced by the community. It also provides an opportunity for collaborative efforts to improve data visualization.

## 🤝 Contributions

If you wish to contribute to the project, we welcome collaborations! You can open issues, submit pull requests, and enhance both functionality and user interface.

## 📜 License

This project is licensed under the [MIT License](LICENSE).
```