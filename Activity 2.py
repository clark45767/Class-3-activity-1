weight =float(input("Enter your weight in kgs.."))
height =float(input("Enter your height in cm..."))
BMI =weight / (height*100)**2
if BMI <= 18.4:
    print("You are underweight..")
elif BMI <=24.9:
    print("Healthy...")
elif BMI <=29.9:
    print("Overweight..")
elif BMI<=34.9:
    print("Slightly over weight..")
else:
    print("Obese...")