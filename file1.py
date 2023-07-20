#If you need to modify specific records in a file based on certain criteria 
#while continuing to read the file, you can follow this approach:
import os
file_path = 'file.txt'
#temp_file_path = 'path/to/temp_file.txt'
temp_file_path = 'temp_file.txt'

# Open the original file for reading
with open(file_path, 'r') as input_file:
    # Open a temporary file for writing
    with open(temp_file_path, 'w') as temp_file:
        # Iterate over each line in the input file
        for line in input_file:
            # Perform your criteria-based modifications
            # For example, let's assume we want to replace "old" with "new" in each line
            modified_line = line.replace("old", "new")
            
            # Write the modified line to the temporary file
            temp_file.write(modified_line)
            
            # Continue processing or reading the original file as needed
            # You can perform additional operations on the modified line here
            
# Replace the original file with the modified temporary file
# Uncomment the following lines if you want to replace the original file
# import os
# os.replace(temp_file_path, file_path)

# Print the modified file
with open(temp_file_path, 'r') as modified_file:
    content = modified_file.read()
    print(f'Modified file content:\n{content}')

# If you want to replace old file with temp file, execute below code
#os.replace(temp_file_path,file_path)
