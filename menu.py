def show_menu ():
    print ("\n---Student Management Menu ----")
    print ("1.Enter the student´s information ")
    print ("2.See the all students information ")
    print ("3.See the top 3 best student grade ")
    print("4.See the general average of all grades ")
    print ("5.Data export to CSV")
    print ("6.Data import from CSV")
    print ("0.Exit")

    option = input("Enter an option: ")
    return option.strip()
