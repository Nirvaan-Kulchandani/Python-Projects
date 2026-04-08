# BMI CALCULATOR by Nirvaan_K, THAT CALCULATES BMI 
# AND ALSO TELLS THAT IT IS HOW MUCH GOOD OR BAD.

# (BMI = kg / m²)
print("A Good or Healthy BMI is generally considered between 18.5 to 24.9\n\n")

def Calculate_BMI(weight_kg, height_m):
    BMI = weight_kg/(height_m**2)
    return round(BMI, 1)

weight = float(input("Enter your weight in KiloGrams: "))
height = float(input("Enter your height in CentiMetres: "))

weight_kg = weight
height_m = (height/100)

BMI = Calculate_BMI(weight_kg, height_m)

print(f"Your BMI is: {BMI}\n")

if BMI < 18.5:
    print("You are Underweighted!!")

elif BMI >= 18.5 and BMI <= 20.9:
    print("Good!")

elif BMI >= 21 and BMI <= 22.6:
    print("Perfect Body!!!")

elif BMI >= 22.7 and BMI <= 24.9:
    print("Good!")

elif BMI == 25 and BMI <= 25.9:
    print("A bit heavy")

elif BMI >= 26 and BMI <= 229.9:
    print("OverWeighted!!")

else:
    print("Obese!")

print("Thank_YOU! for using our program!")