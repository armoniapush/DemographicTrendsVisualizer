import csv

def read_csv(path):
    data = []
    try:
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                # Dictionary to store the country name and population data HERE =>
                country_data = {'Country/Territory': row['Country/Territory']}
                for key, value in row.items():
                    if key.endswith(" Population"):
                        country_data[key] = value
                data.append(country_data)
    except FileNotFoundError:
        print(f'The file {path} does not exist.')
    except csv.Error as e:
        print(f'Error reading the file {path}: {e}')
    return data

if __name__ == '__main__':
    data = read_csv('data.csv')
    for entry in data:
        print(entry)
