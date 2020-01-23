# 45 * 3 = 555 , 56+9=77 , 56/6=4
# Faulty Calculater

a=int(input("Enter number #1:"))
b=int(input("Enter number #2:"))

query=input("What you do?:")
print("Enter + for Addition")
print("Enter - for Subtraction")
print("Enter * for Multiplication")
print("Enter / for Divition")

if a==45:
    if b==3:
        if query=="+":
            print("Your Answer is 555.")

if a==56:
    if b==9:
        if query=="+":
            print("Your Answer is 77.")
    elif b==6:
        if query=="/":
            print("Your Answer is 4.")

if a!=45 or b!=3:
    if a!=56 or b != 9:
        if b !=6:
           if query=="+":
               print("Your Answer is",a+b)
           elif query=="-":
               print("Your Answer is",a-b)
           elif query=="*":
               print("Your Answer is",a*b)
           elif query=="/":
               if b==0:
                   print("Division is not Possible.")
               else:
                   print("Your Answer is",a/b)
