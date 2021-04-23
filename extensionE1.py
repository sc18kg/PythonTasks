
math = int(input("Please enter your maths mark:"))
chem = int(input("Please enter your chemistry mark:"))
physics = int(input("Please enter your physics mark: "))

average = (math + chem + physics) / 3

print("Your percentage across the three subjects was:" ,average)
if average < 40:
 print("You Failed")

if average >= 40 and average <50:
 print("You scored a grade: D")

if average >= 50 and average <60:
 print("You scored a grade: C")

if average >= 60 and average <70:
 print("You scored a grade: B")

if average >= 70:
 print("You scored a grade: A")

