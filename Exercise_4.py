def add(a,b):
    print(f"a+b = {a+b}")
def subtract(a,b):
    print (f"a-b={a-b}")
def multiply(a,b):
   print(f"a*b={a*b}")
def divide(a,b):
    if b == 0:
        print("We can't divide by zero")
    else:
        print(f"a / b={a/b}")

def show_all(a,b):
    add(a,b)
    subtract(a,b)
    multiply(a,b)
    divide(a,b)

show_all(10,4)


