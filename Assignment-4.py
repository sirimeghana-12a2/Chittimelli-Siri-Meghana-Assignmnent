# #1. #Create class name as deptartment. Containing deptname,deptid,deptlocation and HOD through the constructor initialize the department attributes.
#     #Create a method to display the dept info
#     #dispaly total departments in the organisation
class Department:
    dept_count = 0
    def __init__(self,deptid,deptname,deptloc,HOD):
        self.deptid = deptid
        self.deptname = deptname
        self.deptloc = deptloc
        self.HOD = HOD
        Department.dept_count += 1
    def display_dept_info(self):
        print("Department Information:")
        print("----------------------------")
        print(f"ID : {self.deptid}")
        print(f"Name: {self.deptname}")
        print(f"Location: {self.deptloc}")
        print(f"HOD: {self.HOD}")
    @classmethod
    def get_total_dept(cls):
        return cls.dept_count
dept1 = Department(101,"CSE","HYderabad","Anitha") #<- here data is given
dept1.display_dept_info()
dept2 = Department(102,"IT","Pune","Siri")
dept2.display_dept_info()
dept3 = Department(103,"AIML","Banglore","Vinaya")
dept3.display_dept_info()
dept4 = Department(104,"ECE","Chennai","Ramesh")
dept4.display_dept_info()
dept5 = Department(105,"EEE","Mumbai","Mrudula")
print(f"Total Departments: {Department.get_total_dept()}")
# #Output
# # Department Information:
# # ----------------------------
# # ID : 101
# # Name: CSE
# # Location: HYderabad
# # HOD: Anitha
# # Department Information:
# # ----------------------------
# # ID : 102
# # Name: IT
# # Location: Pune
# # HOD: Siri
# # Department Information:
# # ----------------------------
# # ID : 103
# # Name: AIML
# # Location: Banglore
# # HOD: Vinaya
# # Department Information:
# # ----------------------------
# # ID : 104
# # Name: ECE
# # Location: Chennai
# # HOD: Ramesh
# # Total Departments: 5


# #2. #get the input from users no.of depts create the list or dict to store different depts and use for loop to get dept info.
#     #the info provided add to list or dict
#     #display all dept info in the form of list or dict.
#     #add method search dept by deptno. User will give input deptid. if there print details else dept not available.
#     #add a function to search dept by name
class Department:
    dept_count = 0

    def __init__(self, deptid, deptname, deptloc, HOD):
        self.deptid = deptid
        self.deptname = deptname
        self.deptloc = deptloc
        self.HOD = HOD
        Department.dept_count += 1

    def display_dept_info(self):
        print("Department Information:")
        print("----------------------------")
        print(f"ID      : {self.deptid}")
        print(f"Name    : {self.deptname}")
        print(f"Location: {self.deptloc}")
        print(f"HOD     : {self.HOD}\n")


departments = {}

def add_department():
    n = int(input("Enter number of departments to add: "))
    for i in range(n):
        print(f"\nEnter details for Department #{i+1}:")
        deptid = int(input("Enter Dept ID     : "))
        deptname = input("Enter Dept Name   : ")
        deptloc = input("Enter Dept Location: ")
        hod = input("Enter HOD Name    : ")
        dept = Department(deptid, deptname, deptloc, hod)
        departments[deptid] = dept
    print("\nDepartments added successfully.\n")

def search_by_deptid():
    search_id = int(input("Enter Department ID to search: "))
    if search_id in departments:
        departments[search_id].display_dept_info()
    else:
        print("Department not found with that ID.\n")

def search_by_deptname():
    name = input("Enter Department Name to search: ")
    found = False
    for dept in departments.values():
        if dept.deptname.lower() == name.lower():
            dept.display_dept_info()
            found = True
            break
    if not found:
        print("Department not found with that name.\n")

def display_all_departments():
    if not departments:
        print("No departments to display.\n")
    else:
        for dept in departments.values():
            dept.display_dept_info()

while True:
    print("----- Department Management Menu -----")
    print("1. Add Department Details")
    print("2. Search Department by ID")
    print("3. Search Department by Name")
    print("4. Display All Departments")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_department()
    elif choice == 2:
        search_by_deptid()
    elif choice == 3:
        search_by_deptname()
    elif choice == 4:
        display_all_departments()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.\n")
#Output
# ----- Department Management Menu -----
# 1. Add Department Details
# 2. Search Department by ID
# 3. Search Department by Name
# 4. Display All Departments
# 5. Exit
# Enter your choice: 1
# Enter number of departments to add: 2

# Enter details for Department #1:
# Enter Dept ID     : 101
# Enter Dept Name   : CSE
# Enter Dept Location: Hyderabad
# Enter HOD Name    : Anitha

# Enter details for Department #2:
# Enter Dept ID     : 102
# Enter Dept Name   : IT
# Enter Dept Location: Pune
# Enter HOD Name    : Siri

# Departments added successfully.

# ----- Department Management Menu -----
# 1. Add Department Details
# 2. Search Department by ID
# 3. Search Department by Name
# 4. Display All Departments
# 5. Exit
# Enter your choice: 2
# Enter Department ID to search: 102
# Department Information:
# ----------------------------
# ID      : 102
# Name    : IT
# Location: Pune
# HOD     : Siri

# ----- Department Management Menu -----
# 1. Add Department Details
# 2. Search Department by ID
# 3. Search Department by Name
# 4. Display All Departments
# 5. Exit
# Enter your choice: 2
# Enter Department ID to search: 103
# Department not found with that ID.

# ----- Department Management Menu -----
# 1. Add Department Details
# 2. Search Department by ID
# 3. Search Department by Name
# 4. Display All Departments
# 5. Exit
# Enter your choice: 3
# Enter Department Name to search: CSE
# Department Information:
# ----------------------------
# ID      : 101
# Name    : CSE
# Location: Hyderabad
# HOD     : Anitha

# ----- Department Management Menu -----
# 1. Add Department Details
# 2. Search Department by ID
# 3. Search Department by Name
# 4. Display All Departments
# 5. Exit
# Enter your choice: 3 
# Enter Department Name to search: ECE
# Department not found with that name.

# ----- Department Management Menu -----
# 1. Add Department Details
# 2. Search Department by ID
# 3. Search Department by Name
# 4. Display All Departments
# 5. Exit
# Enter your choice: 4
# Department Information:
# ----------------------------
# ID      : 101
# Name    : CSE
# Location: Hyderabad
# HOD     : Anitha

# Department Information:
# ----------------------------
# ID      : 102
# Name    : IT
# Location: Pune
# HOD     : Siri

# ----- Department Management Menu -----
# 1. Add Department Details
# 2. Search Department by ID
# 3. Search Department by Name
# 4. Display All Departments
# 5. Exit
# Enter your choice: 5