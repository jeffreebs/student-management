def enter_students(students):
    try:
        n = int(input("How many students do you want to enter: ? "))
        for x in range(n):
            name = input ("Enter the students name please : ")
            section= input("Section : ").strip()

            grades = {}
            for subject in ["Spanish", "English", "Science", "Social Studies" ]:
                while True:
                    try:
                        grade = float(input(f"Grade of {subject}: "))
                        if 0 <= grade <= 100:
                            grades[subject] = grade
                            break
                        else:
                            print ("The grade need to stay in middle of 0 and 100 ")
                    except:
                        print ("Please, enter a valid number")


            student = {
                "name" : name,
                "section": section,
                **grades
            }
            students.append(student)

    except Exception as e:
        print("Error to enter the students:", e)



def show_students (students):
    if not students:
        print ("Not have students registered. ")
        return 
    
    for st in students:
        print(st)



def calculate_average(student):
    return sum([student[sub]for sub in["Spanish", "English", "Science", "Social Studies" ]])/ 4



def show_top3(students):
    if len (students) < 3:
        print ("The program need to have at least 3 students ")
        return 
    top = sorted (students,key=calculate_average,reverse=True)[:3]
    for i, st in enumerate(top,1):
        print(f"{i}.{st['name']} - average: {calculate_average(st):.2f} ") 


def show_general_average(students):
    if not students:
        print("Not have students registered.")
        return
    averages = [calculate_average(e) for e in students]
    print(f"General average: {sum(averages)/ len(averages):2f}")        