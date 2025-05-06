import csv
import os



def data_export(students):
    filename = "students.csv"
    with open(filename,mode = "w",)as f:
        space=["name", "section", "Spanish", "English", "Science", "Social Studies" ]
        writer = csv.DictWriter(f,fieldnames=space)
        writer.writeheader()
        writer.writerows(students)
    print("Data export successfully ")

def data_import():
    filename = "students.csv"
    if not os.path.exists(filename):
        print("The File is null.")
        return []

    students = []
    try:
        with open(filename, mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    student = {
                        "name": row["name"],
                        "section": row["section"],
                        "Spanish": float(row["Spanish"]),
                        "English": float(row["English"]),
                        "Science": float(row["Science"]),
                        "Social Studies": float(row["Social Studies"]),
                    }
                    students.append(student)
                except ValueError:
                    print(f" Error in data students'{row['name']}'. Not add the file.")
    except Exception as e:
        print(f" Error to read the file: {e}")
    
    return students



    
