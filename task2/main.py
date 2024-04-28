def get_cats_info(path):
    """Calculate total and average salary"""
    data_list = []
    try:
        with open(path, encoding = 'utf-8') as file:
            for line in file:
                # Clear from spaces and divide by comma
                data_line = line.strip().split(',')
                # Create dict for each cat
                cat_info = {'id': data_line[0], 'name': data_line[1], 'age': data_line[2]}
                # Add each cat to the list
                data_list.append(cat_info)
    except FileNotFoundError:
        print('File not found')
    return data_list

cats_info = get_cats_info("task2/data.txt")
print(cats_info)
