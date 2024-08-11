from collections import deque
students = [1,2,3,4,5,6,7,8,9,10]
students_queue = deque(students)

def serve():
    print(students_queue)
    students_queue.rotate(-1)
print("Breakfast")
serve()
print("Lunch")
serve()
print("Dinner")
serve()