"""
This time we want to write calculations using functions and get the results. 
Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""
def perform_operation(operations, number):
    if not operations: return number
    if operations["sign"] == "*":
        return operations["value"] * number
    if operations["sign"] == "+":
        return operations["value"] + number
    if operations["sign"] == "-":
        return number - operations["value"] 
    if operations["sign"] == "/":
        return  number // operations["value"]

zero = lambda operations=None : perform_operation(operations, 0)
one = lambda operations=None : perform_operation(operations, 1)
two = lambda operations=None : perform_operation(operations, 2)
three = lambda operations=None : perform_operation(operations, 3)
four = lambda operations=None : perform_operation(operations, 4)
five = lambda operations=None : perform_operation(operations, 5)
six = lambda operations=None : perform_operation(operations, 6)
seven = lambda operations=None : perform_operation(operations, 7)
eight = lambda operations=None : perform_operation(operations, 8)
nine = lambda operations=None : perform_operation(operations, 9)

get_operation = lambda operation, num : {"sign": operation, "value": num}
plus = lambda num : get_operation("+", num)
minus = lambda num : get_operation("-", num)
times = lambda num : get_operation("*", num)
divided_by = lambda num : get_operation("/", num)

"""
-- best solution:

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y


id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x

-----eval-----
def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return "+%s" % n
def minus(n):      return "-%s" % n
def times(n):      return "*%s" % n
def divided_by(n): return "/%s" % n
"""