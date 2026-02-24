import csv
from tabulate import tabulate


def get_data(files):
    """Reads data from multiple CSV files and combines it into a single list
    of dictionaries.
    Чтение данных из нескольких CSV файлов и объединение их в один список
    словарей"""

    all_data = []
    for file in files:
        try:
            with open(file, 'r') as f:
                reader = csv.DictReader(f)
                all_data.extend(list(reader))
        except FileNotFoundError as e:
            print(f"File not found (Файл не найден): {e}")
        except Exception as e:
            print(f"An error occurred (Произошла ошибка): {e}")
    return all_data


def process_data(data: list, report_type: str) -> dict:
    """Processes the data to calculate
    the average valuesfor the specifiedreport type.
    Обработка данных для расчета
    средних значений для указанного типа отчета."""

    report_data = {}
    for row in data:
        country = row['country']
        try:
            value = float(row[report_type])
        except KeyError:
            print('Wrongly enter the --report (Не праильно введен --report)')
            continue
        if country not in report_data:
            report_data[country] = []
        report_data[country].append(value)
    average_report = {
        country: sum(values) / len(values)
        for country, values in report_data.items()
    }
    return average_report


def sort_report_data(report_data: dict) -> list:
    """Sorts the report data in descending order based on the average values.
    Сортировка данных отчета в порядке убывания на основе средних значений."""

    sorted_data = sorted(
        report_data.items(), key=lambda x: float(x[1]), reverse=True
    )
    formatted_data = [
        (i, country, f"{value:.2f}")
        for i, (country, value) in enumerate(sorted_data, start=1)
    ]
    return formatted_data


def main(files: list, report: str):
    """Main function to execute the data processing and reporting.
    Основная функция для выполнения обработки данных и создания отчета."""

    report = report.lower().replace('average-', '')
    data = get_data(files)
    report_data = process_data(data, report)
    sorted_data = sort_report_data(report_data)
    print(tabulate(sorted_data, headers=['', 'country', report],
                   tablefmt='pretty', colalign=('right', 'left', 'right')))
