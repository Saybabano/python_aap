def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b)+ " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b)+ " = " + str(answer))

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b)+ " = " + str(answer))

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b)+ " = " + str(answer))



print("_________________________")
print("_______calculater_________")
print("__________________________")
print()
print()

print("your choices are:")
print("A. Additon")
print("B.Subtraction")  
print("C.Multplication")
print("D.Division")
print("E.Exit")  
  
choice = input("input your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("inpur first number:"))
    b = int(input("input second number:"))
    add(a,b)
elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("inpur first number:"))
    b = int(input("input second number:"))
    sub(a,b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("inpur first number:"))
    b = int(input("input second number:"))
    mul(a,b)    
elif choice == "d" or choice == "D":
    print("Division ")
    a = int(input("inpur first number:"))
    b = int(input("input second number:"))
    div(a,b)    
elif choice == "e" or choice == "E":
    print("program ended 😊")
    quit()
else :
    print("you are choice is wrong.🙁")

