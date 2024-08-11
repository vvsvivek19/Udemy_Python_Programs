class NegativeAgeException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def stage(age):
    try:
        if age < 0:
            raise NegativeAgeException("Age Cannot be negative")
        else:
            if age < 13:
                return 'Kid'
            elif age >= 13 and age < 19:
                return 'Teen'
            elif age >= 19 and age < 50:
                return 'Young'
            elif age >= 50:
                return "Old"
    except NegativeAgeException as msg:
        print(msg)
        return 'Program Ended with Exception'

try:
    Age = int(input("Please Enter Valid Age: "))
    current_stage = stage(Age)
    print(current_stage)
except ValueError as ve:
    print(ve)
