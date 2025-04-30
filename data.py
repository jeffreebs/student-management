import csv
import os

f1le = "students.csv"

def data_export(students):
    with open(f1le,mode = "w",)as f:
        space=["name", "section", "Spanish", "English", "Science", "Social Studies" ]
        writer = csv.DictWriter(f,fieldnames=space)
        writer.writeheader()
        writer.writerows(students)
    print("Data export successfully ")

def data_import():
    if not os.path.exists(f1le):
        print("Not exist CSV file")
    return[]


    with open(f1le, mode= "r",) as f:
        reader = csv.DictReader(f)
        return [
            {
                "name": row["name"],
                "section": row ["section"],
                "Spanish": float(row["Spanish"]),
                "English": float(row["English"]),
                "Science": float(row["Science"]),
                "Social Studies": float(row["Social Studies"]),
            }

            for row in reader
        ]
