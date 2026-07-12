# Three sets of students
math_club = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
science_club = {'Charlie', 'Eve', 'Frank', 'Grace', 'Henry'}
art_club = {'Alice', 'Eve', 'Grace', 'Ivy', 'Jack'}

# 1. Students in at least one club (Union)
at_least_one = math_club | science_club | art_club

# 2. Students in all three clubs
all_three = math_club & science_club & art_club

# 3. Students in exactly two clubs
math_science = (math_club & science_club) - art_club
math_art = (math_club & art_club) - science_club
science_art = (science_club & art_club) - math_club

exactly_two = math_science | math_art | science_art

# 4. Verify Inclusion-Exclusion Principle
A = len(math_club)
B = len(science_club)
C = len(art_club)

AB = len(math_club & science_club)
AC = len(math_club & art_club)
BC = len(science_club & art_club)
ABC = len(all_three)

inclusion_exclusion = A + B + C - AB - AC - BC + ABC

# Display Results
print("Students in at least one club:", at_least_one)
print("Number of students in at least one club:", len(at_least_one))

print("\nStudents in exactly two clubs:", exactly_two)
print("Number of students in exactly two clubs:", len(exactly_two))

print("\nStudents in all three clubs:", all_three)
print("Number of students in all three clubs:", len(all_three))

print("\nVerification using Inclusion-Exclusion Principle")
print("A =", A)
print("B =", B)
print("C =", C)
print("A ∩ B =", AB)
print("A ∩ C =", AC)
print("B ∩ C =", BC)
print("A ∩ B ∩ C =", ABC)

print("\n|A ∪ B ∪ C| =", inclusion_exclusion)
print("Actual Union Size =", len(at_least_one))
