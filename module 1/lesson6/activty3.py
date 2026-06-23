height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))

bmi = weight/(height/100)**2
bmi = round(bmi,2)

if bmi <=18.4:
    print(f"your bmi is {bmi}. you are underweight.")

elif bmi <=24.9:
    print(f"your bmi is {bmi}. you are healthy.")

elif bmi <=29.9:
    print(f"your bmi is {bmi}. you are overweight.")

elif bmi <=34.9:
    print(f"your bmi is {bmi}. you are severly overweight.")

elif bmi <=39.9:
    print(f"your bmi is {bmi}. you are obese.")

else:
    print(f"your bmi is {bmi}. you are severly obese.")