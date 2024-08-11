class Book:
    def __init__(self,title=None,author=None,price=None):
        self.title = title
        self.author = author
        self.price = price
    def show_details(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print('Price:',self.price)

b = []
flag = 1

while flag == 1:
    ask = input("Do you wish to enter Book details? Type Y or N: ")
    if ask == 'y' or ask == 'Y':
        title = input("Please Enter the Book's Title: ")
        author = input("Please Enter the Author Name: ")
        price = input("Please Enter the price: ")
        try:
            price = float(price)
        except ValueError:
            print('Please Enter Valid amount!')
            continue
        print('')
        b.append(Book(title,author,price))
    else:
        flag = 0

print("All the details are: \n")
for x in b:
    x.show_details()
    print('')