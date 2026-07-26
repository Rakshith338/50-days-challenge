import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["kiran", 25])

with open("student.csv", "r") as old_file:
    read = csv.reader(old_file)

with open("copy_students.csv", "w", newline = "") as new_file:
    write = csv.writer(new_file)

for row in reader:
    write.writerow(row)
