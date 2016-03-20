# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(raw_input().strip())
students=[]
if(n>=2 and n<=5):
    while(n):
        name=raw_input().strip()
        grade=float(raw_input().strip())
        students.append([name, grade])
        n-=1

    students.sort()
    grades=list(set([student[1] for student in students]))
    grades.sort()
    #print grades
    result=grades[1]
    for student in students:
        if(result == student[1]):
            print student[0]