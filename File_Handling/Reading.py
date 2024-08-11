import Student,pickle
with open('Students.data','rb') as f:
    for i in range(3):
        s = pickle.load(f)
        s.display()