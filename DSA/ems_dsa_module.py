import os
import csv

# -----------------------------------
# Global Course Credit Mapping
# -----------------------------------

COURSE_CREDITS = {
    "Data Structures": 4,
    "Algorithms": 4,
    "Operating Systems": 3,
    "Machine Learning": 3,
    "Compiler Design": 3,
    "DBMS": 3
}

MAX_CREDIT_LIMIT = 7


# -----------------------------------
# Load Dataset from CSV
# -----------------------------------

def load_students(filename):
    students = []

    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, filename)

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            ds = int(row["ds"])
            algo = int(row["algo"])
            dbms = int(row["dbms"])

            total = ds + algo + dbms
            average = round(total / 3, 2)

            students.append({
                "id": int(row["id"]),
                "name": row["name"],
                "ds": ds,
                "algo": algo,
                "dbms": dbms,
                "total": total,
                "average": average
            })

    return students


# -----------------------------------
# Linear Search
# -----------------------------------

def linear_search(student_list, target_id):
    for student in student_list:
        if student["id"] == target_id:
            return student
    return None


# -----------------------------------
# Ranking with Tie Handling
# -----------------------------------

def assign_ranks(student_list):

    sorted_students = sorted(
        student_list,
        key=lambda x: x["total"],
        reverse=True
    )

    prev_total = None
    rank = 0

    for i, student in enumerate(sorted_students):

        if student["total"] != prev_total:
            rank = i + 1
            prev_total = student["total"]

        student["rank"] = rank

    return sorted_students


# -----------------------------------
# Subject-wise Topper Detection
# -----------------------------------

def subject_toppers(student_list):

    ds_top = max(student_list, key=lambda x: x["ds"])
    algo_top = max(student_list, key=lambda x: x["algo"])
    dbms_top = max(student_list, key=lambda x: x["dbms"])

    return {
        "Data Structures": (ds_top["name"], ds_top["ds"]),
        "Algorithms": (algo_top["name"], algo_top["algo"]),
        "DBMS": (dbms_top["name"], dbms_top["dbms"])
    }


# -----------------------------------
# CSE Graph Class
# -----------------------------------

class CSEGraph:

    def __init__(self):
        self.graph = {}

    def add_course(self, course):

        if course not in self.graph:
            self.graph[course] = []

    def add_prerequisite(self, course, prerequisite):

        self.add_course(course)
        self.add_course(prerequisite)

        self.graph[course].append(prerequisite)

    def next_courses(self, completed_courses):

        available = []

        for course, prereqs in self.graph.items():

            if (
                course not in completed_courses and
                all(pr in completed_courses for pr in prereqs)
            ):
                available.append(course)

        return available

    def display(self):

        print("\nCSE Course Prerequisite Graph:")

        for course in self.graph:
            print(f"{course} -> {self.graph[course]}")


# -----------------------------------
# Display Table
# -----------------------------------

def display_table(student_list):

    print("-" * 110)

    print(f"{'ID':<6}{'Name':<12}{'DS':<8}{'Algo':<8}{'DBMS':<8}"
          f"{'Total':<8}{'Avg':<8}{'Rank':<6}")

    print("-" * 110)

    for student in student_list:

        rank = student.get("rank", "-")

        print(f"{student['id']:<6}"
              f"{student['name']:<12}"
              f"{student['ds']:<8}"
              f"{student['algo']:<8}"
              f"{student['dbms']:<8}"
              f"{student['total']:<8}"
              f"{student['average']:<8}"
              f"{rank:<6}")

    print("-" * 110)


# -----------------------------------
# Dynamic Programming Credit Optimization
# -----------------------------------

def credit_optimization_with_courses(courses, credits, limit):

    n = len(courses)

    dp = [[0]*(limit+1) for _ in range(n+1)]

    # Fill DP table
    for i in range(1, n+1):

        for l in range(limit+1):

            if credits[i-1] <= l:

                dp[i][l] = max(
                    credits[i-1] + dp[i-1][l-credits[i-1]],
                    dp[i-1][l]
                )

            else:

                dp[i][l] = dp[i-1][l]

    # Traceback
    selected = []

    l = limit

    for i in range(n, 0, -1):

        if dp[i][l] != dp[i-1][l]:

            selected.append(courses[i-1])
            l -= credits[i-1]

    selected.reverse()

    return dp[n][limit], selected


# -----------------------------------
# MAIN
# -----------------------------------

if __name__ == "__main__":

    # Load students
    students = load_students("students.csv")

    print("\nOriginal Data")
    display_table(students)


    # Ranking
    print("\nRanking")
    ranked_students = assign_ranks(students)
    display_table(ranked_students)


    # Subject toppers
    toppers = subject_toppers(students)

    print("\nSubject-wise Toppers:")

    for subject, (name, score) in toppers.items():

        print(f"{subject} Topper: {name} (Score: {score})")


    # Linear Search
    search_id = int(input("\nEnter Student ID to search: "))

    student = linear_search(students, search_id)

    if not student:

        print("Student not found.")
        exit()

    print(f"\nStudent Found: {student['name']}")
    print(f"DS: {student['ds']}, Algo: {student['algo']}, DBMS: {student['dbms']}")


    # Graph setup
    graph = CSEGraph()

    graph.add_prerequisite("Algorithms", "Data Structures")
    graph.add_prerequisite("Operating Systems", "Data Structures")
    graph.add_prerequisite("Machine Learning", "Algorithms")
    graph.add_prerequisite("Compiler Design", "Operating Systems")

    graph.display()


    # Determine completed courses
    completed = []

    if student["ds"] > 0:
        completed.append("Data Structures")

    if student["algo"] > 0:
        completed.append("Algorithms")

    if student["dbms"] > 0:
        completed.append("DBMS")


    # Get eligible next courses
    next_courses = graph.next_courses(completed)

    print(f"\nEligible Next Courses: {next_courses}")


    # Credit optimization using eligible courses
    if next_courses:

        credits = [COURSE_CREDITS[course] for course in next_courses]

        max_credits, selected_courses = credit_optimization_with_courses(
            next_courses,
            credits,
            MAX_CREDIT_LIMIT
        )

        print(f"\nMaximum Credits Allowed: {MAX_CREDIT_LIMIT}")
        print(f"Maximum Credits Selected: {max_credits}")
        print(f"Courses Selected for Next Semester: {selected_courses}")

    else:

        print("\nNo eligible courses available.")


"""
In this project, we learned how Data Structures and Algorithms (DSA) are applied to solve practical problems 
in student and course management systems. We implemented linear search to find specific student records efficiently. 
Sorting techniques were used to rank students based on total marks with proper tie handling. We used a graph data structure to represent 
course prerequisites and determine eligible next-semester subjects. Additionally, we applied Dynamic Programming using the 0/1 Knapsack approach 
to optimize course selection within a credit limit.

This project helped us understand how different DSA concepts work together in a complete system. 
It improved our logical thinking and problem-solving skills. We learned how optimization techniques can make better decisions 
under constraints. DSA plays a vital role in AI systems by enabling fast searching, efficient data organization, 
and intelligent decision-making. Graphs are widely used in AI for modeling relationships, 
while Dynamic Programming helps in optimization problems. Overall, this project demonstrated that DSA forms the 
backbone of efficient and intelligent systems.
"""