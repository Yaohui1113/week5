import csv

def get_classification(average):
    if average >= 70:
        return "1"
    elif average >= 60:
        return "2:1"
    elif average >= 50:
        return "2:2"
    elif average >= 40:
        return "3"
    else:
        return "F"
    
def calculate_grades(input_filename):
    output_filename = f"{input_filename}_out.csv"

    with open(input_filename, 'r') as infile, open(output_filename, "w", newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        writer.writerow(["student_id", "average_grade", "classification"])

        for row in reader:
            student_id = row[0]
            grades = [int(grade) for grade in row[1:] if grade]
            if grades:
                average_grade = sum(grades) / len(grades)
                classification = get_classification(average_grade)
                writer.writerow([student_id, f"{average_grade:.2f}", classification])

input_filename = input("Enter the filename of the student file: ")
calculate_grades(input_filename)
