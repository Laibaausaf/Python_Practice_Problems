name=input("Enter your full name: ")
marks=[]
grade=[]
for i in range(5):
    marks.append(int(input(f"Enter your marks for subject {i+1}: ")))
    if marks[i]>=80 and marks[i]<100:
        grade.append("A")
    elif marks[i]>=70 and marks[i]<80:
        grade.append("B")
    elif marks[i]>=60 and marks[i]<70:
        grade.append("C")
    elif marks[i]>=50 and marks[i]<60:
        grade.append("D")
    else:
        grade.append("F")
    print(f"Grade of subject {i+1} is : {grade[i]}")