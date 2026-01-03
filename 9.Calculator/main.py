import design
print(design.calculator_design)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def calculator(first,second,operator):
    if operator=='+':
        return add(first,second)
    elif operator=='-':
        return subtract(first,second)
    elif operator=='*':
        return multiply(first,second)
    elif operator=='/':
        return division(first,second)

calculation=True
user_choice=''

def calculation():
    first_number=int(input("please enter first number"))
    accumulated_result=True
    while accumulated_result:
        user_operator=input("Please choose one of the opeator \n" \
        "+\n" \
        "-\n" \
        "*\n" \
        "/\n")
        second_number=int(input("please enter another number \n"))
        result=calculator(first_number,second_number,user_operator)
        user_choice=input(f"""Do you want to more operation with result {result}
                        y for yes n for no""")
        if user_choice=='n':
            accumulated_result=False
            print('\n'*100)
            return calculation()
        
print(calculation())






