import argparse
import csv
from tabulate import tabulate

parser = argparse.ArgumentParser()

# Options, именованные аргументы
parser.add_argument('--file', type=str, dest='file_names', nargs='+',
                    help='file names',)
parser.add_argument('--report', choices=['average-gdp', ...],
                    help='report type')

args = parser.parse_args()


if args.report == 'average-gdp':
    gdp_data = {}
    try:
        gdp_average = {}
        for file_name in args.file_names:
            with open(file_name, 'r') as f:
                data = csv.DictReader(f)
                for row in data:
                    country = row['country']
                    gdp = float(row['gdp'])
                    if country not in gdp_average:
                        gdp_average[country] = []
                    gdp_average[country].append(gdp)

        for country, gdp_list in gdp_average.items():
            average_gdp = sum(gdp_list) / len(gdp_list)
            gdp_data[country] = average_gdp
        formatted_data = []

        for i, (country, gdp) in enumerate(gdp_data.items(), start=1):
            formatted_gdp = f"{gdp:.2f}"
            formatted_data.append((i, country, formatted_gdp))

        results = tabulate(
            formatted_data,
            headers=['', 'country', 'gdp'],
            tablefmt='pretty',
            colalign=('right', 'left', 'right'),
        )
    except FileNotFoundError as e:
        print(f"File not found (Файл не найден): {e}")
    except Exception as e:
        print(f"Error reading file (Ошибка чтения файла {file_name}): {e}")


print('---- Отчет создан успешно ----')
print(results)
