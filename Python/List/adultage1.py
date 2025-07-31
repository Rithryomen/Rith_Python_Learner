def filter_adult_students(ages):
    adult_list=[]
    for age in ages:
        if age >= 18:
            adult_list.append(age)
    return adult_list
student_age=[16,17,18,21,32,42,22,35]
adults=filter_adult_students(student_age)
print(f"Students in adult age: {adults}")