import numpy as np
import json
import csv

# -------------------------------------------------
# Student Result Analytics Module
# -------------------------------------------------

# Student Names (10 students)
students = np.array([
    "Student 1", "Student 2", "Student 3", "Student 4", "Student 5",
    "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"
])

# Marks Matrix (Students x Subjects)
# Subjects: Subject 1, Subject 2, Subject 3
marks = np.array([
    [85, 90, 78],   # Student 1
    [60, 70, 65],   # Student 2
    [95, 88, 92],   # Student 3
    [50, 40, 55],   # Student 4
    [72, 75, 70],   # Student 5
    [98, 95, 94],   # Student 6
    [89, 92, 91],   # Student 7
    [58, 60, 55],   # Student 8
    [77, 79, 80],   # Student 9
    [45, 48, 50]    # Student 10
])

# Subject passing marks threshold
SUBJECT_PASS_MARKS = 50

# -------------------------------------------------
# Task 1: Student-wise Performance
# -------------------------------------------------

total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

# Grade Assignment
grades = np.where(average_marks >= 80, "A+",
         np.where(average_marks >= 70, "A",
         np.where(average_marks >= 60, "B",
         np.where(average_marks >= 50, "C", "F"))))

print("Student Performance Summary")
print("---------------------------")
for i in range(len(students)):
    print(f"{students[i]}: Total = {total_marks[i]}, Avg = {average_marks[i]:.1f}, Grade = {grades[i]}")

# -------------------------------------------------
# Task 2: Subject-wise Performance
# -------------------------------------------------

subject_averages = np.mean(marks, axis=0)

print("\nSubject Summary")
print("---------------------------")
for i in range(len(subject_averages)):
    print(f"Subject {i+1} Avg: {subject_averages[i]:.2f}")

# -------------------------------------------------
# Task 3: Class Summary
# -------------------------------------------------

class_average = np.mean(marks)
top_student = students[np.argmax(total_marks)]
lowest_student = students[np.argmin(total_marks)]

print(f"\nTop Student: {top_student}")
print(f"Lowest Student: {lowest_student}")
print(f"Class Average: {class_average:.2f}")

# -------------------------------------------------
# Bonus Task 6: Merit List (Top 3 Students)
# -------------------------------------------------

ranking_indices = np.argsort(-total_marks)  # Descending order

print("\nMerit List (Top 3 Students)")
print("---------------------------")
top_3 = ranking_indices[:3]
for i, idx in enumerate(top_3, start=1):
    print(f"{i}. {students[idx]} (Total = {total_marks[idx]})")

# -------------------------------------------------
# Bonus Task 7: Pass / Fail Report
# -------------------------------------------------

# Pass if average >= 50
pass_fail = np.where(average_marks >= 50, "Pass", "Fail")

print("\nPass/Fail Report")
print("---------------------------")
for i in range(len(students)):
    print(f"{students[i]}: {pass_fail[i]}")

# -------------------------------------------------
# NEW FEATURE: Subject-wise Pass/Fail Report
# -------------------------------------------------

# Create subject-wise pass/fail matrix (Pass if marks >= 50)
subject_pass_fail = np.where(marks >= SUBJECT_PASS_MARKS, "Pass", "Fail")

#Check if student passed all subjects
all_subjects_passed = np.all(marks >= SUBJECT_PASS_MARKS, axis=1)
overall_result = np.where(all_subjects_passed, "Pass (All Subjects)", "Fail (One or More Subjects)")


# Subject-wise statistics
print("\nSubject-wise Pass/Fail Statistics")
print("------------------------------------")

for subject_idx in range(marks.shape[1]):
    subject_num = subject_idx + 1
    passed_count = np.sum(marks[:, subject_idx] >= SUBJECT_PASS_MARKS)
    failed_count = len(students) - passed_count
    pass_percentage = (passed_count / len(students)) * 100
    
    print(f"\nSubject {subject_num}:")
    print(f"  Passed: {passed_count} students ({pass_percentage:.1f}%)")
    print(f"  Failed: {failed_count} students ({100-pass_percentage:.1f}%)")

# Students who failed in specific subjects
print("Students Failed in Each Subject")
print("------------------------------------")

for subject_idx in range(marks.shape[1]):
    subject_num = subject_idx + 1
    failed_students = students[marks[:, subject_idx] < SUBJECT_PASS_MARKS]
    
    if len(failed_students) > 0:
        print(f"\nSubject {subject_num}:")
        for student in failed_students:
            student_idx = np.where(students == student)[0][0]
            print(f"  - {student} (Marks: {marks[student_idx][subject_idx]})")
    else:
        print(f"\nSubject {subject_num}: All students passed! ✓")

# -------------------------------------------------
# Bonus Task 8: Export Report with User Choice
# -------------------------------------------------

# Prepare enhanced report data with subject-wise details
report_data = []
for i in range(len(students)):
    report_data.append({
        "Student": students[i],
        "Subject_1_Marks": int(marks[i][0]),
        "Subject_1_Status": subject_pass_fail[i][0],
        "Subject_2_Marks": int(marks[i][1]),
        "Subject_2_Status": subject_pass_fail[i][1],
        "Subject_3_Marks": int(marks[i][2]),
        "Subject_3_Status": subject_pass_fail[i][2],
        "Total": int(total_marks[i]),
        "Average": round(float(average_marks[i]), 2),
        "Grade": grades[i],
        "Overall_Result": overall_result[i]
    })

# User choice for export format
print("\nExport Options:")
print("-----------------")
print("1. Export as JSON only")
print("2. Export as CSV only")
print("3. Export as both JSON and CSV")
print("4. Skip export")

while True:
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Export to JSON only
            with open("student_report.json", "w") as f:
                json.dump(report_data, f, indent=4)
            print("\n✓ Report exported successfully to: student_report.json")
            break
            
        elif choice == '2':
            # Export to CSV only
            with open("student_report.csv", "w", newline="") as f:
                fieldnames = ["Student", "Subject_1_Marks", "Subject_1_Status", 
                            "Subject_2_Marks", "Subject_2_Status", 
                            "Subject_3_Marks", "Subject_3_Status",
                            "Total", "Average", "Grade", "Overall_Result"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(report_data)
            print("\n✓ Report exported successfully to: student_report.csv")
            break
            
        elif choice == '3':
            # Export to both JSON and CSV
            with open("student_report.json", "w") as f:
                json.dump(report_data, f, indent=4)
            
            with open("student_report.csv", "w", newline="") as f:
                fieldnames = ["Student", "Subject_1_Marks", "Subject_1_Status", 
                            "Subject_2_Marks", "Subject_2_Status", 
                            "Subject_3_Marks", "Subject_3_Status",
                            "Total", "Average", "Grade", "Overall_Result"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(report_data)
            
            print("\n✓ Report exported successfully to:")
            print("  - student_report.json")
            print("  - student_report.csv")
            break
            
        elif choice == '4':
            print("\n✓ Export skipped.")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            
    except KeyboardInterrupt:
        print("\n\n✓ Export cancelled.")
        break
    except Exception as e:
        print(f"Error: {e}. Please try again.")