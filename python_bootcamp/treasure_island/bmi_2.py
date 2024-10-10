height = float(input("How tall are you in meters?"))
weight = float(input("What is your weight in kilograms?"))

bmi = int(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is: {bmi}. You are underweight.")
elif bmi < 22.0:
    print(f"Your BMI is: {bmi}. You are an ideal weight.")
elif bmi < 28:
    print(f"Your BMI is: {bmi}. You are slightly overweight.")
elif bmi < 32:
    print(f"Your BMI is: {bmi}. You are obese.")
else:
    print(f"Your BMI is: {bmi}. You are clinically obese.")