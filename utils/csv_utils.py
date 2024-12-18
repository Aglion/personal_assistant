import csv
from .file_utils import load_json, save_json

def import_csv_to_json(csv_filename, json_filename, fieldnames):
    try:
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            data = []
            first = True
            for row in reader:
                if first and row[fieldnames[0]] == fieldnames[0]:
                    first = False
                    continue
                data.append(row)
            save_json(json_filename, data)
        print("Данные успешно импортированы из CSV.")
    except FileNotFoundError:
        print("CSV-файл не найден.")

def export_json_to_csv(json_filename, csv_filename, fieldnames):
    data = load_json(json_filename)
    with open(csv_filename, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
    print("Данные успешно экспортированы в CSV.")