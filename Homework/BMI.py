height_cm = int(input('Enter your height here (cm): '))
weight = int(input('Enter your weight here (kg): '))
height_m = height_cm / 100
BMI = weight / (height_m * height_m)
print(BMI)
if BMI < 16:
    print('Severely underweight')
elif 16 <= BMI <= 18.5:
    print('Underweight')
elif 18.5 <= BMI <= 25:
    print('Normal')
elif 25 <= BMI <= 30:
    print('Overweight')
else:
    print('Obese')