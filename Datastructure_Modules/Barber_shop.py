from collections import deque
customers = deque()
def all_customers():
    print(customers)
def walk_in(person):
    customers.append(person)
def serviced():
    serviced_person = customers.popleft()
    print(serviced_person,'was serviced')

walk_in('vivek')
walk_in('James')
walk_in('John')
walk_in('Virat')
walk_in('Kobe')
all_customers()
serviced()
all_customers()