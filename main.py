from menu import show_menu
from actions import *
from data import  data_import
from data import data_export

students = []

def main():
    global students
    students = data_import()

    while True:
        option= show_menu()

        if option == "1" : 
            enter_students(students)
        elif option == "2" :
            show_students(students)
        elif option == "3" :
            show_top3(students)
        elif option == "4" :
            show_general_average(students)
        elif option == "5" :
            data_export(students)
        elif option == "6" : 
            students = data_import()
        elif option == "0" :
            print ("Goodbye cow boy ")
            break
        else:
            print ( "Invalid option, try again and please enter the correct number option ")

if __name__ == "__main__":
    main()
