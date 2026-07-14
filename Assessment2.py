# Storage: { "RollNo": [ "Name", Marks ] }
students = {}

while True:
    print("\n*** STUDENT SYSTEM ***")
    print("1. Add  2. Display  3. Search  4. Update  5. Delete")
    print("6. Topper  7. Average  8. Count  9. Exit")
    
    choice = int(input("\nEnter choice (1-9): "))
    
    if choice == 9:
        print("Goodbye!")
        break
        
    elif choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        students[roll] = [name, marks]
        print("Added successfully!")
        
    elif choice == 2:
        for roll in students:
            print(f"Roll: {roll} | Name: {students[roll][0]} | Marks: {students[roll][1]}")
            
    elif choice == 3:
        roll = input("Enter Roll No to search: ")
        if roll in students:
            print(f"Found -> Name: {students[roll][0]}, Marks: {students[roll][1]}")
        else:
            print("Not found.")
            
    elif choice == 4:
        roll = input("Enter Roll No to update: ")
        if roll in students:
            new_marks = float(input("Enter new marks: "))
            students[roll][1] = new_marks
            print("Updated!")
        else:
            print("Not found.")
            
    elif choice == 5:
        roll = input("Enter Roll No to delete: ")
        if roll in students:
            del students[roll]
            print("Deleted!")
        else:
            print("Not found.")
            
    elif choice == 6:
        if not students: print("No students.")
        else:
            topper_roll = ""
            max_marks = -1
            for roll in students:
                if students[roll][1] > max_marks:
                    max_marks = students[roll][1]
                    topper_roll = roll
            print(f"Topper is {students[topper_roll][0]} with {max_marks} marks!")
            
    elif choice == 7:
        if not students: print("No students.")
        else:
            total = 0
            for roll in students:
                total += students[roll][1]
            print("Average Marks:", total / len(students))
            
    elif choice == 8:
        print("Total Students:", len(students))
        
    else:
        print("Invalid choice!")
