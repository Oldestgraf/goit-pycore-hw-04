def total_salary(file_path):
    """Calculate total and average salary"""
    total = 0
    line_count = 0
    average = 0
    try:
        with open(file_path, encoding='utf-8') as file:
            for line in file:
                line_count += 1 # Calculate how many lines
                data_list = line.strip().split(',')
                total += int(data_list[1]) # Calculate total salary
        average = int(total/line_count) # Calculate average salary
    except FileNotFoundError:
        print('File is absent')
    else:
        return total, average

total, average = total_salary("task1/data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")