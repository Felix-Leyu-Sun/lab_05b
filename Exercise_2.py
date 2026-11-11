def get_input(prompt):
    return input(prompt)

def bmi(weight_kg, height_m):
    BMI = weight_kg / (height_m ** 2)
    return BMI

def bmi_category(BMI):
    if BMI < 18.5 :
        return "Underweight"
    if BMI < 25 :
        return "Normal weight"
    if BMI < 30 :
        return "Overweight"
    else :
        return "Obese"

KG = float(get_input("Enter your weight in kg: "))
HEIGHT = float(get_input("Enter your height in m: "))
BMI = bmi(KG, HEIGHT)
print(f"Your BMI level is {bmi_category(BMI)}")



