class Course:
    def __init__(self, course_name, course_duration, *book):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(x) for x in book]

    def show_details(self):
        i = 1
        print('Course name:', self.course_name)
        print('Course Duration:',self.course_duration)
        print('Suggested Books: ')
        for x in self.books:
            print(i,':',x) #when you try to print object of a python class then automatically the str function is called
            i = i + 1

    class Book:
        def __init__(self, book):
            self.book_name = book
        def __str__(self):
            return self.book_name
c1 = Course('Physics_101', 12, "Pradeep's Fundamental Physics",'NCERT Class 11th and 12th', 'HC Verma')
c1.show_details()
print('*'*40)
c2 = Course('Python', 10, 'Learn Python','Python Crash Course')
c2.show_details()