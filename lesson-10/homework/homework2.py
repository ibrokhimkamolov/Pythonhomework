import csv
from collections import defaultdict

def read_grades(file_name):
    grades = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = defaultdict(lambda: {'total': 0, 'count': 0})
    
    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        subject_totals[subject]['total'] += grade
        subject_totals[subject]['count'] += 1
    
    averages = {subject: total['total'] / total['count'] for subject, total in subject_totals.items()}
    return averages

def write_averages(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 1)])

# File names
grades_file = '/Users/ibrokhimkamolov/Documents/Analytics_Studies/Python/Pythonhomework/lesson-10/homework/grades.csv'

averages_file = 'average_grades.csv'

# Process data
grades = read_grades(grades_file)
averages = calculate_average(grades)
write_averages(averages_file, averages)

print(f"Average grades written to {averages_file}")
