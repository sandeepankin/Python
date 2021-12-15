for i in range(5):
    print()

print(".................Basic Calculator...................")

for i in range(5):
    print()

val1 = int(input("Enter Number 1: "))
val2 = int(input("Enter Number 2: "))

a=
"""
1: 'Addition'
2: 'Subraction'
3: 'Multiplication'
4: 'Division'
"""

print(a)
print()
op = int(input("Enter a value for the operation you want to apply: "))

if op==1:
    c = val1+val2
    print("The Result is",c)
elif op==2:
    if val1>val2:
        c = val1-val2
        print("The Result is",c)
    else:
        c = val1-val2
    print("The Result is",c)
elif op==3:
    c=val1*val2
    print("The Result is",c)
elif op==4:
    c=val1//val2
    print("The Result is", c)
else:
    print("Invalid Operation")


