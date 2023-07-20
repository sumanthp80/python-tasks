def read_fixed_length_file(file_path, column_widths):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            row = []
            start = 0
            for width in column_widths:
                value = line[start:start+width].strip()
                row.append(value)
                start += width
            data.append(row)
    return data

def write_fixed_length_file(file_path, data, column_widths):
    with open(file_path, "w") as file:
        for row in data:
            line = ""
            for i in range(len(column_widths)):
                value = str(row[i]).ljust(column_widths[i])
                line += value
            file.write(line + "\n")

# Example usage:
file_path = "data.txt"
column_widths = [10, 15, 8]

# Reading fixed-length file
data = read_fixed_length_file(file_path, column_widths)
print("Data:")
for row in data:
    print(row)

# Modifying the data
for row in data:
    row[1] = row[1].upper()

# Writing data to a new fixed-length file
new_file_path = "modified_data.txt"
write_fixed_length_file(new_file_path, data, column_widths)
print("Modified data written to:", new_file_path)
