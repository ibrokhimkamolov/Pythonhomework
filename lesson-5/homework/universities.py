universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions

def mean(values):
    return sum(values) / len(values) if values else 0

def median(values):
    if not values:
        return 0
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2 
    
    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2

enrollments, tuitions = enrollment_stats(universities)
total_students = sum(enrollments)
total_tuition = sum(tuitions)
mean_students = mean(enrollments)
median_students = median(enrollments)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}\n")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,}")
print("*" * 30)