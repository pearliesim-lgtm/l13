def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def avg(x,y):
    return (x+y)/2
def perc(x,y):
    return (x/y)*100
def power(x,y):
    return x**y

print("Welcome to the calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Average")
print("6. Percentage")
print("7. Power")
print("8. Exit")
while True:
    choice=int(input("Enter your choice:"))
    if choice==8:
        break
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    if choice==1:
        print("Addition",add(x,y))
    elif choice==2:
        print("subtraction",sub(x,y))
    elif choice==3:
        print("Multiplication",mul(x,y))
    elif choice==4:
        print("Division",div(x,y))
    elif choice==5:
        print("Average",avg(x,y))
    elif choice==6:
        print("Percentage",perc(x,y))
    elif choice==7:
        print("Power",power(x,y))
    else:
        print("Invalid choice")
