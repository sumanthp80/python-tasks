import csv

def read_csv_file(file_path):
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = list(csv_reader)
    return header, data

def write_csv_file(file_path, header, data):
    with open(file_path, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)

def filter_data(data, column_index, filter_value):
    filtered_data = [row for row in data if row[column_index] == filter_value]
    return filtered_data

def calculate_total(data, column_index):
    total = sum(float(row[column_index]) for row in data)
    return total

# Example usage:
csv_file_path = "data.csv"

# Reading CSV file
header, data = read_csv_file(csv_file_path)
print("Header:", header)
print("Data:", data)

# Filtering data based on a condition
filtered_data = filter_data(data, 2, "Male")
print("Filtered Data:", filtered_data)

# Calculating the total of a column
total = calculate_total(data, 3)
print("Total:", total)

# Writing data to a new CSV file
new_csv_file_path = "new_data.csv"
write_csv_file(new_csv_file_path, header, data)
print("New CSV file created:", new_csv_file_path)
