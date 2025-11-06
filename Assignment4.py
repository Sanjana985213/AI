from constraint import Problem

problem = Problem()

subjects = {
    "AI": "Prof. Verma",
    "ML": "Prof. Sharma",
    "DS": "Prof. Patil",
    "DT": "Prof. Pawar"
}

slots = ["Tue 10am", "Thu 11am", "Fri 11:30am", "Sat 9am"]

for subj in subjects:
    problem.addVariable(subj, slots)  


for s1 in subjects:
    for s2 in subjects:
        if s1 != s2:
            problem.addConstraint(lambda a, b: a != b, (s1, s2))


problem.addConstraint(lambda t: t == "Tue 10am", ("AI",))      
problem.addConstraint(lambda t: t == "Fri 11:30am", ("DT",)) 


solution = problem.getSolution()

if solution:
    print("One valid timetable:\n")
    for subj in subjects:
        print(f"  {subj} : {solution[subj]}")
else:
    print("No timetable possible.")
