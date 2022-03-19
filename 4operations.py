while True:
    try:
        num1=input("Please enter a number: ")
        num2=input("Please enter another number: ")
        answer=float(num1)+float(num2)
        print(answer)
    except ValueError:
        print("Please enter only numbers.")
        continue