print("Welcome to the tip calculator")
total_bill=float(input("what was the total bill ?"))
tip=float(input("""how much tip would you like to give ?
          10 15 20 \n"""))
people=float(input("how many people split the bill ?"))
each_person_pay=total_bill+round((total_bill*tip/100)/people,2)
print(f"Each person should pay $ {each_person_pay}")
