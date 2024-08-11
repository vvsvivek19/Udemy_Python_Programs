def decorator(fun):
    def wrapper(msg):
        print("*" * 20)
        fun(msg)
        print("*" * 20)

    return wrapper

@decorator
def display(msg):
    print(msg)


#display = decorator(display)
display("How you doin?")
