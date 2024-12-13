height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / height ** 2
bmi_as_integer = round(bmi)
print(bmi_as_integer)

if bmi_as_integer < 18.5:
    print(f"Your bmi is {bmi_as_integer}, you are Underweight")
elif bmi_as_integer < 25:
    print(f"Your bmi is {bmi_as_integer}, you are Normal weight")
elif bmi_as_integer < 30:
    print(f"Your bmi is {bmi_as_integer}, you are Overweight")
elif bmi_as_integer < 35:
    print(f"Your bmi is {bmi_as_integer}, you are Obese")
else:
    print(f"Your bmi is {bmi_as_integer}, you are Clinically obese")