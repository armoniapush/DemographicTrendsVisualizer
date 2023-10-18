markdown
# 📊 Population Graph Generator

## 📝 Description

The "Population Graph Generator" is a project centered around the creation of population evolution graphs for various countries over the years. The project relies on a Python (`3.10.12`) script that extracts population data from a CSV file and generates scatter plots to visualize the comparative population trends across multiple countries.

## 🚀 Operation

The project is executed through a Python script. Follow these steps to set up and run it:

1. **Clone the Repository:** Clone the repository to your local machine using the following git command:

   ```shell
   git clone https://github.com/yourusername/population_graph.git
   ```
   **Or FORK it**

2. **Activate the Virtual Environment:** Activate your Python virtual environment using one of the following methods depending on your operating system:

   - **On Unix (Linux and macOS):**

     ```shell
     source nombre_del_entorno/bin/activate
     ```

   - **On Windows:**

     ```shell
     nombre_del_entorno\Scripts\activate
     ```

3. **Install Dependencies:** Once the virtual environment is active, navigate to the project directory and create or ensure the existence of a `requirements.txt` file. You can create one and list the dependencies as follows (if requirements.txt do not exist):

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

4. **Install Dependencies:** Install the project's dependencies using the following pip command:

   ```shell
   pip3 install -r requirements.txt
   ```

5. **Run the Script:** Run the main script using Python 3:

   ```shell
   python3 main.py
   ```

6. **Country Selection:** The script will prompt you to input the names of countries, separated by commas or spaces (up to a maximum of 4 countries).

7. **Graph Generation:** After entering the countries, the script will generate scatter plots that display the population evolution of the selected countries over the years.

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