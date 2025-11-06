from constraint import Problem

teams = ["T1", "T2", "T3", "T4"]

# All unique matches between teams
matches = [(t1, t2) for i, t1 in enumerate(teams) for t2 in teams[i + 1:]]

time_slots = [1, 2, 3]  # 3 time slots
stadiums = ["A", "B"]   # 2 stadiums

p = Problem()

# Each match → (time_slot, stadium)
p.addVariables(matches, [(t, s) for t in time_slots for s in stadiums])

# Constraint: No team plays two matches in the same time slot
for team in teams:
    team_matches = [m for m in matches if team in m]
    for i in range(len(team_matches)):
        for j in range(i + 1, len(team_matches)):
            # Use default arguments to avoid late binding issue in lambda
            p.addConstraint(lambda m1, m2, i=i, j=j: m1[0] != m2[0],
                            (team_matches[i], team_matches[j]))

# Constraint: No two matches can happen in the same stadium at the same slot
for i in range(len(matches)):
    for j in range(i + 1, len(matches)):
        p.addConstraint(lambda m1, m2, i=i, j=j: not (m1[0] == m2[0] and m1[1] == m2[1]),
                        (matches[i], matches[j]))

# Get all valid solutions
solutions = p.getSolutions()

print("Total valid schedules:", len(solutions))
print("\nSample Schedule:")
if solutions:
    for match, schedule in solutions[0].items():
        print(f"{match}: Time Slot {schedule[0]}, Stadium {schedule[1]}")
else:
    print("No valid schedules found.")
