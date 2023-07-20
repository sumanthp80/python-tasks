#Python code that opens a file in 'r+' mode for both reading and writing:
file_path = 'path/to/file.txt'

# Open the file in 'r+' mode
with open(file_path, 'r+') as file:
    # Read from the file
    content = file.read()
    print(f'Content read from the file: {content}')
    
    # Write to the file
    file.write('New content')
    print('Content written to the file')
    
    # Move the file pointer to the beginning
    file.seek(0)
    
    # Read the modified content from the file
    modified_content = file.read()
    print(f'Modified content: {modified_content}')
