import Student,pickle

studs = [Student.Student(10,'John','CS'), Student.Student(20,'Ajay','EC'), Student.Student(30,'Vivek','IT')]

with open('Students.data','wb') as f:
    for s in studs:
        pickle.dump(s,f)