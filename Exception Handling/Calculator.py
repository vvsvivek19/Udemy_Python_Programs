class InvalidFormulaException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def evaluate(exp):
    f = exp.split()
    if len(f) != 3:
        raise InvalidFormulaException("Formula should have spaces!")
    if f[1] == '+' or f[1] == '-' or f[1] == '*' or f[1] == '/' or f[1] == '//':
        if f[1] == '/' and f[2] == '0':
            raise ZeroDivisionError('Cannot Divide by Zero')
        else:
            result= eval(exp)
            return result
    else:
        raise InvalidFormulaException('Formula should be in form ex: 10 + 2')

try:
    expression = input("Please enter a expression (Separated by space): ")
    res = evaluate(expression)
    print(res)
except (InvalidFormulaException,ZeroDivisionError) as msg:
    print(msg)

