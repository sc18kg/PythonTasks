def final_grade(gradea, gradeb, gradec):
    average_gradea = (gradea / 25) * 100
    average_gradeb = (gradeb / 50) * 100
    average_gradec = (gradec / 100) * 100

    return ((average_gradea * 0.25) +  (average_gradeb * 0.5) +  average_gradec) / 1.75

def determine_grade(average_grade):
    if average_grade >= 80:
        return 'A'
    elif average_grade >= 70:
        return 'B'
    elif average_grade >= 60:
        return 'C'
    elif average_grade >= 50:
        return 'D'
    elif average_grade >= 40:
        return 'E'
    else:
        return 'F'

name = input("Please enter your name: ")
gradea = int(input("Please enter your Homework Grade: "))
gradeb = int(input("Please enter your Assesment Grade: "))
gradec = int(input("Please enter your Final Exam Grade: "))

average_grade = str(final_grade(gradea, gradeb, gradec))
grade = determine_grade(int(round(float(average_grade))))

print(f"Hello {name} Your Final Grade is: " + average_grade, "which equates to a " + grade)



